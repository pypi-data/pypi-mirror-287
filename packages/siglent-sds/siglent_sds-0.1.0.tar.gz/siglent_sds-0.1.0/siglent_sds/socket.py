import logging
import asyncio

from siglent_sds import SDS800X_Base

__all__ = ["SDS800X_Socket"]


class SDS800X_Socket(SDS800X_Base):
    """
    Class for the Siglent SDS800X HD oscilloscope connected via a network socket.

    :param host: IP address or hostname for the device.
    :param port: Port for raw TCP connections to the device.
    :param buffer_size: Size of read buffer.
    :param kwargs: Other keyword arguments are passed to :class:`~siglent_sds.base.SDS800X_Base`.
    """

    def __init__(self, host="10.42.0.59", port=5025, buffer_size=2**27, **kwargs):
        self._log = logging.getLogger(f"{__name__}.{__class__.__name__}")

        self._host = host
        self._port = int(port)
        self._buffer_size = int(buffer_size)

        # Task used to establish and maintain communication channels.
        self._connection_task = None

        # Call super class init to finish config, open connection etc
        super().__init__(**kwargs)

    async def _open_connection(self):
        """
        Coroutine to attempt to connect to a socket server.
        """
        first_attempt = True
        while True:
            if first_attempt:
                self._log.info(f"Connecting to server at {self._host}:{self._port}.")
                first_attempt = False
            try:
                self._reader, self._writer = await asyncio.open_connection(
                    host=self._host, port=self._port, limit=self._buffer_size
                )
            except Exception:
                self._log.debug("Unable to connect to server, will retry.")
                await asyncio.sleep(5.0)
            else:
                # Connection established, let the base class handle communications from here
                self._connection_name = self._writer.get_extra_info("peername")
                await self._handle_comms()
                self._log.info("Connection lost, will retry.")
                first_attempt = True
