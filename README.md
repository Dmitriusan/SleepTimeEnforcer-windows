# What this script does
This script schedules system shutdown at a pre-defined time (23:00 by default). That helps
to stop playing games and go to bed at a proper time. If computer is turned on after 
shutdown time, but before 23:59, the immediate shutdown is triggered.

**Note**: shutdown time between 00:00 and 12:00 is not supported. That 

# Compatibility
- The shutdown time is specified in a system-default timezone in a 24-hour format. 
- Shutdown time may be between 12:01 to 23:59. 
- The script works only under Windows (tested under Windows 8)
- Script requires Python 3.x (tested under Python 3.6.3)

# Usage:
* Install latest python 3.x from https://www.python.org/downloads/windows/ 
* Download script from github https://raw.githubusercontent.com/Dmitriusan/SleepTimeEnforcer-windows/master/SleepTimeEnforcer.py
somewhere (e.g. to "C:\Users\user\AppData\Local\Programs\") 
* Add it to autostart. Go to Start->Task Scheduler and choose action->"create basic task"
** Name: Force sleep time
** Trigger: When I log on
** Action: start a program
*** Program/script "C:\Users\user\AppData\Local\Programs\SleepTimeEnforcer.py" (actually the path where you downloaded the program)
*** Add arguments: "23:00" (actually, the time after which the computer should be turned off. Only 24-hour format is supported)
** Next> Finish
* Now, log off and log on (or just reboot the computer) 

