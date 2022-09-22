""" Importing external modules """  # These you have to install with pip and pipwin

import psutil  # To cheack if a program is running or not
import pyttsx3  # For speaking
# Note: Speech recognition will not work without pyaudio so, install pyaudio by this '>>> python -m pip install pipwin  >>> python -m pipwin install pyaudio '. Also you need internet connection for spech recognition.
import speech_recognition as sr
import wikipedia
import webbrowser  # This is will be used for opening websites

# Selenium Modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # For chromedriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # For edgedriver

""" Importing inbuit modules """


""" J.A.R.V.I.S SourceCode """

# Initializing pyttsx3(Speaking capabilities) as engine
import datetime
import os
import subprocess
engine = pyttsx3.init()


# voices = engine.getProperty('voices') # Use this for female voice
# engine.setProperty('voice', voices[1].id)
# Changes the speed of speach or how fast the engine will speak
engine.setProperty('rate', 200)


def speak(*sentences):  # Speak function to speak using pyttsx3 module
    for sentence in sentences:
        engine.say(sentence)
        engine.runAndWait()


def caps(string):
    return ''.join((c.upper() if i == 0 or string[i-1] == ' ' else c) for i, c in enumerate(string))


def voiceRecognition():  # This will recongnize your voice and give text

    r = sr.Recognizer()  # Setting recognizer
    with sr.Microphone() as source:  # Taking input from microphone as source
        print("\n>>> Listening...")
        r.energy_threshold = 600  # Minimum audio energy to consider for recording
        r.pause_threshold = 2  # This will make recognition start after 1s
        # This will remove background noise
        r.adjust_for_ambient_noise(source, duration=1)
        # This will listen the speach and atore it in audio
        audio = r.listen(source)

    try:
        print(">>> Recognizing...")
        # This will recognize the audio and it will convert it into text and store it in speach
        speach = r.recognize_google(audio, language='en-in')
        print("   >>> You said:\n", "  ---", caps(speach), "\n")
        return speach
    except sr.UnknownValueError:  # Cannot comprehend speach
        # print(">>> error code: 1 \n   cannot comprehend \n")
        return ">>> error code: 1"
    except sr.RequestError:  # Request related error
        print(">>> error code: RequestError \n    --- Check your internet connection, boss")
        return ">>> error code: 2"


def time():  # This will speak time in 12 hour format
    time = datetime.datetime.now().strftime("%I:%M")
    speak(time)
    return time


def date():  # This will speak date
    currentDate = datetime.date.today()
    return currentDate


def wishMe():  # This will wish you according to time
    time = int(datetime.datetime.now().strftime("%H"))
    if time <= 12:
        speak("Good morning")
    elif time > 12 and time <= 18:
        speak("Good afternooon")
    else:
        speak("Good evening")


def intro():
    speak("i am jarvis a i, i was created by shivam on 31st august 2020. 2020 was not a good year for humanity due to china ahmm coronavirus pandemic. anyway i can help you with many things, just ask me boss")


"""
Choose greet from below:

0. jarvis at your service boss
1. how was your day boss
2. good night boss, have sweet dreams
3. anything else boss?

"""


def greet(whichGreet):  # This will greet you according to above choices
    if whichGreet == 0:
        speak("jarvis at your service boss")
    elif whichGreet == 1:
        speak("how was your day boss")
    elif whichGreet == 2:
        speak("good night boss, have sweet dreams")
    elif whichGreet == 3:
        speak("anything else boss?")

    else:
        speak("come on boss, you have entered 'invalid greet number'")


def path(path):
    var = path.replace("\\", "\\\\")
    return var


def openProgram(path):  # This opens the file
    try:
        os.startfile(path)
    except Exception:
        print(">>> Error code: File not found!, line 107")
        speak('file not found!')


def closeProgram(programName):  # This closes the program
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    # si.wShowWindow = subprocess.SW_HIDE # default
    # Closes the program
    subprocess.call(f'taskkill /F /IM {programName}', startupinfo=si)


def programRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
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
        try:
            # Chrome driver
            options = webdriver.ChromeOptions()
            options.add_experimental_option(
                'excludeSwitches', ['enable-logging', 'enable-automation'])
            br = webdriver.Chrome(
                executable=r'Resources\Selenium Drivers\chromedriver_win32\chromedriver.exe', options=options)
            br.maximize_window()
            # This line will make sure that this program waits for max 6s if the effect of a code is taking time to display
            br.implicitly_wait(60)
            return br
        except:
            # Chrome driver
            options = webdriver.ChromeOptions()
            options.add_experimental_option(
                'excludeSwitches', ['enable-logging', 'enable-automation'])
            br = webdriver.Chrome(
                ChromeDriverManager().install(), options=options)
            br.maximize_window()
            # This line will make sure that this program waits for max 6s if the effect of a code is taking time to display
            br.implicitly_wait(60)
            return br
    elif browserName == 'edge':
        br = webdriver.Edge(
            executable=r'Resources\Selenium Drivers\edgedriver_win64\msedgedriver.exe')
        br.maximize_window()
        br.implicitly_wait(60)
        try:
            # Chrome driver
            br = webdriver.Edge(EdgeChromiumDriverManager().install())
            br.maximize_window()
            br.implicitly_wait(60)
            return br
        except:
            # Chrome driver
            br = webdriver.Edge(EdgeChromiumDriverManager().install())
            br.maximize_window()
            br.implicitly_wait(60)
        return br

    # elif borwserName.lower().strip() == 'edge':
    #     br = webdriver.Edge(
    #         EdgeChromiumDriverManager().install())
    #     br.maximize_window()
    #     # This line will make sure that this program waits for max 6s if the effect of a code is taking time to display
    #     br.implicitly_wait(60)
    #     return br


