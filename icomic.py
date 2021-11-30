#	Internet Comic Collector Script V 0.1
#	(C) Oliver Reischl
#	Creates a HTML-document with several linked online comics
#

import urllib
import string
import os
import datetime

class icomicClass:
	"All Internet Comic related Attributes needed to create a proper link"
	name = ""		# Comic page Name
	mainURL = ""		# Comic page URL
	indentifier = ""	# Identifier string for the comic URL
	addstring   = ""	# String to where the comicURL has to be added
	imageFormat = ""	# Image format ending... needed for iden<tifieng comic URL end.
	comicURLPrivate = ""	# cache-definition of the comic-URL (so it won't load everytime it is checked on runtime
	
	def comicURL(self):										# Retrieves relative URL from Website
		if self.mainURL and self.identifier and self.imageFormat: 				# Checks if all necessarities are defined
			if not self.comicURLPrivate:							# Checks, if already run through
				handle = urllib.urlopen(self.mainURL)					# Opens URL
				content = handle.read()							# Reads content
				startPosition = string.find(content, self.identifier)			# Searches identifier string
				print (self.name, startPosition)
				endPosition = string.find(content, self.imageFormat, startPosition)	# Searches end of comic-URL
				print (self.name, endPosition)
				comic = content[startPosition: endPosition+3]				# Creates URL-string
				print (self.name, comic)
				self.comicURLPrivate = comic						# Stores it (for later retrival)
			else:
				print("Stored comic URL:"+self.comicURLPrivate)
			return self.comicURLPrivate							# Return it
		else:
			return None								# Ooops... some definition lacking...

def createGarfieldImg():
	datumSTR=datetime.date.today()
	datum=str(datumSTR)
	url="ga"+datum[2:4]+datum[5:7]+datum[8:10]+".gif"
	print("Garfield Img URL:"+url)
	return url

def createTempHTMLFile(*args):

	htmlfile = open("temp.htm","w") 								# open head
	htmlfile.write("<html><head><title>Comic Page! ")  # create head
	htmlfile.write("(created from Internet Comic Collector ")
	htmlfile.write("Script by Oliver Reischl)</title></head><body>")
	htmlfile.write("<table><tr>")
	htmlfile.write("<td><a href='http://weatherpixie.com/' target='_blank'><img src='http://weatherpixie.com/displayimg.php?place=LOWW&trooper=1&type=' width=124 height=175 border=0 alt='The WeatherPixie'></a></td>")
	htmlfile.write("<td><a href='http://weatherpixie.com/' target='_blank'><img src='http://weatherpixie.com/displayimg.php?place=SBRJ&trooper=47&type=C' width=124 height=175 border=0 alt='The WeatherPixie'></a></td>")
	htmlfile.write("</tr><tr><td>Vienna, Austria</td><td>Rio de Janeiro, Brazil</td></tr></table>")
	
	for x in args:											# creating html-code for one instance
		htmlfile.write("<h1><a href="+x.mainURL+">"+x.name+"</a><br></h1>") 			# html link line
		htmlfile.write("<img src="+x.addstring+x.comicURL()+"></img><br><br>") 			# html image line
	
	htmlfile.write("</body></html>")								# finish with closing tags
	htmlfile.close
	# ... and close the file. Voila!

# Sinfest definitions

sinfest = icomicClass()
sinfest.name = "Sinfest"
sinfest.mainURL = "http://sinfest.net"
sinfest.identifier = "/comikaze/comics"
sinfest.addstring = "http://www.sinfest.net"
sinfest.imageFormat = "gif"

# http://sinfest.net/comikaze/comics/2008-01-04.gif
# http://www.sinfest.netomikaze/comics/2008-01-04.gif

# Penny Arcade definitions

penny = icomicClass()
penny.name = "Penny Arcade"
penny.mainURL = "http://www.penny-arcade.com/view.php3"
penny.identifier = "images/2008/"
penny.addstring = "http://www.penny-arcade.com/"
penny.imageFormat = "jpg"

# Garfield definitions

garfield = icomicClass()
garfield.name = "Garfield"
garfield.mainURL = "http://garfield.ucomics.com/"
garfield.identifier = "http://images.ucomics.com/comics/ga/2008/"
garfield.addstring = ""
garfield.imageFormat = "gif"
garfield.comicURLPrivate=garfield.identifier+(createGarfieldImg())

# Calvin and Hobbes definitions

calvin = icomicClass()
calvin.name = "Calvin and Hobbes"
calvin.mainURL = "http://www.ucomics.com/calvinandhobbes/"
calvin.identifier = "http://images.ucomics.com/comics/ch"
calvin.addstring = ""
calvin.imageFormat = "gif"

# Creat HTML-File ;-)

print(garfield.comicURL)	
createTempHTMLFile(penny,garfield,sinfest,calvin)
os.startfile("temp.htm")
