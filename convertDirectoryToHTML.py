import os, sys
from pathlib import Path

from docopt import docopt

__version__=0.1
__doc__="""
Convert Directory To HTML

by Oliver Reischl 2021

Greates a quick 

Usage:
  convertDirectoryToHTML (-h | --help)
  convertDirectoryToHTML <sourcepath>

Options:
-h, --help          Show this help.
-v, --version       Show program's version number
"""

def sizeof_fmt(num, suffix='Byte'):
		for unit in ['','Ki','M','Gi','Ti','Pi','Ei','Zi']:
				if abs(num) < 1024.0:
						return "%3.1f %s%s" % (num, unit, suffix)
				num /= 1024.0
		return "%.1f %s%s" % (num, 'Yi', suffix)

def convertDirectoryToHTML(*args):

	img_types=[".png",".jpg",".gif"]
	vid_types=[".mp4"]

	htmldirs=[Path(x) for x in args]
	srcpath=htmldirs[0]
	htmlfilepath=htmldirs[0]/"index.htm"

	# print(len(sys.argv))
	# print(sys.argv)
	# if (len(sys.argv)>1):
		# htmldirs=Path(sys.argv[1])

	width=320
	height=240

	head="""
	<html>
	<head>
	<style>
	</style>
	</head>
	<body>
	<style>

		.center {
			display: block;
			margin-left: auto;
			margin-right: auto;
			width: 50%;
		}

		h1 {
			font: 26px Verdana, sans-serif, black;
			float: none;
		}

		div.headline
		{
			margin-top: 50px;
		}

		p.gallery {
			margin: 50px;
			position:  relative;
			float: none;
			clear: both;
		}

		div.gallery {
			margin: 5px;
			border: 1px solid #ccc;
			float: left;
		}

		div.gallery_end{
			clear:  both;
		}

		div.gallery:hover {
			border: 1px solid #777;
		}

		div.gallery img {
			max-height: 200px;
			width: auto;
		}

		div.gallery video {
			max-height: 200px;
			width: auto;
		}

		div.desc {
			padding: 15px;
			font: 15px Verdana, sans-serif;
			text-align: center;
		}
	</style>
	</head>
	<body>
	"""

	imgcode="""
	<div class="gallery">
		<a target="_blank" href="{0}">
			<img src="{0}" width="{2}" height="{3}" class="center">
		</a>
		<div class="desc">{1}</div>
	</div>
	"""
	vidcode="""
	<div class="gallery">
		<video width="{2}" height="{3}" controls>
			<source src="{0}" type="video/mp4">
			Your browser does not support the video tag.
		</video>
		<a target="_blank" href="{0}">
			<div class="desc">{1}</div>
		</a>
	</div>
	"""
	with open(htmlfilepath, "w") as htmlfile:
		htmlfile.write(head)
		while htmldirs:
			currDir=htmldirs.pop()

			# collect files
			dirItems=dict()
			for e in currDir.iterdir():
				if e.is_dir():
					htmldirs.append(e)
				if e.is_file():
					if e.suffix in img_types:
						e=e.rename(e.parent / e.name.replace(" ", "_"))
						dirItems[e]=imgcode.format(str(e.relative_to(srcpath).as_posix()), e.name, 400, 400)
						# htmlfile.write(imgcode.format(str(e.relative_to(srcpath).as_posix()), e.name, 400, 400))
					if e.suffix in vid_types:
						e=e.rename(e.parent / e.name.replace(" ", "_"))
						filesize=sizeof_fmt(e.stat().st_size)
						dirItems[e]=vidcode.format(str(e.relative_to(srcpath).as_posix()), f"{e.name}: {filesize}", 400, 400)
						# htmlfile.write(vidcode.format(str(e.relative_to(srcpath).as_posix()), f"{e.name}: {filesize}", 400, 400))

			# write html
			if len(dirItems)>0:
				htmlfile.write(f"<p><div><h1>{currDir.relative_to(srcpath)}</h1></div>\n")
				for e, e_html in dirItems.items():
					htmlfile.write(e_html)
				htmlfile.write("<div class=\"gallery_end\"></div>\n</p>\n")
		htmlfile.write("</body></html>")

	return htmlfilepath


if __name__ == '__main__':
	# print(main(r"H:\Files\Images\Pixel\Turrican"))
	args=docopt(__doc__, version=__version__)
	if args["<sourcepath>"]:
		convertDirectoryToHTML(args["<sourcepath>"])
