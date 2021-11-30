import string
import sys
import os
import shutil

if (len(sys.argv)>1):
	if (os.path.isdir(sys.argv[1])):
		# htmlFile=open(sys.argv[1]+os.path.basename(sys.argv[1]+".htm")
		# with open(sys.argv[1]+os.path.basename(sys.argv[1]+".htm","w") as htmlFile:
		filelist=os.listdir(sys.argv[1])
		
		# create img html
		htmlList=["<html><head><title>"+os.path.basename(sys.argv[1])+" - created with Oli's Image Script!</title></head>\n"]
		htmlList.append("<body>\n")
		for x in filelist:
			if (os.path.isdir(sys.argv[1]+"\\"+x)):
				subFileList=os.listdir(sys.argv[1]+"\\"+x)
				for y in subFileList:
					if string.find(y,".jpg")!=-1:
						if string.find(y," ")!=-1:
							os.rename(sys.argv[1]+"\\"+x+"\\"+y,sys.argv[1]+"\\"+x+"\\"+string.replace(y," ","_")) #rename file if whitespace is found!
							y=string.replace(y," ","_")
						htmlList.append("<img src=file:///"+sys.argv[1]+"\\"+x+"\\"+y+">"+x+"<br>\n")
			
		htmlList.append("</body></html>")
				
		# write the file
		htmlFile=open(sys.argv[1]+"//"+os.path.basename(sys.argv[1])+".htm","w")
		htmlFile.writelines(htmlList)
		htmlFile.close