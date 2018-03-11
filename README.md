# What this script does
This script schedules system shutdown at a pre-defined time (11 pm by default). That helps
to stop playing games and go to bed at a proper time. If computer is turned on after 
shutdown time, but before 12pm, the immediate shutdown command is triggered.

**Note**: shutdown time after 12pm and 6am is not supported. I don't think it's a real use case to plan
going to bed at a so late hour. 

# Compatibility
- All times are specified in a system-default timezone. Shutdown time may be between 6am and 12pm. 
- The script works only under Windows (tested under Windows 8)
- Script requires Python 3.x (tested under Python 3.6.3)

# Usage:
- Install latest python 3.x from https://www.python.org/downloads/windows/ 
- Download script from github https://raw.githubusercontent.com/Dmitriusan/SleepTimeEnforcer-windows/master/SleepTimeEnforcer.py
- Add it to autostart 
Open system 
```
python SleepTimeEnforcer.py 23:30
```

