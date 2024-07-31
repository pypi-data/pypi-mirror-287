#!/usr/bin/env python

import logging
from threading import Thread, Event
import time

import numpy as np
from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader, loadUiType
from PySide6.QtCore import Signal, Slot
import pyqtgraph as pg

from siglent_sds import SDS800X_Socket


class SDS_Acquisition:

    def __init__(self, **kwargs):
        """
        A class for a custom data acquisition method.
        """
        pass

    # Routine to acquire and serve data
    def acquire_data(self, host, channels, callback, stop_acquisition):
        """
        Routine to acquire and serve data in a loop.

        This is an example of configuring and running a custom acquisition while keeping it
        separated from the user interface thread. That is, this method runs in a separate thread to
        the main Qt event loop of the plot window. Data and communications must be passed in a
        thread-safe manner (e.g. via Qt Signals and Slots, Events). Manipulating Qt objects directly
        from this thread will cause Bad Things to happen.

        The ``host`` parameter should be a string which is the hostname or IP address of the device
        to connect to.

        The ``callback`` parameter will be called with the acquired data in the form
        ``callback(channels, time, data)`` where ``channels`` is a list of channel labels, ``time``
        is the time axis labels in seconds and ``data`` is the y-axis data in volts for each channel
        and waveform in the sequence. If a Qt :class:`~PySide6.QtCore.Signal` ``emit()`` method is
        used here then thread-safe data transfer will be achieved.

        The ``stop_acquisition`` parameter must be an :class:`~threading.Event` which, when set,
        indicates that the acquisition loop should be stopped.

        :param callback: Method to call with the acquired data.
        :param stop_acquisition: An Event to indicate acquisition should be stopped.
        """
        # Configure scope
        self.sds = SDS800X_Socket(host=host)
        # Wait for connection... crudely
        while not self.sds.ready():
            if stop_acquisition.is_set():
                return
            time.sleep(0.1)

        # Configure acquisition settings
        # TODO: Should activate selected channels first, otherwise max waveform size can change
        # since waveform request activates channel but waveform points wil be misconfigured.
        self.sds.waveform_start(0, block=False)
        self.sds.waveform_interval(1, block=False)
        self.sds.waveform_points(0, block=False)
        self.sds.trigger_mode("single", block=False)

        def handle_data(channels, time, data):
            # Send to callback function and reset trigger
            callback(channels, time, data)
            self.sds.trigger_mode("single", block=False)

        # Handle trigger status request, request waveforms if stopped
        def handle_trigger_status(data):
            if data == b"Stop\n":
                # Stopped, try to retrieve waveforms
                self.sds.get_waveforms(channels=channels, block=False, callback=handle_data)

        while not stop_acquisition.is_set():
            # Wait for empty queue so device should be ready
            if self.sds.ready():
                self.sds.send(":TRIG:STAT?", delimiter=b"\n", block=False, callback=handle_trigger_status)
            time.sleep(0.1)

        self.sds.close()


class PyQtGraph_Window(*loadUiType(__file__.removesuffix(".py") + ".ui")):

    #  Note: signals need to be defined inside a QObject class/subclass.
    #: Signal to indicate new data acquisition.
    data_acquired = Signal(list, np.ndarray, np.ndarray)

    def __init__(self):
        """
        Plot live data from the SDS8000X HD in a PyQtGraph window.
        """
        super().__init__(parent=None)
        self.setupUi(self)

        #: PyQtGraph :class:`~pyqtgraph.PlotItem` inside the :class:`~pyqtgraph.GraphicsLayoutWidget`.
        self.plot = self.graphicsLayoutWidget.addPlot()
        self.plot.setLabels(bottom="Time (s)", left="Value")
        self.waves = {
            "C1": self.plot.plot(pen=(255, 255, 0), antialias=False),
            "C2": self.plot.plot(pen=(255, 0, 255), antialias=False),
            "C3": self.plot.plot(pen=(0, 255, 255), antialias=False),
            "C4": self.plot.plot(pen=(0, 192, 0), antialias=False),
            "F1": self.plot.plot(pen=(255, 128, 0), antialias=False),
            "F2": self.plot.plot(pen=(255, 0, 0), antialias=False),
            "F3": self.plot.plot(pen=(0, 0, 255), antialias=False),
            "F4": self.plot.plot(pen=(0, 255, 0), antialias=False),
        }

        # Connect signals
        self.start_pushButton.clicked.connect(self.start_clicked)
        # Connect the signal for new data acquisition
        self.data_acquired.connect(self._update_data)

        #: Thread to run the acquisition in.
        self.thread = None
        #: An :class:`~threading.Event` to indicate the acquisition thread should stop.
        self.stop_acquisition = Event()

        #: Instance of our example custom acquisition class.
        self.acquisition = SDS_Acquisition()

    def start_clicked(self):
        """
        Handle starting and stopping of the acquisition when the UI button is clicked.
        """
        if self.start_pushButton.isChecked():
            # Clear existing traces
            for wave in self.waves.values():
                wave.setData()
            # Make and start the background thread to acquire data
            # Pass it the signal.emit as the callback function
            self.thread = Thread(
                target=self.acquisition.acquire_data,
                args=(
                    self.hostnameLineEdit.text(),
                    [cb.text() for cb in self.channels_groupBox.children() if type(cb) == QtWidgets.QCheckBox and cb.isChecked()],
                    self.data_acquired.emit,
                    self.stop_acquisition
                ),
            )
            self.stop_acquisition.clear()
            self.thread.start()
            self.start_pushButton.setText("&Stop")
        else:
            # Stop background thread
            self.stop_acquisition.set()
            self.start_pushButton.setText("&Start")

    def closeEvent(self, close_event):
        """
        On window close, stop the data acquisition thread and close connection to the device.
        """
        self.stop_acquisition.set()
        if self.thread:
            self.thread.join()

    def _update_data(self, channels, time, data):
        """
        Slot to receive acquired data and update the plot.
        """
        for ch_i, ch in enumerate(channels):
            self.waves[ch].setData(time, data[ch_i, 0])
            #self.waves[ch].setData(time, np.mean(data[ch_i], axis=0))


if __name__ == "__main__":
    import sys

    logging.basicConfig(level=(logging.DEBUG if "--debug" in sys.argv else logging.INFO))

    app = QtWidgets.QApplication(sys.argv)
    window = PyQtGraph_Window()
    window.show()
    sys.exit(app.exec())
