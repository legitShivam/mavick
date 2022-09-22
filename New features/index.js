// © Copyright 2020 Shivam Shandilya
// This JavaScript is linked to 'index.html' and to the python script.
// This file will execute the GUI related commands.


// This statement will start the brain of A.I when the GUI is loaded
function guiIsStarted(){
	return 'True'
}

// This function will show the result on the <pre> tag
var previsuOutputValue
function output(result){
    var previsuResult = document.getElementById("result")
   	if(previsuResult.innerHTML == 'Booting the brain! Please wait.'){
   		window.previsuOutputValue = ''
   	}
   	else{
    window.previsuOutputValue = previsuResult.innerHTML + '\n'}
    previsuResult.innerHTML = result
}

// This function will return the result value to 'voiceRecognition()' function in python script
function getOutputValue(){
	return previsuOutputValue
} 

// This create music controler in div with id: 'resultContainer'
function musicControl(control){
    var previsuResult = document.getElementById("resultContainer")
    previsuResult.innerHTML = control
}

// This function will update the status of the A.I 
function ai_status(status){
	var previusStatus = document.getElementById("ai-status")
	previusStatus.innerHTML = status
}

// This function will close the GUI when the user terminates the A.I
function exitWindow(){
	window.close()
}

playValue = 'True'  // To play/pause music
stopValue = 'False' // To stop the music

isPlayButtonClicked = true
isPauseButtonClicked = false
isStopButtonClicked = false

// This function will set the play value to 'True', sets the src of clicked image to ...hover.png and other images to ...Button.png
function playFunction(){
	eel.resumeViaEelConnection()
	window.playValue = 'True'
	window.isPlayButtonClicked = true
	window.isPauseButtonClicked = false
	window.isStopButtonClicked = false
	document.getElementById("playButton").src = "Resources/images/playButtonHover.png"
	document.getElementById("pauseButton").src = "Resources/images/pauseButton.png"
	document.getElementById("stopButton").src = "Resources/images/stopButton.png"

}

// This function will set the play value to 'False', sets the src of clicked image to ...hover.png and other images to ...Button.png, sets the is...ButtonClicked value to true so that onmouseout does'nt apply if the button is clicked.
function pauseFunction(){
	eel.pauseViaEelConnection()
	window.playValue = 'False'
	window.isPauseButtonClicked = true
	window.isPlayButtonClicked = false
	window.isStopButtonClicked = false
	document.getElementById("pauseButton").src = "Resources/images/pauseButtonHover.png"
	document.getElementById("playButton").src = "Resources/images/playButton.png"
	document.getElementById("stopButton").src = "Resources/images/stopButton.png"
}

// This function will set the play value to 'False', sets the src of clicked image to ...hover.png and other images to ...Button.png, sets the is...ButtonClicked value to true so that onmouseout does'nt apply if the button is clicked.
function stopFunction(){
	eel.stopViaEelConnection()
	window.stopValue = 'True'
	window.isStopButtonClicked = true
	window.isPlayButtonClicked = false
	window.isPauseButtonClicked = false
	document.getElementById("stopButton").src = "Resources/images/stopButtonHover.png"
	document.getElementById("playButton").src = "Resources/images/playButton.png"
	document.getElementById("pauseButton").src = "Resources/images/pauseButton.png"
}

// This function will reset the music controler presets 
function resetMusicControler(){
	window.playValue = 'True'
	window.stopValue = 'False'
	window.isPlayButtonClicked = true
	window.isPauseButtonClicked = false
	window.isStopButtonClicked = false
}

// This function will tell python about status of play/pause
function playStatus(){
	return playValue
}

// This function will tell the python to stop the music
function stopStatus(){
	return stopValue
}


// These two funtion's will apply hover effect to playButton
function playButtonOnHover(){
	document.getElementById("playButton").src = "Resources/images/playButtonHover.png"
}
function playButtonOnHoverOut(){
	if(! isPlayButtonClicked){
	document.getElementById("playButton").src = "Resources/images/playButton.png"}
}

// These two funtion's will apply hover effect to pauseButton
function pauseButtonOnHover(){
	document.getElementById("pauseButton").src = "Resources/images/pauseButtonHover.png"
}
function pauseButtonOnHoverOut(){
	if(! isPauseButtonClicked){
	document.getElementById("pauseButton").src = "Resources/images/pauseButton.png"}
}

// These two funtion's will apply hover effect to stopButton
function stopButtonOnHover(){
	document.getElementById("stopButton").src = "Resources/images/stopButtonHover.png"
}
function stopButtonOnHoverOut(){
	if(! isStopButtonClicked){
	document.getElementById("stopButton").src = "Resources/images/stopButton.png"}
}


// Exposing JavaScript function to python with the help of eel

eel.expose(guiIsStarted)	   // To signal the python script that GUI is started
eel.expose(output)	           // To fetch the output from python script and show it on the HTML page
eel.expose(musicControl)       // To intiate music controler
eel.expose(resetMusicControler)// To reset the music controler
eel.expose(getOutputValue)     // To get the value of printGUI for voiceRecognition function in python
eel.expose(ai_status)          // To update the status of ai on the GUI
eel.expose(exitWindow)         // To exit the HTML page(GUI) when the python script is terminated by the user
eel.expose(playStatus)         // To check whether the user have pressed the play button.
eel.expose(stopStatus)         // To check whether the user have pressed the stop button.
