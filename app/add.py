from app.config import *
from app.utils import (
	add_precheck,
	add_keycheck,
	get_venv_pyversion
)
import json, os, sys


incl_rcfile = """
if [ -f ~/.envm/envmrc ] ; then
	. ~/.envm/envmrc
fi
"""

def add_venv(args):
	debug = args.debug
	OK = True
	messages = []
	if debug:
		print("Running add precheck")
	if not add_precheck(args.env):
		if debug:
			print(" -> add precheck: FAIL")
		messages.append("ARGS.ENV not a venv. Try to point to an existing venv.")
		OK = False
	if debug:
		print(" -> add precheck: PASS")
		print(f"Adding venv {args.key} to envm")
	with open(f"{ENVMHOME+ENVMDIR}envs.json", "r") as inf:
		d = json.load(inf)
	if debug:
		print(" -> opened d")
	if not add_keycheck(args.key, d["envs"]):
		messages.append(f"The key you entered -- {args.key} -- already exists.")
		OK = False
		return OK, messages
	else:
		if OK:
			try:
				version = None
				if debug:
					print("Getting pyversion")
				version = get_venv_pyversion(args.env)
				if debug:
					if version:
						print(" -> Got")
					else:
						print(" -> Get pyversion: FAIL")
				if debug:
					print("Setting venv --{args.key}-- in envm")
				d["envs"][args.key] = {
						"PATH": os.path.abspath(args.env), 
						"PYVERSION": version, 
						"DESCRIPTION":args.description
					}
				if debug:
					print(" -> set")
					print("Writing to envs.json")
				with open(f"{ENVMHOME+ENVMDIR}envs.json", "w") as outf:
					json.dump(d, outf, ensure_ascii=False, indent=4)

				if args.add_rc:
					if debug:
						print("Adding to activate file")
					with open(f"{args.env}/bin/activate", "a") as rc:
						rc.write(incl_rcfile)
				if debug:
					print(" -> wrote")
				return OK, messages
			except:
				messages.append("Add failed somewhere after the venv check and key check")
				OK = False
				if debug:
					print(" -> exception")
					for m in messages:
						print("    {m}")
				return OK, messages
		else:
			return OK, messages
