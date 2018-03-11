import sys
from datetime import datetime, date, time
import subprocess
import pprint
import math


def error_out(message):
    """
    Print the error message and exit
    :param message: error message
    """
    print("ERROR: " + message)
    exit(1)


def get_shutdown_time():
    if len(sys.argv) == 1:  # If no arguments have been specified to script
        shutdown_time = time(23, 0)
    elif len(sys.argv) == 2:  # If shutdown time has been explicitly specified
        custom_shutdown_time_str = sys.argv[1]
        try:
            shutdown_time = datetime.strptime(custom_shutdown_time_str, "%H:%M").time()
        except ValueError:
            error_out("Can not parse time " + custom_shutdown_time_str)
    else:
        error_out("Too many arguments specified")
    if time(0, 0) < shutdown_time <= time(6, 0):
        error_out("Shutdown time between 00:00AM and 6:00AM is not supported.")
    return shutdown_time


def main():
    shutdown_final_countdown_seconds = 60  # Value of argument passed to shutdown command.

    shutdown_time = get_shutdown_time()
    time_delta = datetime.combine(date.today(), shutdown_time) - datetime.now()
    time_delta_seconds = math.floor(time_delta.total_seconds())

    sleep_time = time_delta_seconds - shutdown_final_countdown_seconds

    if 0 < time_delta_seconds < shutdown_final_countdown_seconds:
        shutdown_final_countdown_seconds = time_delta_seconds
        sleep_time = 0
    elif time_delta_seconds < 0:
        sleep_time = 0
        shutdown_final_countdown_seconds = 1  # Shutdown immediately

    # Using powershell is required here, because if shutdown time is > 10 minutes,
    # shutdown.exe issues a warning 10 minutes before shutdown. It disrupts user when playing games
    # See https://superuser.com/a/559755 for details
    command = ["start", "powershell.exe", "-WindowStyle Hidden", "-Command",
               "sleep %s; shutdown -s -t %s" % (sleep_time, shutdown_final_countdown_seconds)]
    print("Running command " + pprint.pformat(command))
    subprocess.check_call(command)


if __name__ == "__main__":
    main()
