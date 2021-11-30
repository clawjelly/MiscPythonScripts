# -----------------------
# subtitle scaler
# -----------------------
# rescales subtitles
# in the .sub format
# by a given size
# -----------------------

import os, sys

def filterSubString(substring):
    # filters string and returns parts
    tempString=substring.split("}")
    resultString=[]
    for x in tempString:
        x=x.replace("{","")
        x=x.replace("}","")
        resultString.append(x)
    return resultString

def getSecondsFromSRT(srtime):
	# extracts the seconds
	srtimeItems=srtime.replace(",",":").split(":")
	time=float(srtimeItems[0])*3600+float(srtimeItems[1])*60+float(srtimeItems[2])+float(srtimeItems[3])/1000
	return time
	
def generateSRTTimeCode(secs):
	tempsecs=divmod(secs,3600)
	hours=str(int(tempsecs[0])).zfill(2)
	tempsecs=divmod(tempsecs[1],60)
	minutes=str(int(tempsecs[0])).zfill(2)
	seconds=str(int(tempsecs[1])).zfill(2)
	hundreds=str(int((tempsecs[1]-int(tempsecs[1]))*1000)).zfill(3)
	timecode=hours+":"+minutes+":"+seconds+","+hundreds
	return timecode

class subtitleItem:
	"All Internet Comic related Attributes needed to create a proper link"
	start = 0		# time in seconds
	end = 0 		# time in seconds
	text = ""
	
# --------- Chinese Ghost Story 1
# sourcepath="Z:\Shared Videos\Full Movies\A.Chinese Ghost Story I 1987 mHD - Source.srt"
# destpath="Z:\Shared Videos\Full Movies\A.Chinese Ghost Story I 1987 mHD.srt"
# scaler=1.0465
# offset=0
# --------- Chinese Ghost Story 2
sourcepath="Z:\Shared Videos\Full Movies\A Chinese Ghost Story II 1990 mHD - Source.srt"
destpath="Z:\Shared Videos\Full Movies\A Chinese Ghost Story II 1990 mHD.srt"
scaler=1.0431
offset=19

srcFile=open(sourcepath)
desFile=file(destpath,"w")

try:
	while True:
		activeItem=int(srcFile.readline()) # get first item
		# subtitles.append(subtitleItem()) # generate new item
		templine=srcFile.readline() # get time
		start=getSecondsFromSRT(templine.split(" --> ")[0])*scaler+offset
		end=getSecondsFromSRT(templine.split(" --> ")[1])*scaler+offset
		templine=srcFile.readline()
		subtext=""
		while templine!="\n":
			subtext+=templine
			templine=srcFile.readline()
		# --- now write
		desFile.write(str(activeItem)+"\n")
		desFile.write(generateSRTTimeCode(start)+" --> "+generateSRTTimeCode(end)+"\n")
		desFile.write(subtext)
		desFile.write("\n")
	
finally:
    srcFile.close()
    desFile.close()

print(linecount)