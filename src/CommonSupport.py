﻿#!/usr/bin/python
# encoding: utf-8
#
#   Copyright (C) 2011-2023
#
#   In case of reuse of this source code please do not remove this copyright.
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	For more information on the GNU General Public License see:
#	<http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import
import os
import re
from enigma import eServiceReference
from .VlcPluginInterface import vlcFil
from .EMCTasker import emcDebugOut


#------------------------------------------------------------------------------------
# Common variables and methods imported/moved from different scripts in this projects
# to avoid cross referencing
#------------------------------------------------------------------------------------


global extAudio, extDvd, extVideo, extPlaylist, extList, extMedia, extBlu
global plyDVB, plyM2TS, plyDVD, plyMP3, plyVLC, plyAll
global sidDVB, sidDVD, sidMP3

# Set definitions (imported from MovieCenter.py)

# Media types
extAudio = frozenset([".ac3", ".dts", ".flac", ".m4a", ".mp2", ".mp3", ".ogg", ".wav", ".wma", ".aac"])
extVideo = frozenset([".ts", ".trp", ".avi", ".divx", ".f4v", ".flv", ".img", ".ifo", ".iso", ".m2ts", ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".mpg", ".mts", ".vob", ".wmv", ".bdmv", ".asf", ".stream", ".webm"])
extPlaylist = frozenset([".m3u", ".e2pls"])#, ".pls"])
extMedia = extAudio | extVideo | extPlaylist
extDir = frozenset([""])
extList = extMedia | extDir

# Additional file types
extTS = frozenset([".ts", ".trp"])
extM2ts = frozenset([".m2ts"])
#extDvd      = frozenset([".iso", ".img", ".ifo"])
extIfo = frozenset([".ifo"])
extIso = frozenset([".iso", ".img"])
extDvd = extIfo | extIso
extVLC = frozenset([vlcFil])
extBlu = frozenset([".bdmv"])
# blue disk movie
# mimetype("video/x-bluray") ext (".bdmv")

# Player types
plyDVB = extTS											# ServiceDVB
plyM2TS = extM2ts										# ServiceM2TS
plyDVD = extDvd											# ServiceDVD
plyMP3 = extMedia - plyDVB - plyM2TS - plyDVD - extBlu	# ServiceMP3 GStreamer
plyVideo = extMedia - extAudio
plyVLC = extVLC											# VLC Plugin
#plyBLU      = extBlu | extIso							# BludiscPlayer Plugin
plyAll = plyDVB | plyM2TS | plyDVD | plyMP3 | plyVLC | extBlu


# Type definitions

# Service ID types for E2 service identification
sidDVB = eServiceReference.idDVB						# eServiceFactoryDVB::id   enum { id = 0x1 };
sidDVD = 4369 											# eServiceFactoryDVD::id   enum { id = 0x1111 };
sidMP3 = 4097											# eServiceFactoryMP3::id   enum { id = 0x1001 };
# For later purpose
sidM2TS = 3 											# eServiceFactoryM2TS::id  enum { id = 0x3 };
#TODO
#sidXINE = 4112											# eServiceFactoryXine::id  enum { id = 0x1010 };

# Grouped service ids
sidsCuts = frozenset([sidDVB, sidDVD])


## getInfoFile (imported from MetaSupport.py)
def getInfoFile(path, exts=""):
	fpath = p1 = p2 = p3 = ""
	name, ext = os.path.splitext(path)
	ext = ext.lower()

	if os.path.isfile(path) and ext in extMedia:			#files & movie structures
		dir = os.path.dirname(path)
		p1 = name						# filename.ext
		p2 = os.path.join(dir, os.path.basename(dir))		# folder.ext if no filename.ext

	elif os.path.isdir(path):
		if path.lower().endswith("/bdmv"):			# bluray structures
			dir = path[:-5]
			if dir.lower().endswith("/brd"):
				dir = dir[:-4]
		elif path.lower().endswith("video_ts"):			# DVD structures
			dir = path[:-9]
			if dir.lower().endswith("/dvd"):
				dir = dir[:-4]
		else:							# folders
			dir = path
			p2 = os.path.join(dir, "folder")		# "folder.ext"

		prtdir, dirname = os.path.split(dir)
		p1 = os.path.join(dir, dirname)				# /dir/dirname.ext
		p3 = os.path.join(prtdir, dirname)			# /prtdir/dirname.ext, show AMS-files

	pathes = [p1, p2, p3]
	for p in pathes:
		for ext in exts:
			fpath = p + ext
			if os.path.exists(fpath):
				break
		if os.path.exists(fpath):
			break
	return (p1, fpath)


## getMetaTitleFromDescription (imported from MetaSupport.py)
def getMetaTitleFromDescription(desc):
	#TODO make it better and --> for example get the right title from other meta like "title only"
	title = ""
	try:
		x1 = len(desc.split(',', -1)) - 1
		x2 = x1 - 1
		title = desc.replace(desc.split(',', -1)[x1], '').replace(desc.split(',', -1)[x2], '').replace(',,', '')
		if title == ",":
			if re.match('(\w+(?:/\w+|)(?:/\w+|)(?:/\w+|)(?:/\w+|)\s\d{4})', desc.rsplit(',', 1)[1].strip(), re.S):
				title = ''
			else:
				if len(desc) > 50:
					title = desc[:47] + "..."
				else:
					title = desc
		elif (len(title) >= 50) or (len(title) < 3):
			if len(desc) > 50:
				title = desc[:47] + "..."
			else:
				title = desc
	except Exception as e:
		emcDebugOut("[EMC] getMetaTitle failed !!!\n" + str(e))
	return title					


## readPlaylist (imported from EMCPlayList.py)
def readPlaylist(path):
	if path:
		overview = []
		plist = open(path, "r")
		if os.path.splitext(path)[1] == ".e2pls":
			while True:
				service = plist.readline()
				if service == "":
					break
				service = service.replace('\n', '')
				spos = service.find('/')
				servicepath = service[spos:]
				service = servicepath.split('/')[-1]
				name = service + "\n"
				overview.append(name)
		return overview
	