@echo off
echo Starting SPELLING app. Please wait ...

:: Activate the virtual environment
call python -m pipenv run python main.py

pause

:: Deactivate the virtual environment when you're done
exit
