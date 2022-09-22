@echo off
echo === This will install required modules for the virtual envrinment
python -m pip install -r .\requirements_database.txt
echo     --- Installing pyaudio
python -m pip install .\PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
cmd /k
@echo on