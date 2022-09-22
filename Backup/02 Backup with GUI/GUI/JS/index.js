/********************************* ©Copyright 2020 Shivam Shandilya *********************************/
console.warn("©Copyright 2020 Shivam Shandilya")
// This statement will start the brain of A.I when the GUI is loaded
function guiIsStarted(){
	return 'True'
}
eel.expose(guiIsStarted)

// This function will show the result on the <pre> tag
function output(result){
    var previsuResult = document.getElementById("result");
    previsuResult.innerHTML = result;
}
eel.expose(output);

// This function will update the status of the A.I 
function ai_status(status){
	var previusStatus = document.getElementById("ai-status");
	previusStatus.innerHTML = status;
}
eel.expose(ai_status)

// This function will close the GUI when the user terminates the A.I
function exitWindow(){
	window.close();
}
eel.expose(exitWindow)