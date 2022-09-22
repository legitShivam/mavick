import eel
import threading

eel.init('GUI')

def func():
	eel.start("index.html", size=(700,600), mode='electron')

def eelInitialization():
	thread_1 = threading.Thread(target=func)
	thread_1.start()

eelInitialization()


