""" TODO: create a prettier function which will format the output if viewport is < 800px in GUI"""
""" TODO: modified the code till line 319 """

from functions import *

eelThread = None


def eelStart():
    """
    This will be called from ellThreadInitialization to start eel(GUI)

    """
    eel.start("index.html", size=(700, 600), mode='edge')


def eelThreadInitialization():
    """
    This will create a thread in which GUI will run by eel

    """
    global eelThread
    eelThread = threading.Thread(target=eelStart)
    eelThread.start()


def eelClosed():
    if eelThread.is_alive() == False:
        sys.exit()


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



def main():
    """
    Main function which contain all the brain of the A.I

    """
    print(">>> JARVIS 1.0")
    printGUI("Ready to help you!")
    eelClosed()
    eelStatus(f"{wishMe()}")
    speak(wishMe())
    greet(0)

    
    sleep = False

    while True:
        eelClosed()
        if sleep == False:
            if eelThread.is_alive() == False:
                sys.exit()
            query = voiceRecognition().lower()  # Getting input from user
            """ Basic queries """

            if "tell me the time" in query or "what is the time" in query:  # Giving currrent time
                printGUI(f"Current time is {time()}")
                print(f">>> Current time is {time()}")
                speak(f"current time is {time()}")

            elif "tell me the date" in query or "what is the date" in query:  # Giving currrent date
                printGUI(f"Today is {date()}")
                print(f">>> Today is {date()}")
                speak(f"Today is {date()}")

                """ Introduction about A.I """

            elif "who are you" in query or "about youself" in query:  # Whos is A.I
                intro()
            elif "who made you" in query or "who is your creator" in query:  # Who is creator of A.I
                printGUI(f"Shivam Shandilya")
                speak("Shivam Shandilya")
            elif "when were you made" in query or "what is date of birth" in query:  # When A.I was made
                printGUI(caps("I was made on 31st august 2020"))
                speak("i was made on 31st august 2020")

                """ Wikipedia related queries """

            elif "search on wikipedia" in query:  # Searches the wikipedia
                eelStatus(f"Searching Wikipedia")
                print(">>> Searching Wikipedia")
                speak("searching wikipeadia...")
                query = query.replace("on wikipedia", " ")
                query = query.replace("search", " ")
                results = wikipedia.summary(query, sentences=2)
                eelStatus(f"Result: \n{results} \n")
                print("   --- Result: \n", results, "\n")
                speak(results)
                printGUI(f"Do you want detail information about it")
                speak("do you want detail information about it")
                answer = voiceRecognition().lower()
                # Gives deep information about the queri searched
                if "yes" in answer or "yeah" in answer or "ya" in answer or "ha" in answer:
                    results = wikipedia.summary(query, sentences=10)
                    printGUI(f"Result: \n{results}\n")
                    print("   --- Result: \n", results, "\n")
                    speak(results)

                elif "no" in answer or "na" in answer or "nah" in answer or "not now" in answer:
                    eelStatus(f"Okay!")
                    speak("okay!")
                else:
                    printGUI(caps("didnt hear you boss, please repeat"))
                    speak("didnt hear you boss, please repeat")
                    answer = voiceRecognition().lower()
                    if "yes" in answer or "yeah" in answer or "ya" in answer or "ha" in answer:
                        results = wikipedia.summary(query, sentences=10)
                        printGUI(f"Result: \n{results}\n")
                        print("   --- Result: \n", results, "\n")
                        speak(results)
                    elif "no" in answer or "na" in answer or "nah" in answer or "not now" in answer:
                        eelStatus(f"Okay!")
                        speak("okay!")

                """ launching websites """

            elif "open youtube" in query:  # YouTube
                printGUI("Launching YouTube on browser.")
                print(">>> launching YouTube on browser")
                speak("launching YouTube on browser")
                webbrowser.open("https://www.youtube.in/")
            elif "open facebook" in query:  # Facebook
                printGUI("Launching Facebook on browser.")
                print(">>> launching Facebook on browser")
                speak("launching Facebook on browser")
                webbrowser.open("https://www.facebook.com/")
            elif "open twitter" in query:  # Twitter
                printGUI("Launching Twitter on browser.")
                print(">>> launching Twitter on browser")
                speak("launching Twitter on browser")
                webbrowser.open("https://twitter.com/?lang=en")
            elif "open digicamp website" in query:  # Digicamp
                printGUI("Launching Digicamp on browser.")
                print(">>> launching Digicamp on browser")
                speak("launching Digicamp on browser")
                webbrowser.open("https://www.apsdigicamp.com/")
            elif "open gmail" in query:  # Gmail
                printGUI("Launching Gmail on browser.")
                print(">>> launching Gmail on browser")
                speak("launching Gmail on browser")
                webbrowser.open("https://www.google.com/gmail/")
            elif "open whatsapp web" in query:  # Whatsapp web
                printGUI("Launching Whatsapp web on browser.")
                print(">>> launching Whatsapp web on browser")
                speak(">>> launching Whatsapp web on browser")
                webbrowser.open("https://web.whatsapp.com/")
            elif "open stack overflow" in query:  # Stackoverflow
                printGUI("Launching Stackoverflow on browser.")
                print(">>> launching Stackoverflow on browser")
                speak("launching Stackoverflow on browser")
                webbrowser.open("https://stackoverflow.com/")
            elif "open w 3 school" in query or "open w3school" in query or "open w3schools" in query:  # W3 school
                print(">>> launching W3Schools on browser")
                speak("launching W3Schools on browser")
                webbrowser.open("https://www.w3schools.com/")
            elif "open geeks for geeks" in query or "open geeksforgeeks" in query:  # GeeksForGeeks
                printGUI("Launching GeeksForGeeks on browser.")
                print(">>> launching GeeksForGeeks on browser")
                speak("launching GeeksForGeeks on browser")
                webbrowser.open("https://www.geeksforgeeks.org/")
            elif "open google" in query:  # Google
                printGUI("Launching Google on browser.")
                print(">>> launching Google on browser")
                speak("launching Google on browser")
                webbrowser.open("https://www.google.in/")

                """ Showing Intalled Applications """

            elif "show my apps" in query or "show me my apps" in query or "show my application" in query or "show me my application" in query:
                printGUI("These are your apps in startmenu")
                print(">>> These are your apps in Start Menu")
                speak("\n These are your apps in startmenu")
                appList = list(availablePrograms('startMode').keys())
                print(
                    "\n##################################### START MENU APPLICATION #####################################\n")
                applicationList = "START MENU:\n\n"
                for index, application in enumerate(appList):
                    application = application.replace(".lnk", "")
                    applicationList +=  f"{index+1}. {caps(application)}\n"
                    print(f"{index+1}. {caps(application)}")
                printGUI(applicationList)
            elif "deep search my apps" in query or "deep search my application" in query or "deeply search my apps" in query or "deeply search my application" in query:
                printGUI("SEARCHING APPS DEEPLY!  <<<\n--- May take few minutes")
                print(
                    "\n>>> SEARCHING APPS DEEPLY!  <<<\n\n    --- May take few minutes")
                speak('Searching apps deeply, may take few minutes')
                deepSearchedAppList = list(
                    availablePrograms('deepMode').keys())
                printGUI("These are your apps in startmenu")
                print(">>> These are your apps in startmenu")
                speak("\n These are your apps in startmenu")
                appList = list(availablePrograms('startMode').keys())
                applicationList = "START MENU:\n\n"
                print(
                    "\n##################################### START MENU APPLICATION #####################################\n")
                for index, application in enumerate(appList):
                    application = application.replace(".lnk", "")
                    applicationList +=  f"{index+1}. {caps(application)}\n"
                    print(f"{index+1}. {caps(application)}")
                printGUI(applicationList)
                speak('and these are apps after searching deeply')
                applicationList = "\nDEEP SEARCHED APPLICATION:\n\n"
                print(
                    "\n##################################### DEEP SEARCHED APPLICATION #####################################\n")
                for index, application in enumerate(deepSearchedAppList):
                    application = application.replace(".exe", "")
                    applicationList +=  f"{index+1}. {caps(application)}\n"
                    print(f"{index+1}. {caps(application)}")
                printGUI(applicationList)
            else:

                """ launching programs """
                query = query.replace('programme', 'program')
                programName = query.replace(
                    'launch program named ', '').replace(
                    'launch app named ', '').replace(
                    'launch application named ', '').replace('from start menu', '').replace('from deep search', '').replace('from deep searched', '').replace('from deeply searched', '').replace('from deeply search', '').strip()

                if f"launch application named {programName} from start menu" in query or f"run application named {programName} from start menu" in query or f"open application named {programName} from start menu" in query or f"launch app named {programName} from start menu" in query or f"run app named {programName} from start menu" in query or f"open app named {programName} from start menu" in query or f"launch program named {programName} from start menu" in query or f"run program named {programName} from start menu" in query or f"open program named {programName} from start menu" in query:
                    if openProgram('startMode', programName):
                        printGUI(f"Launching {programName} from Start Menu")
                        print(f">>> Launching {programName} from Start Menu")
                        speak(f"Launching {programName} from Start Menu")
                        openProgram('startMode', programName)
                    else:
                        printGUI("Program not found!")
                        speak("program not found!")

                elif f"launch application named {programName} from deep search" in query or f"run application named {programName} from deep search" in query or f"open application named {programName} from deep search" in query or f"open application named {programName} from deep searched" in query or f"launch application named {programName} from deep searched" in query or f"run application named {programName} from deep searched" in query or f"open application named {programName} from deeply searched" in query or f"launch application named {programName} from deeply searched" in query or f"run application named {programName} from deeply searched" in query or f"launch application named {programName} from deeply search" in query or f"run application named {programName} from deeply search" in query or f"open application named {programName} from deeply search" in query or f"launch app named {programName} from deep search" in query or f"run app named {programName} from deep search" in query or f"open app named {programName} from deep search" in query or f"open app named {programName} from deep searched" in query or f"launch app named {programName} from deep searched" in query or f"run app named {programName} from deep searched" in query or f"open app named {programName} from deeply searched" in query or f"launch app named {programName} from deeply searched" in query or f"run app named {programName} from deeply searched" in query or f"launch app named {programName} from deeply search" in query or f"run app named {programName} from deeply search" in query or f"open app named {programName} from deeply search" in query:
                    if openProgram('deepMode', programName):
                        printGUI(f"Launching {programName} from Deeply Searched application list")
                        print(
                            f">>> Launching {programName} from Deeply Searched application list")
                        speak(
                            f"Launching {programName} from Deeply Searched application list")
                        openProgram('deepMode', programName)
                    else:
                        printGUI("Program not found!")
                        speak("program not found!")

                else:
                    programName = query.replace('application from', '').replace(
                        'app from', '').replace('program from', '').replace('application from', '').replace(
                        'app from', '').replace('program from', '').replace('application from', '').replace(
                        'app from', '').replace('program from', '').replace('start menu', '')
                    if f"close {programName} app from" in query or f"close {programName} application from" in query or f"close {programName} program from" in query or f"kill {programName} app from" in query or f"kill {programName} application from" in query or f"kill {programName} program from" in query or f"stop {programName} app from" in query or f"stop {programName} application from" in query or f"stop {programName} program from" in query:
                        if closeProgram(programName):
                            printGUI(f"Closing {programName}")
                            print(f"Closing {programName}")
                            speak(f"Closing {programName}")
                            closeProgram(programName)
                        else:
                            printGUI("Program not found!")
                            print(">>> Program not found!")

                        # VS code launching
                    elif "open code" in query or "open vs code" in query:
                        printGUI("Launching VS code")
                        print(">>> launching VS code")
                        speak("launching v s code")
                        openProgram('pathMode',
                                    path(r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe"))
                    elif "start code" in query or "start vs code" in query:
                        printGUI("Launching VS code")
                        print(">>> launching VS code")
                        speak("launching v s code")
                        openProgram('pathMode',
                                    path(r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe"))
                    elif "run code" in query or "run vs code" in query:
                        printGUI("Launching VS code")
                        print(">>> launching VS code")
                        speak("launching v s code")
                        openProgram('pathMode',
                                    path(r"C:\Users\dell\AppData\Local\Programs\Microsoft VS Code\Code.exe"))
                        # VS code Closing
                    elif "close code" in query or "close vs code" in query:
                        printGUI("Closing VS code")
                        print(">>> Closing VS code")
                        speak("closing v s code")
                        closeProgram("Code.exe")
                    elif "stop code" in query or "stop vs code" in query:
                        printGUI("Closing VS code")
                        print(">>> Closing VS code")
                        speak("closing v s code")
                        closeProgram("Code.exe")
                    elif "exit code" in query or "exit vs code" in query:
                        printGUI("Closing VS code")
                        print(">>> Closing VS code")
                        speak("closing v s code")
                        closeProgram("Code.exe")

                        # Chrome launching
                    elif "open chrome" in query or "run chrome" in query or "start chrome" in query:
                        printGUI("Launching Chrome")
                        print(">>> launching Chrome")
                        speak("launching chrome")
                        openProgram('pathMode',
                                    path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
                        # Chrome Closing
                    elif "close chrome" in query or "stop chrome" in query or "exit chrome" in query:
                        printGUI("Closing Chrome")
                        print(">>> Closing Chrome")
                        speak("Closing chrome")
                        closeProgram("chrome.exe")

                        # Command Prompt launching
                    elif "open cmd" in query or "run cmd" in query or "start cmd" in query:
                        printGUI("Launching Command Prompt")
                        print(">>> launching Command Prompt")
                        speak("launching Command Prompt")
                        openProgram('pathMode',
                                    path(r"C:\WINDOWS\system32\cmd.exe"))
                    elif "open command prompt" in query or "run command prompt" in query or "start command prompt" in query:
                        printGUI("Launching Command Prompt")
                        print(">>> launching Command Prompt")
                        speak("launching Command Prompt")
                        openProgram('pathMode',
                                    path(r"C:\WINDOWS\system32\cmd.exe"))
                        # Command Prompt Closing
                    elif "close cmd" in query or "stop cmd" in query or "exit cmd" in query:
                        printGUI("Closing Command Prompt")
                        print(">>> Closing Command Prompt")
                        speak("Closing Command Prompt")
                        closeProgram("cmd.exe")
                    elif "close command prompt" in query or "stop command prompt" in query or "exit command prompt" in query:
                        printGUI("Closing Command Prompt")
                        print(">>> Closing Command Prompt")
                        speak("Closing Command Prompt")
                        closeProgram("cmd.exe")

                        # Anonymous Command Prompt launching
                    elif "open anonymous cmd" in query or "run anonymous cmd" in query or "start anonymous cmd" in query:
                        printGUI("Launching Anonymous Command Prompt")
                        print(">>> launching Anonymous Command Prompt")
                        speak("launching Anonymous Command Prompt")
                        openProgram('pathMode',
                                    path(r"G:\cmd1.bat"))
                        # Anonymous Command Prompt Closing
                    elif "close anonymous cmd" in query or "stop anonymous cmd" in query or "exit anonymous cmd" in query:
                        printGUI("Closing Anonymous Command Prompt")
                        print(">>> Closing Anonymous Command Prompt")
                        speak("Closing Anonymous Command Prompt")
                        closeProgram("cmd.exe")
                    elif "close anonymous command prompt" in query or "stop anonymous command prompt" in query or "exit anonymous command prompt" in query:
                        printGUI("Closing Anonymous Command Prompt")
                        print(">>> Closing Anonymous Command Prompt")
                        speak("Closing Anonymous Command Prompt")
                        closeProgram("cmd.exe")

                        """ Selenium related queries"""

                        # Digicamp for Vivek
                    elif "open digicamp for vivek" in query or "digicamp for vivek" in query or "login on digicamp for vivek" in query or "sign in on digicamp for vivek" in query or "login on digicamp as vivek" in query or "sign in on digicamp as vivek" in query:
                        try:
                            printGUI("Launching Digicamp for Vivek")
                            print(">>> launching Digicamp for Vivek")
                            speak("launching Digicamp for Vivek")
                            br = seleniumInitialisation('chrome')
                            # launching Digicamp website on chrome
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
                            br.find_element_by_xpath(
                                '//*[@id="txtCaptcha"]').click()

                            wait = WebDriverWait(br, 60)
                            wait.until(EC.title_is(
                                "ARMY PUBLIC SCHOOL KUNRAGHAT - APSKUN | ~ TotalES ~"))

                            br.find_element_by_xpath(
                                '//*[@id="nav"]/li[3]/a').click()
                            br.find_element_by_xpath(
                                '//*[@id="dtblStudentAssign"]/tbody/tr/td[7]/button[1]').click()

                            closeProgram("chromedriver.exe")
                        except:
                            print("\n   >>> closing webdriver\n")
                            closeProgram("chromedriver.exe")
                            print("   >>> webdriver closed\n")

                    else:
                        # Searching on YouTube
                        search = query.replace("search", " ")
                        search = search.replace("on youtube", " ")
                        search = search.strip()
                        if f"search {search} on youtube" in query or "on youtube" in query:
                            try:
                                searchKeyword = search.replace(" ", "+")
                                printGUI(caps(f"Searching {search} on YouTube"))
                                print(
                                    caps(f"   --- Searching {search} on YouTube"))
                                speak(f"searching {search} on youtube")
                                br = seleniumInitialisation('chrome')
                                br.get(
                                    f"https://www.youtube.in/results?search_query={searchKeyword}")

                                closeProgram("chromedriver.exe")
                            except:
                                print("\n   >>> closing webdriver\n")
                                closeProgram("chromedriver.exe")
                                print("   >>> webdriver closed\n")
                        else:
                            # Searching on Google
                            search = query.replace("search", " ")
                            search = search.replace("on google", " ")
                            search = search.strip()
                            if f"search {search} on google" in query or "on google" in query or f"what is {search}" in query:
                                try:
                                    searchKeyword = search.replace(" ", "+")
                                    printGUI(
                                        caps(f"Searching {search} on Google"))
                                    print(
                                        caps(f"   --- Searching {search} on Google"))
                                    speak(f"searching {search} on google")
                                    br = seleniumInitialisation('chrome')
                                    br.get(f"https://www.google.com/search?q=hello+world&oq=hello+world{search}")
                                    closeProgram("chromedriver.exe")
                                except:
                                    print("\n   >>> closing webdriver\n")
                                    closeProgram("chromedriver.exe")
                                    print("   >>> webdriver closed\n")

                                # Login on Facebook
                            elif "open facebook for" in query or "login on facebook" in query or "sign in on facebook" in query or "login on facebook" in query or "sign in on facebook" in query:
                                loginName = query.replace(
                                    "open facebook for", "")
                                loginName = loginName.replace(
                                    "login on facebook for", " ")
                                loginName = loginName.replace(
                                    "sign in on facebook for", " ")
                                loginName = loginName.replace(
                                    "login on facebook as", " ")
                                loginName = loginName.replace(
                                    "sign in on facebook as", " ")
                                loginName = loginName.strip()

                                userDataBase = ['shivam', 'anuradha', 'vivek']

                                # Login as Shivam
                                if "shivam" in loginName:
                                    try:
                                        printGUI("Login as Shivam on Facebook")
                                        print(
                                            "   --- Login as Shivam on Facebook")
                                        speak("Login as Shivam on Facebook")

                                        br = seleniumInitialisation('chrome')
                                        br.get("https://www.facebook.com/")

                                        userName = br.find_element_by_xpath(
                                            '//*[@id="email"]')
                                        userName.send_keys(7668356841)

                                        password = br.find_element_by_xpath(
                                            '//*[@id="pass"]')
                                        password.send_keys("Shivam.05")

                                        signUpButton = br.find_element_by_xpath(
                                            '//*[@id="u_0_b"]')
                                        signUpButton.click()

                                        closeProgram("chromedriver.exe")
                                    except:
                                        print("\n   >>> closing webdriver\n")
                                        closeProgram("chromedriver.exe")
                                        print("   >>> webdriver closed\n")

                                    # Login as Vivek
                                elif "vivek" in loginName:
                                    try:
                                        printGUI("Login as Vivek on Facebook")
                                        print(
                                            "   --- Login as Vivek on Facebook")
                                        speak("Login as Vivek on Facebook")
                                        br = seleniumInitialisation('chrome')
                                        br.get("https://www.facebook.com/")

                                        userName = br.find_element_by_xpath(
                                            '//*[@id="email"]')
                                        userName.send_keys(7269055756)

                                        password = br.find_element_by_xpath(
                                            '//*[@id="pass"]')
                                        password.send_keys("Vivek.05")

                                        signUpButton = br.find_element_by_xpath(
                                            '//*[@id="u_0_b"]')
                                        signUpButton.click()

                                        closeProgram("chromedriver.exe")
                                    except:
                                        print("\n   >>> closing webdriver\n")
                                        closeProgram("chromedriver.exe")
                                        print("   >>> webdriver closed\n")
                                elif not loginName in userDataBase:
                                    try:
                                        """ TODO: Make this work! """
                                        print(
                                            "    --- Enter your registered mobile number or email address")
                                        speak(
                                            "Enter your registered mobile number or email address")
                                        userNameValue = input("    --> ")
                                        print(
                                            "    --- Type your password")
                                        speak(
                                            "Type your password")
                                        userPasswordValue = input("    --> ")

                                        print(
                                            f"   --- Login as {loginName} on Facebook")
                                        speak(
                                            f"Login as {loginName} on Facebook")
                                        br = seleniumInitialisation('chrome')
                                        br.get("https://www.facebook.com/")

                                        userName = br.find_element_by_xpath(
                                            '//*[@id="email"]')
                                        userName.send_keys(userNameValue)

                                        password = br.find_element_by_xpath(
                                            '//*[@id="pass"]')
                                        password.send_keys(userPasswordValue)

                                        signUpButton = br.find_element_by_xpath(
                                            '//*[@id="u_0_b"]')
                                        signUpButton.click()

                                        closeProgram("chromedriver.exe")
                                    except:
                                        print("\n   >>> closing webdriver\n")
                                        closeProgram("chromedriver.exe")
                                        print("   >>> webdriver closed\n")

                                """ A.I controls """

                            elif "kill yourself" in query or "terminate yourself" in query or "shutdwon yourself" in query:  # Stops the A.I
                                eelStatus("Shutting down:")
                                print(">>> Shutting down\n")
                                speak("Terminating myself")
                                eel.exitWindow()
                                sys.exit()
                                
                            elif "hibernate yourself" in query or "go to sleep" in query:  # Puts the A.I to sleep
                                sleep = True
                                eelStatus("Sleep Mode:")
                                printGUI("To wake me up say:\nWake up Jarvis")
                                speak("wake me up whenever you need me!")
                            elif "don't disturb me" in query or "dont disturb me" in query:  # Puts the A.I to sleep
                                sleep = True
                                eelStatus("Sleep Mode: ")
                                
                                speak("as you wish boss")
        elif sleep == True:
            print(">>> In sleep mode\n")
            while sleep == True:
                query = voiceRecognition_SleepMode().lower()
                if "wake up" in query or "hey jarvis" in query:  # Wakes up the A.I
                    printGUI("Exiting Sleep mode")
                    eelStatus("Normal Mode:")
                    print(">>> Exiting Sleep mode\n")
                    speak("i'm online")
                    sleep = False
                elif "kill yourself" in query or "terminate yourself" in query:  # Stops the A.I
                    eelStatus("Shutting down:")
                    print(">>> Shutting down\n")
                    speak("Terminating myself")
                    eel.exitWindow()
                    sys.exit()
            

if __name__ == '__main__':
    eelThreadInitialization()
    if eel.guiIsStarted()() == 'True':
        main()
