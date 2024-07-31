#!/usr/bin/env -S python -i

"""
Script to set up a :class:`SDS800X_Socket` object and interact with it using the python REPL.
"""

if __name__ == "__main__":

    import os
    import sys
    import logging
    import atexit

    from siglent_sds import SDS800X_Socket

    logging.basicConfig(level=(logging.DEBUG if "--debug" in sys.argv else logging.INFO))
    try:
        host = sys.argv[sys.argv.index("--host") + 1]
    except:
        print("WARNING: the default host IP address will likely be incorrect!")
        print("Usage:")
        print(f"{sys.argv[0]} --host <hostname>")
        host = "10.42.0.59"

    #: An instance of the :class:`~siglent_sds.SDS800X_Socket` class.
    sds = SDS800X_Socket(host=host)
    atexit.register(sds.close)
    print(80 * "-")
    print("Send commands to the Siglent SDS800X HD using the sds object. For example:")
    print(">>> sds.autoset()")
    print(">>> sds.run()")
    print(">>> sds.png()")
    print("Custom commands (that don't expect a response) can be sent like:")
    print('>>> sds.command("*RST")')
    print("Custom queries are commands that expect a response, such as:")
    print('>>> sds.print_query(":ACQ:POIN?")')
    print("1.00E+06")
    print(80 * "-")