if __name__ == '__main__':
    print(">>> JARVIS 1.0")

    wishMe()
    greet(0)

    loop = True
    sleep = False

    while loop == True:
        if sleep == False:
            query = voiceRecognition().lower()  # Getting input from user
            """ Basic queries """

            if "tell me the time" in query or "what is the time" in query:  # Giving currrent time
                print(f">>> Current time is {time()}")
                speak(f"current time is {time()}")

            elif "tell me the date" in query or "what is the date" in query:  # Giving currrent date
                print(f">>> Today is {date()}")
                speak(f"Today is {date()}")

            """ Introduction about A.I """

            if "who are you" in query or "about youself" in query:  # Whos is A.I
                intro()
            elif "who made you" in query or "who is your creator" in query:  # Who is creator of A.I
                speak("shivam made me while sipping coffee")
            elif "when were you made" in query or "what is date of birth" in query:  # When A.I was made
                speak("i was made on 31st august 2020")

            """ Wikipedia related queries """

            if "wikipedia" in query:  # Searches the wikipedia
                print(">>> Searching Wikipedia")
                speak("searching wikipeadia...")
                query = query.replace("on wikipedia", " ")
                query = query.replace("search", " ")
                results = wikipedia.summary(query, sentences=2)
                print("   --- Result: \n", results, "\n")
                speak(results)
                speak("do you want detail information about")
                speak(query)
                answer = voiceRecognition().lower()
                # Gives deep information about the queri searched
                if "yes" in answer or "yeah" in answer or "ya" in answer or "ha" in answer:
                    results = wikipedia.summary(query, sentences=10)
                    print("   --- Result: \n", results, "\n")
                    speak(results)

                elif "no" in answer or "na" in answer or "nah" in answer or "not now" in answer:
                    speak("okay!")
                else:
                    speak("didnt hear you boss, please repeat")
                    answer = voiceRecognition().lower()
                    if "yes" in answer or "yeah" in answer or "ya" in answer or "ha" in answer:
                        results = wikipedia.summary(query, sentences=10)
                        print("   --- Result: \n", results, "\n")
                        speak(results)
                    elif "no" in answer or "na" in answer or "nah" in answer or "not now" in answer:
                        speak("okay, but do you want")

            """ Opening websites """

            if "open youtube" in query:  # YouTube
                print(">>> Opening YouTube on browser")
                speak("Opening YouTube on browser")
                webbrowser.open("https://www.youtube.in/")
            elif "open facebook" in query:  # Facebook
                print(">>> Opening Facebook on browser")
                speak("Opening Facebook on browser")
                webbrowser.open("https://www.facebook.com/")
            elif "open twitter" in query:  # Twitter
                print(">>> Opening Twitter on browser")
                speak("Opening Twitter on browser")
                webbrowser.open("https://twitter.com/?lang=en")
            elif "open digicamp website" in query:  # Digicamp
                print(">>> Opening Digicamp on browser")
                speak("Opening Digicamp on browser")
                webbrowser.open("https://www.apsdigicamp.com/")
            elif "open gmail" in query:  # Gmail
                print(">>> Opening Gmail on browser")
                speak("Opening Gmail on browser")
                webbrowser.open("https://www.google.com/gmail/")
            elif "open whatsapp web" in query:  # Whatsapp web
                print(">>> Opening Whatsapp web on browser")
                speak(">>> Opening Whatsapp web on browser")
                webbrowser.open("https://web.whatsapp.com/")
            elif "open stack overflow" in query:  # Stackoverflow
                print(">>> Opening Stackoverflow on browser")
                speak("Opening Stackoverflow on browser")
                webbrowser.open("https://stackoverflow.com/")
            elif "open w 3 school" in query or "open w3school" in query or "open w3schools" in query:  # W3 school
                print(">>> Opening W3Schools on browser")
                speak("Opening W3Schools on browser")
                webbrowser.open("https://www.w3schools.com/")
            elif "open geeks for geeks" in query or "open geeksforgeeks" in query:  # GeeksForGeeks
                print(">>> Opening GeeksForGeeks on browser")
                speak("Opening GeeksForGeeks on browser")
                webbrowser.open("https://www.geeksforgeeks.org/")
            elif "open google" in query:  # Google
                print(">>> Opening Google on browser")
                speak("Opening Google on browser")
                webbrowser.open("https://www.google.in/")

            """ Opening programs """

            # VS code Opening
            if "open code" in query or "open vs code" in query:
                print(">>> Opening VS code")
                speak("Opening v s code")
                openProgram(
                    path(r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe"))
            elif "start code" in query or "start vs code" in query:
                print(">>> Opening VS code")
                speak("Opening v s code")
                openProgram(
                    path(r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe"))
            elif "run code" in query or "run vs code" in query:
                print(">>> Opening VS code")
                speak("Opening v s code")
                openProgram(
                    path(r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe"))
            # VS code Closing
            if "close code" in query or "close vs code" in query:
                print(">>> Closing VS code")
                speak("closing v s code")
                closeProgram("Code.exe")
            elif "stop code" in query or "stop vs code" in query:
                print(">>> Closing VS code")
                speak("closing v s code")
                closeProgram("Code.exe")
            elif "exit code" in query or "exit vs code" in query:
                print(">>> Closing VS code")
                speak("closing v s code")
                closeProgram("Code.exe")

            # Chrome Opening
            if "open chrome" in query or "run chrome" in query or "start chrome" in query:
                print(">>> Opening Chrome")
                speak("Opening chrome")
                openProgram(
                    path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
            # Chrome Closing
            if "close chrome" in query or "stop chrome" in query or "exit chrome" in query:
                print(">>> Closing Chrome")
                speak("Closing chrome")
                closeProgram("chrome.exe")

            # Command Prompt Opening
            if "open cmd" in query or "run cmd" in query or "start cmd" in query:
                print(">>> Opening Command Prompt")
                speak("Opening Command Prompt")
                openProgram(
                    path(r"C:\WINDOWS\system32\cmd.exe"))
            elif "open command prompt" in query or "run command prompt" in query or "start command prompt" in query:
                print(">>> Opening Command Prompt")
                speak("Opening Command Prompt")
                openProgram(
                    path(r"C:\WINDOWS\system32\cmd.exe"))
            # Command Prompt Closing
            if "close cmd" in query or "stop cmd" in query or "exit cmd" in query:
                print(">>> Closing Command Prompt")
                speak("Closing Command Prompt")
                closeProgram("chrome.exe")
            elif "close command prompt" in query or "stop command prompt" in query or "exit command prompt" in query:
                print(">>> Closing Command Prompt")
                speak("Closing Command Prompt")
                closeProgram("chrome.exe")

            # Anonymous Command Prompt Opening
            if "open anonymous cmd" in query or "run anonymous cmd" in query or "start anonymous cmd" in query:
                print(">>> Opening Anonymous Command Prompt")
                speak("Opening Anonymous Command Prompt")
                openProgram(
                    path(r"G:\cmd1.bat"))
            elif "open anonymous command prompt" in query or "run anonymous command prompt" in query or "start anonymous command prompt" in query:
                print(">>> Closing Anonymous Command Prompt")
                speak("Closing Anonymous Command Prompt")
                openProgram(
                    path(r"G:\cmd1.bat"))
            # Anonymous Command Prompt Closing
            if "close anonymous cmd" in query or "stop anonymous cmd" in query or "exit anonymous cmd" in query:
                print(">>> Closing Anonymous Command Prompt")
                speak("Closing Anonymous Command Prompt")
                closeProgram("cmd.exe")
            elif "close anonymous command prompt" in query or "stop anonymous command prompt" in query or "exit anonymous command prompt" in query:
                print(">>> Closing Anonymous Command Prompt")
                speak("Closing Anonymous Command Prompt")
                closeProgram("cmd.exe")

            """ Selenium related queries"""

            # Digicamp for Vivek
            if "open digicamp for vivek" in query or "digicamp for vivek" in query or "login on digicamp for vivek" in query or "sign in on digicamp for vivek" in query or "login on digicamp as vivek" in query or "sign in on digicamp as vivek" in query:
                try:
                    print(">>> Opening Digicamp for user kun020")
                    speak("Opening Digicamp for user kun020")
                    br = seleniumInitialisation('chrome')
                    # Opening Digicamp website on Chrome
                    br.get("https://www.apsdigicamp.com/")

                    br.find_element_by_class_name(
                        "loginbut").click()  # login button
                    br.find_element_by_xpath(  # Teachers button
                        "//*[@id='login-modal']/div/div/div/div/div/div/div/div[1]/div/a[2]").click()

                    # Selecting username and filling kun020
                    br.find_element_by_xpath(
                        "//*[@id='username']").send_keys("kun020")
                    # Selecting password and filling password
                    br.find_element_by_xpath(
                        '//*[@id="password"]').send_keys("password")
                    # Selecting schoolName and choosing APS Kunraghat
                    br.find_element_by_xpath(
                        '//*[@id="divSchool"]/div/div[1]/input').send_keys("ARMY PUBLIC SCHOOL KUNRAGHAT", Keys.ENTER)
                    # Selecting captcha input box
                    br.find_element_by_xpath('//*[@id="txtCaptcha"]').click()

                    wait = WebDriverWait(br, 60)
                    wait.until(EC.title_is(
                        "ARMY PUBLIC SCHOOL KUNRAGHAT - APSKUN | ~ TotalES ~"))

                    br.find_element_by_xpath('//*[@id="nav"]/li[3]/a').click()
                    br.find_element_by_xpath(
                        '//*[@id="dtblStudentAssign"]/tbody/tr/td[7]/button[1]').click()

                    closeProgram("chromedriver.exe")
                except:
                    print("\n   >>> closing webdriver\n")
                    closeProgram("chromedriver.exe")
                    print("   >>> webdriver closed\n")

            # Searching on YouTube
            search = query.replace("search", " ")
            search = search.replace("on youtube", " ")
            search = search.strip()
            if f"search {search} on youtube" in query or "on youtube" in query:
                try:
                    searchKeyword = search.replace(" ", "+")
                    print(caps(f"   --- Searching {search} on YouTube"))
                    speak(f"searching {search} on youtube")
                    br = seleniumInitialisation('chrome')
                    br.get(
                        f"https://www.youtube.in/results?search_query={searchKeyword}")

                    closeProgram("chromedriver.exe")
                except:
                    print("\n   >>> closing webdriver\n")
                    closeProgram("chromedriver.exe")
                    print("   >>> webdriver closed\n")

            # Searching on Google
            search = query.replace("search", " ")
            search = search.replace("on google", " ")
            search = search.strip()
            if f"search {search} on google" in query or "on google" in query or f"what is {search}" in query:
                try:
                    searchKeyword = search.replace(" ", "+")
                    print(caps(f"   --- Searching {search} on Google"))
                    speak(f"searching {search} on google")
                    br = seleniumInitialisation('chrome')
                    br.get("https://www.google.in/")

                    searchBox = br.find_element_by_xpath(
                        '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
                    searchBox.send_keys(search, Keys.ENTER)
                    closeProgram("chromedriver.exe")
                except:
                    print("\n   >>> closing webdriver\n")
                    closeProgram("chromedriver.exe")
                    print("   >>> webdriver closed\n")

            # Login on Facebook
            if "open facebook for" in query or "login on facebook" in query or "sign in on facebook" in query or "login on facebook" in query or "sign in on facebook" in query:
                loginName = query.replace("open facebook for", "")
                loginName = loginName.replace("login on facebook for", " ")
                loginName = loginName.replace("sign in on facebook for", " ")
                loginName = loginName.replace("login on facebook as", " ")
                loginName = loginName.replace("sign in on facebook as", " ")
                loginName = loginName.strip()

                # Login as Shivam
                if "shivam" in loginName:
                    try:
                        print("   --- Login as Shivam on Facebook")
                        speak("Login as Shivam on Facebook")

                        br = seleniumInitialisation('chrome')
                        br.get("https://www.facebook.com/")

                        userName = br.find_element_by_xpath('//*[@id="email"]')
                        userName.send_keys(9919248647)

                        password = br.find_element_by_xpath('//*[@id="pass"]')
                        password.send_keys("#Brahmand@05")

                        signUpButton = br.find_element_by_xpath(
                            '//*[@id="u_0_b"]')
                        signUpButton.click()

                        closeProgram("chromedriver.exe")
                    except:
                        print("\n   >>> closing webdriver\n")
                        closeProgram("chromedriver.exe")
                        print("   >>> webdriver closed\n")

                # Login as Vivek
                if "vivek" in loginName:
                    try:
                        print("   --- Login as Vivek on Facebook")
                        speak("Login as Vivek on Facebook")
                        br = seleniumInitialisation('chrome')
                        br.get("https://www.facebook.com/")

                        userName = br.find_element_by_xpath('//*[@id="email"]')
                        userName.send_keys(7269055756)

                        password = br.find_element_by_xpath('//*[@id="pass"]')
                        password.send_keys("Vivek.05")

                        signUpButton = br.find_element_by_xpath(
                            '//*[@id="u_0_b"]')
                        signUpButton.click()

                        closeProgram("chromedriver.exe")
                    except:
                        print("\n   >>> closing webdriver\n")
                        closeProgram("chromedriver.exe")
                        print("   >>> webdriver closed\n")

            """ A.I controls """

            if "kill yourself" in query or "terminate yourself" in query or "shutdwon yourself" in query:  # Stops the A.I
                print(">>> Shutting down\n")
                speak("Terminating myself")
                loop = False
            elif "hibernate yourself" in query or "go to sleep" in query:  # Puts the A.I to sleep
                sleep = True
                speak("wake me up whenever you need me! bosss")
            elif "don't disturb me" in query or "dont disturb me" in query:  # Puts the A.I to sleep
                sleep = True
                speak("as you wish boss")
        if sleep == True:
            print(">>> In sleep mode\n")
            while sleep == True:
                query = voiceRecognition().lower()
                if "wake up" in query:  # Wakes up the A.I
                    print(">>> Exiting Sleep mode\n")
                    sleep = False
                elif "kill yourself" in query or "terminate yourself" in query:  # Stops the A.I
                    print(">>> Shutting down\n")
                    speak("Terminating myself")
                    sleep = False
                    loop = False
