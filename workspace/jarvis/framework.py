# >> Importing external modules  # These you have to install with pip and pipwin

import psutil  # To cheack if a program is running or not
import pyttsx3  # For speaking
# Note: Speech recognition will not work without pyaudio so, install pyaudio by this '>> python -m pip install pipwin  >> python -m pipwin install pyaudio '. Also you need internet connection for spech recognition.
import speech_recognition as sr

# Selenium Modules
from selenium import webdriver

# GUI Modules
# To communicate with GUI(it will enable us to access javacript functions(in file at 'GUI/JS/index.js') in python code)
import eel
# To create GUI thread so that our engine can run along with GUI(engine is python code)
import threading


import easygui  # To get the path of files/folder with GUI (Based on Tkinter)
import pygame  # To play background music

# >> Importing inbuit modules
import datetime
import os
import subprocess
import getpass  # To obtain user name which is logged in on this machine

# Initializing pyttsx3(Speaking capabilities) as engine
engine = pyttsx3.init()

# voices = engine.getProperty('voices') # Use this for female voice
# engine.setProperty('voice', voices[1].id)
# Changes the speed of speach or how fast the engine will speak
engine.setProperty('rate', 200)

""" GUI code Functions """

eel.init('wb')

eelThread = None
eelSubThread = None


def eelStart():
    """
    This will be called from ellThreadInitialization to start eel(GUI)

    """

    eel.start(r"main.html", size=(600, 610), mode='edge')


def eelSubThreadInitialization():
    global eelSubThread
    eelSubThread = threading.Thread(target=eelStart)
    eelSubThread.start()
    eelSubThread.join()
    try:
        pygame.mixer.music.stop()
        pygame.quit()
    except:
        pass
    closeProgram('jarvis.exe')


def eelThreadInitialization():
    """
    This will create a thread in which GUI will run by eel

    """
    global eelThread
    eelThread = threading.Thread(target=eelSubThreadInitialization)
    eelThread.start()


def printGUI(result):
    """
    This will show the result in GUI

    ARGUMENTS:

        --- result: pass the result which will be shown to the user

    """
    eel.output(result)


def eelStatus(status):
    """
    This will show the status of the A.I

    ARGUMENTS:

        --- status: pass the status of the A.I

    """

    eel.ai_status(status)


def speak(*sentences):
    """ Speak function to speak using pyttsx3 module """

    for sentence in sentences:
        engine.say(sentence)
        engine.runAndWait()


def caps(string):
    """ Returns the string with proper capitalisation """

    return ''.join((c.upper() if i == 0 or string[i - 1] == ' ' else c) for i, c in enumerate(string))


def voiceRecognition():
    """ This will recongnize your voice and give text """

    r = sr.Recognizer()  # Setting recognizer
    with sr.Microphone() as source:  # Taking input from microphone as source
        eelStatus("Listening...")
        # r.energy_threshold = 200  # Minimum audio energy to consider for recording
        r.pause_threshold = 0.5  # This will make recognition start after 1s
        # This will remove background noise
        r.adjust_for_ambient_noise(source, duration=1)
        # This will listen the speach and atore it in audio
        audio = r.listen(source)

    try:
        eelStatus("Recognizing...")
        # This will recognize the audio and it will convert it into text and store it in speach
        speach = r.recognize_google(audio, language='en-in')
        eelStatus("Working on it...")
        # previousOuputValue = eel.getOutputValue()()
        printGUI(f"You said:\n--- {caps(speach)}")
        return speach
    except sr.UnknownValueError:  # Cannot comprehend speach

        return ">> error code: 1"
    except sr.RequestError as e:  # Request related error
        eelStatus("No Internet Connection!")
        return f">> error code: 2\n {e}"


def voiceRecognition_SleepMode():
    """ This will recongnize your voice and give text """

    r = sr.Recognizer()  # Setting recognizer
    with sr.Microphone() as source:  # Taking input from microphone as source
        eelStatus("Listening...")
        r.energy_threshold = 200  # Minimum audio energy to consider for recording
        r.pause_threshold = 0.5  # This will make recognition start after 1s
        # This will remove background noise
        r.adjust_for_ambient_noise(source, duration=1)
        # This will listen the speach and atore it in audio
        audio = r.listen(source)

    try:
        eelStatus("Recognizing...")
        # This will recognize the audio and it will convert it into text and store it in speach
        speach = r.recognize_google(audio, language='en-in')
        return speach
    except sr.UnknownValueError:  # Cannot comprehend speach

        return ">> error code: 1"
    except sr.RequestError:  # Request related error
        eelStatus("No Internet Connection!")
        return ">> error code: 2"


def time():
    """ This will speak time in 12 hour format """

    currentTime = datetime.datetime.now().strftime("%I:%M")
    return currentTime


