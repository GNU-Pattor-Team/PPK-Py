#!/usr/bin/python3

# PPK (Pattor Packager)
# Copyright (C) 2020, GNU/Pattor Team
# <web>
# You should have received a copy of the GNU General Public License
# along with this program. If not, see https://www.gnu.org/licenses

import os
import time
import argparse

Index0Url = str("https://raw.githubusercontent.com/GNU-Pattor-Team/PPK-Sources-Main/master/main.index")
Index1Url = str("")

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--terms",
	help="(--terms [dummy]) - Shows the Terms of the program's license.")
ap.add_argument("-n", "--nofetch",
	help="(--nofetch true) - Skips ReFetching of sources lists.")
ap.add_argument("-l", "--list",
	help="(--list [package name]) - Lists the desired package(s).")
ap.add_argument("-a", "--about",
	help="(--about [package name]) - Shows info About the desired package(s).")
ap.add_argument("-d", "--download",
	help="(--download [package name]) - Downloads the desired package(s), without installing.")
ap.add_argument("-i", "--install",
	help="(--install [package name]) - Installs/Updates the desired package(s), downloading if necessary.")
ap.add_argument("-r", "--remove",
	help="(--remove [package name]) - Removes the desired package'(s) binaries, without touching the data.")
ap.add_argument("-p", "--purge",
	help="(--purge [package name]) - Fully Removes the desired package(s).")
args = ap.parse_args()

def printHelp():
	print("\n\033[95mPPK (Pattor Packager) | Copyright (C) 2020, GNU/Pattor Team\nThis program comes with ABSOLUTELY NO WARRANTY;\nThis is free software, and you are welcome to redistribute it\nunder certain conditions; type 'show t' for details.\n\033[0m")

def printTerms():
	print("\n\033[95mPPK (Pattor Packager) | A gateway to everything pirate on GNU/Linux.\nCopyright (C) 2020, GNU/Pattor Team\nRelies on DPKG and WGET to work.\n\n<web>\n\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License,\nor (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\nSee the GNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program. If not, see <https://www.gnu.org/licenses/>.\n\033[0m")

def printPattor():
	print("\n\033[95mPPK have the Pattor Super Powers\n\033[0m")

def search_string_in_file(text_file_name, string_to_search):
	current_index = 0
	line_number = 0
	list_of_results = []
	with open(text_file_name, "r") as read_obj:
		for line in read_obj:
			line_number += 1
			if string_to_search in line:
				list_of_results.append((line_number, line.rstrip()))
	return list_of_results

def ppkFetch():
	if (str(args.nofetch) != "true"):
		os.system("mkdir /opt/ppk/lists/ && mkdir /opt/ppk/packages/")
		print("\n\033[94mFetching latest sources index...\n\033[0m")
		time.sleep(1)
		os.system("wget -q --show-progress -O /opt/ppk/lists/main.index " + Index0Url)
		text_file_name = str("/opt/ppk/lists/main.index")
		line_number = 0
		with open(text_file_name) as f:
			for line in f:
				os.system("wget -q --show-progress -O /opt/ppk/lists/sources.index" + str(line_number) + " " + line)
				line_number += 1
		f.close()
		print("\n\033[94mDone fetching sources.\n\033[0m")

def ppkList():
	ppkFetch()
	matched_lines = search_string_in_file("/opt/ppk/lists/sources.index0", args.list)
	for elem in matched_lines:
		print("Line Number = ", elem[0], " :: Line = ", elem[1])

def ppkAbout():
	ppkFetch()

def ppkDownload():
	ppkFetch()

def ppkInstall():
	ppkFetch()
	ppkDownload()

def ppkRemove():
	os.system("dpkg --remove " + args.remove)

def ppkPurge():
	os.system("dpkg --purge " + args.purge)

if (os.getuid() != 0):
	print("\n\033[93m\033[1mNOTE: PPK must run with admin privileges.\nEither call it through sudo, or start it with the root user using su.\n\033[0m")
	exit()

if (str(args.terms) != "None"):
	printTerms()

if (str(args.list) != "None"):
	ppkList()

if (str(args.about) != "None"):
	ppkAbout()

if (str(args.download) != "None"):
	ppkDownload()

if (str(args.install) != "None"):
	ppkInstall()

if (str(args.remove) != "None"):
	ppkRemove()

if (str(args.purge) != "None"):
	ppkPurge()

print("\n\033[94mProgram finished.\n\033[0m")
