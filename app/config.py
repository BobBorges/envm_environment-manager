"""
File contains various config options. No edit.
"""

import os, json

try:
	user_config = os.path.expanduser("~/.envm/user-config.json")
	with open(user_config, 'r') as ucf:
		config = json.load(ucf)
	ENVMHOME = congfig["HOME"]
	ENVMDIR = config["ENVMDIR"]
except:
	ENVMHOME = os.path.expanduser("~") 
	ENVMDIR = "/.envm/"