def date():
    """ This will return date """

    currentDate = datetime.date.today()
    return currentDate


def wishMe():
    """ This will wish you according to time- """

    currentTime = int(datetime.datetime.now().strftime("%H"))
    if currentTime <= 12:
        return "Good morning!"
    elif 12 < currentTime <= 18:
        return "Good afternooon!"
    else:
        return "Good evening!"


def intro():
    speak(
        "i am jarvis a i, i was created by shivam on 31st august 2020. 2020 was not a good year for humanity due to china ahmm coronavirus pandemic. anyway i can help you with many things, just ask me boss")


"""
Choose greet from below:

0. jarvis at your service boss
1. how was your day boss
2. good night boss, have sweet dreams

"""


def greet(whichGreet):
    """ This will greet you according to above choices """

    if whichGreet == 0:
        speak("ready to help you boss!")
    elif whichGreet == 1:
        speak("how was your day boss")
    elif whichGreet == 2:
        speak("good night boss, have sweet dreams")

    else:
        speak("come on boss, you have entered 'invalid greet number'")


def path(pathToFormat):
    var = pathToFormat.replace("\\", "\\\\")
    return var


def availablePrograms(searchMode, *programNames):
    """
    DESCRIPTION: It will return a dictionary of available program and their programs

    ARGUMENT:  searchMode- startMode or deepMode

    """

    if searchMode == 'startMode':
        if programNames == ():
            programList = {}
            user = getpass.getuser()
            for root, dirs, files in os.walk(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"):
                for _ in dirs:
                    for file in files:
                        songPath = root + '/' + file
                        programList.update({file: songPath})
            for root, dirs, files in os.walk(rf"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"):
                for _ in dirs:
                    for file in files:
                        songPath = root + '/' + file
                        programList.update({file: songPath})
            return programList
        else:
            programData = {}
            for programName in programNames:
                user = getpass.getuser()
                for root, dirs, files in os.walk(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"):
                    for _ in dirs:
                        for file in files:
                            if programName.lower() in file.lower():
                                songPath = root + '/' + file
                                programData.update({file: songPath})
                for root, dirs, files in os.walk(
                        rf"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs"):
                    for _ in dirs:
                        for file in files:
                            if programName.lower() in file.lower():
                                songPath = root + '/' + file
                                programData.update({file: songPath})
            return programData
    elif searchMode == 'deepMode':
        if programNames == ():
            user = getpass.getuser()
            programList = {}
            for root, dirs, files in os.walk(r"C:\Program Files (x86)"):
                for _ in dirs:
                    for file in files:
                        if file.endswith('.exe'):
                            songPath = root + '/' + file
                            programList.update({file: songPath})
            for root, dirs, files in os.walk(r"C:\Program Files"):
                for _ in dirs:
                    for file in files:
                        if file.endswith('.exe'):
                            songPath = root + '/' + file
                            programList.update({file: songPath})
            for root, dirs, files in os.walk(rf"C:\Users\{user}\AppData\Local\Programs"):
                for _ in dirs:
                    for file in files:
                        if file.endswith('.exe'):
                            songPath = root + '/' + file
                            programList.update({file: songPath})
            return programList
        else:
            user = getpass.getuser()
            programData = {}
            for programName in programNames:
                for root, dirs, files in os.walk(r"C:\Program Files (x86)"):
                    for _ in dirs:
                        for file in files:
                            if programName.lower() in file.lower():
                                songPath = root + '/' + file
                                programData.update({file: songPath})
                for root, dirs, files in os.walk(r"C:\Program Files"):
                    for _ in dirs:
                        for file in files:
                            if programName.lower() in file.lower():
                                songPath = root + '/' + file
                                programData.update({file: songPath})
                for root, dirs, files in os.walk(rf"C:\Users\{user}\AppData\Local\Programs"):
                    for _ in dirs:
                        for file in files:
                            if programName.lower() in file.lower():
                                songPath = root + '/' + file
                                programData.update({file: songPath})
            return programData


def openProgram(searchMode, *programNames):
    """
    This function will open specified programs

    ARGUMENTS:

        --- searchMode: startMode or deepMode or pathMode
        --- *programNames: name of programs or path of programs

    """
    if searchMode == 'startMode':
        for programName in programNames:
            programList = availablePrograms('startMode', programName)
            if programList == {}:
                return False
            else:
                for availableProgramName, availableProgramPath in programList.items():
                    if programName.lower().strip() in availableProgramName.lower().strip():
                        os.startfile(availableProgramPath)
                        return True
    elif searchMode == 'pathMode':
        try:
            for programPath in programNames:
                os.startfile(programPath)
                return True
        except:
            return False
    elif searchMode == 'deepMode':
        for programName in programNames:
            programList = availablePrograms('deepMode', programName)
            if programList == {}:
                return False
            else:
                for availableProgramName, availableProgramPath in programList.items():
                    if programName.lower().strip() in availableProgramName.lower().strip():
                        os.startfile(availableProgramPath)
                        return True


def closeProgram(*programNames):
    """ This closes the program """
    try:
        for programName in programNames:
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            # si.wShowWindow = subprocess.SW_HIDE # default
            # Closes the program
            subprocess.call(f'taskkill /F /IM {programName}', startupinfo=si)
        return True
    except:
        return False


def programRunning(processName):
    """ Check if there is any running process that contains the given name processName. """

    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


# It will setup selenium, use "br = seleniumInitialisation('chrome')" to initialise
def seleniumInitialisation(browserName):
    browserName = browserName.lower().strip()
    if browserName == 'chrome':
        # Chrome driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            'excludeSwitches', ['enable-logging', 'enable-automation'])
        br = webdriver.Chrome(
            executable_path=r'Resources\Selenium Drivers\chromedriver_win32\chromedriver.exe', options=options)
        br.maximize_window()
        # This line will make sure that this program waits for max 6s if the effect of a code is taking time to display
        br.implicitly_wait(60)
        return br
    elif browserName == 'msedge':
        # Edge Driver
        br = webdriver.Edge(
            executable_path=r'Resources\Selenium Drivers\edgedriver_win64\msedgedriver.exe')
        br.maximize_window()
        br.implicitly_wait(60)
        return br


currentWorkingDirectory = os.getcwd()


class Settings:
    @staticmethod
    def settingsInitializtion():
        """
        Creates the 'data' folder if non created and creats the song folder containing the settings related to song playback

        """
        if os.path.exists('data'):
            os.chdir('data')
            if os.path.exists('songs'):
                os.chdir('songs')
                if os.path.exists('song.list'):
                    pass
                else:
                    with open('song.list', 'w') as file:
                        file.write('')
            else:
                os.mkdir('songs')
        else:
            os.mkdir('data')
            os.chdir('data')
            os.mkdir('songs')
            os.chdir('songs')
            with open('song.list', 'w') as file:
                file.write('')
        os.chdir(currentWorkingDirectory)

    @staticmethod
    def songsFolderPath():
        """
        Returns the path of the folder containing the songs from the file cotaining settings related to song playback

        """
        os.chdir('data')
        os.chdir('songs')
        with open('song.list') as file:
            fileContent = file.read()
        if fileContent == '':
            printGUI('Choose a default Song folder')
            eelStatus('Settings...')
            speak('Choose a default song folder')
            songPath = InputOperations.getFolderPath("Choose a Song Folder")
            notFound = True
            for root, dirs, files in os.walk(songPath):
                for file in files:
                    if file.lower().endswith('.mp3') or file.lower().endswith('.wav'):
                        notFound = False
                        break
            if files == []:
                speak('No music found')
                printGUI('No music found')
                printGUI('Choose a default Song folder')
                speak('Choose a default song folder')
                songPath = InputOperations.getFolderPath("Choose a Song Folder")
                notFound = False
            if notFound:
                speak('No music found')
                printGUI('No music found')
                printGUI('Choose a default Song folder')
                speak('Choose a default song folder')
                songPath = InputOperations.getFolderPath("Choose a Song Folder")
            with open('song.list', 'w') as file:
                file.write(songPath)
            os.chdir(currentWorkingDirectory)
            return songPath
        else:
            os.chdir(currentWorkingDirectory)
            return fileContent


class AudioPlayer:

    @staticmethod
    def play(songPath):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(songPath)
            pygame.mixer.music.play()
        except:
            pass

    @staticmethod
    def stop():
        try:
            pygame.mixer.music.stop()
        except:
            pass

    @staticmethod
    def pause():
        try:
            pygame.mixer.music.pause()
        except:
            pass

    @staticmethod
    def resume():
        try:
            pygame.mixer.music.unpause()
        except:
            pass

    @staticmethod
    def quit():
        try:
            pygame.quit()
        except:
            pass


class InputOperations:
    @staticmethod
    def getFolderPath(titleOfWindow):
        """
        Fires a GUI Window to get path of the folder

        ARGUMENTS:
        >> titleOfWindow: sets the title of the window


        """
        folderPath = easygui.diropenbox(
            titleOfWindow)  # easygui is a Tkinter based libaray for dialog boxes
        return folderPath


def songListGenerator():
    songsFolderPath = Settings.songsFolderPath()
    songs = {}
    for root, dirs, files in os.walk(songsFolderPath):
        for file in files:
            pathOfSong = os.path.join(root, file)
            if file.lower().endswith('.mp3') or file.lower().endswith('.wav'):
                songs.update({file: pathOfSong})
    return songs
