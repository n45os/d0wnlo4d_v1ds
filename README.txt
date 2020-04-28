READ ME

developer: n45os

this file can run if you have python installed on your computer. If you do, this code will be able to run on your macOS or Linux OS for sure. 

1. open your terminal and follow the path that you have the file downloaded (or you can simply drag the file into the terminal). if you are not that experienced with terminal, add the file on your desktop and type this command into the terminal:

	cd desktop/download

2.run this command to install the libraries needed.

	pip install -r requirements.txt

3.when it's done, you have to edit the file. 

	-Enter the path that you want the videos to be saved changing the "download_path" variable's string with your path
	-save the file and close it

4.run the python file. when on the directory (will already be there) run this command:
	
	python3 downloadVids.py

5. now the code is running. follow the steps, add the links and the file name and when you are done type "x" in the url place


IN CASE OF AN ERROR:
	some video hosting sites change its links dynamically which means that you may experience a problem especially if you have a slow internet connection or you want to download many files. in this case you have to edit again the file but change the "after_video" variable to the video the problem occurred. 

This pyhton code is meant to be used only on sites that the content is free and there are no copyrighted videos. 

Happy downloading, n45os®