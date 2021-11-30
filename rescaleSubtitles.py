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

scaler=1.2
# --------- Gourmet Night
# sourcepath="G:\\Files\\Movies\\Series\\Fawlty Towers\\Fawlty Towers - Gourmet Night.divx_old.sub"
# destpath="G:\\Files\\Movies\\Series\\Fawlty Towers\\Fawlty Towers - Gourmet Night.sub"
# --------- The Hotel Inspectors
# sourcepath="G:\\Files\\Movies\\Series\\Fawlty Towers\\Fawlty Towers - 1.04 - The Hotel Inspectors.eng.sub"
# destpath="G:\\Files\\Movies\\Series\\Fawlty Towers\\Fawlty Towers - 1.04 - The Hotel Inspectors.sub"
# --------- The Germans
sourcepath="G:\\Files\\Movies\\Series\\Fawlty Towers\\Fawlty Towers - 1.06 - The Germans.eng.sub"
destpath="G:\\Files\\Movies\\Series\\Fawlty Towers\\Fawlty Towers - The Germans.sub"



srcFile=open(sourcepath)
desFile=file(destpath,"w")

linecount=0
try:
    for line in srcFile:
        linecount+=1
        #print (filterSubString(line))
        newLine=filterSubString(line)
        newLine[0]=str(int(int(newLine[0])*scaler))
        newLine[1]=str(int(int(newLine[1])*scaler))
        #print(newLine)
        desFile.write("{"+newLine[0]+"}{"+newLine[1]+"}"+newLine[2])
        
finally:
    srcFile.close()
    desFile.close()

print(linecount)