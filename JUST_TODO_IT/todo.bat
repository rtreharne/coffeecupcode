@echo off
echo Starting TODO app. Please wait ...

:: Activate the virtual environment
call python -m pipenv run python todo.py

:: Deactivate the virtual environment when you're done
exit
