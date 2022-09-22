import pygame
import random
import os 
import datetime
import threading
import shutil
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import easygui
from functions import *

currentWorkingDirectory = os.getcwd()


class Settings():
	def settingsInitializtion():
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

	def songsFolderPath():
		print('yes 1')
		os.chdir('data')
		os.chdir('songs')
		with open('song.list') as file:
			fileContent = file.read()
		if fileContent == '':
			songPath = getFolderPath("Choose a Song Folder")
			with open('song.list', 'w') as file:
				file.write(songPath)
				print('done')
			os.chdir(currentWorkingDirectory)
			return songPath
		else:
			with open('song.list', 'w') as file:
				file.write(songPath)
				print('done')
			os.chdir(currentWorkingDirectory)
			return songPath

class AudioPlayer():

	def play(path):
		try:
			pygame.mixer.init()
			pygame.mixer.music.load(path)
			pygame.mixer.music.play()
			print('Playing')
		except:
			print("Unable to play song right now! try again later.")
			eelStatus("Stream is preoccupied!")
			printGUI("Unable to play song right now! try again later.")
			speak("Unable to play song right now! try again later.")
	


	def stop():
		pygame.mixer.music.stop()
		pygame.quit()
		print('stopping')
	

	def pause():
		print('Success')
		try:
			pygame.mixer.music.pause()
		except:
			pass

	def resume():
		try:
			pygame.mixer.music.unpause()
		except:
			pass


class inputOperations():
	def getFolderPath(titleOfWindow):
		"""
		Fires a GUI Window to get path of the folder

		ARGUMENTS:
		>>> titleOfWindow: sets the title of the window


		"""
		folderPath = easygui.diropenbox(titleOfWindow)  # easygui is a Tkinter based libaray for dialog boxes
		return folderPath



@eel.expose
def resumeViaEelConnection():
	print('yo')
	AudioPlayer.resume()


@eel.expose
def pauseViaEelConnection():
	print('yo 2')
	AudioPlayer.pause()


@eel.expose
def stopViaEelConnection():
	print('yo 3')
	AudioPlayer.stop()
	createMusicControler.isSongStopped = True




def getFolderPath(titleOfWindow):
	"""
	Fires a GUI Window to get path of the folder

	ARGUMENTS:
	>>> titleOfWindow: sets the title of the window


	"""
	folderPath = easygui.diropenbox(titleOfWindow)
	return folderPath


def songListGenerator():
	songsFolderPath = Settings.songsFolderPath()
	songs = {}
	print(songsFolderPath)
	for root, dirs, files in os.walk(songsFolderPath):
		for dir in dirs:
			for file in files :
				path = root+'/'+file
				if file.lower().endswith('.mp3'):
					songs.update({file: path})
	return songs

isSongPlaying = False

class PlaySong():
	"""
	This class will play the song in different mode:

	>>> radomSong does'nt take argument
	>>> choosedSong take the name or some part of the audio/song.

	"""
	def randomSongInInternalAudioPlayer():
		"""
		Plays random song in internal player

		"""
		global isSongPlaying
		songList = songListGenerator()
		songName = random.choice(list(songList))
		songPath = songList[songName]
		print(f"Playing {songName}")
		eelStatus("Playing Music ♪")
		AudioPlayer.play(songPath)
		isSongPlaying = True
		return caps(songName.replace('.mp3', ''))

	def randomSongInExternalAudioPlayer():
		"""
		Plays random song in external player

		"""
		global isSongPlaying
		songList = songListGenerator()
		songName = random.choice(list(songList))
		songPath = songList[songName]
		print(f"Playing {songName}")
		eelStatus("Playing Music ♪")
		os.startfile(songPath)
		isSongPlaying = True
		return caps(songName.replace('.mp3', ''))


	def choosedSongInInternalAudioPlayer(songName):
		"""
		Plays choosed song in internal player

		"""
		songList = songListGenerator()
		global isSongPlaying
		for song in list(songList):
			if songName.lower().strip() in song.lower():
				songPath = songList[song]
				print(f"Playing {songName}")
				eelStatus("Playing Music ♪")
				AudioPlayer.play(songPath)
				isSongPlaying = True
				return caps(song.replace('.mp3', ''))
		printGUI('Music not found!')
		print("not found")

	def choosedSongInExternalAudioPlayer(songName):
		"""
		Plays choosed song in external player

		"""
		songList = songListGenerator()
		global isSongPlaying
		for song in list(songList):
			if songName.lower().strip() in song.lower():
				songPath = songList[song]
				print(f"Playing {songName}")
				eelStatus("Playing Music ♪")
				isSongPlaying = True
				return caps(song.replace('.mp3', ''))
		print("not found")

def createMusicControler(songName):
	if isSongPlaying:
		eel.musicControl(f'<div style="padding: 10px; margin-top: -20px; margin-bottom: 5px;"><pre style="color: white; padding-top: 12px; padding-left: 10px; padding-right: 15px; margin-top: 10px">♪ {songName}</pre> <center><img src="Resources/images/playButtonHover.png" alt="playButton" style="margin-top: 5px; margin-bottom: 5px;" width="30" height="30" onclick="playFunction()" id="playButton" onmouseover ="playButtonOnHover()" onmouseout="playButtonOnHoverOut()"> <img src="Resources/images/pauseButton.png" alt="pauseButton" style="margin-left: 10px; margin-top: 5px; margin-bottom: 5px;" width="30" height="30" onclick="pauseFunction()" id="pauseButton" onmouseover ="pauseButtonOnHover()" onmouseout="pauseButtonOnHoverOut()"> <img src="Resources/images/stopButton.png" alt="stopButton" style="margin-left: 10px; margin-top: 5px; margin-bottom: 5px;" width="30" height="30" onclick="stopFunction()" id="stopButton" onmouseover ="stopButtonOnHover()" onmouseout="stopButtonOnHoverOut()"></center></div>')
		createMusicControler.isSongStopped = False
		while not createMusicControler.isSongStopped:
			eel.sleep(0.1) # Lowers the CPU load
		eel.musicControl(f'<pre id="result">Music stopped!</pre>')
		eel.resetMusicControler()
			




if __name__ == '__main__':
	eelThread = threading.Thread(target=eelStart)
	eelThread.start()
	Settings.settingsInitializtion()
	while True:
		createMusicControler(PlaySong.randomSongInInternalAudioPlayer())
		eel.sleep(5)
	
