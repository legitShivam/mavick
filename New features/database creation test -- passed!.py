import os 
import datetime
import threading
import shutil
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

def dataManipulation():
	if os.path.exists('data'):
		os.chdir('data')
		if os.path.exists('songs'):
			os.chdir('songs')
			with open('readme.md', 'a') as file:
				file.write(f'This file was created at {datetime.datetime.now().strftime("%I:%M")}\n')
		else:
			os.mkdir('songs')
	else:
		os.mkdir('data')
		os.chdir('data')
		os.mkdir('songs')

def getFolderPath():
	import easygui
	folderPath = easygui.diropenbox()
	return folderPath

if __name__ == '__main__':

	dataManipulation()
	var = os.getcwd()
	print(var)
	songsFolderPath = getFolderPath()
	with open(r'data\songs\path.data','a') as file:
		file.write(f'{songsFolderPath}')