@echo off
echo Starting POMODORO app. Please wait ...

:: Activate the virtual environment
call python -m pipenv run python pomo.py

:: Deactivate the virtual environment when you're done
exit
