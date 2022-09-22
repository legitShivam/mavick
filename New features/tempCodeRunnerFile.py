import os 

currentWorkingDirectory = os.getcwd()
for root, dirs, files in os.walk(r'E:\Music\lrc'):
	print(files)
	if files == []:
		print('done')
	else:
	    for file in files:
	        if file.lower().endswith('.mp3') or file.lower().endswith('.wav'):
	            print('checked')
	            break
	    else:
	    	print('not done')
print(root)