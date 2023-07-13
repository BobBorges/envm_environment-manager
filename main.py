#!/usr/bin/env python3
"""
A little environment manager for python virtual environments.

  - activate venv environments by key instead of path
  - add existing venv environments to envm
  - create venv environments via envm
  - remove venv environments via envm
"""
from app.activate import activate_venv
from app.add import add_venv
from app.config import *
from app.init import initialize_envm
from app.list import list_envs
from app.utils import (
	init_precheck, 
	init_check
)
import argparse, sys



def main(args):
	debug = args.debug
	if debug:
		print(ENVMHOME, ENVMDIR)
		print(vars(args))

	command = args.command

	if command == "activate":
		activate_venv(args)

	elif command == "add":
		OK, messages = add_venv(args)
		if OK:
			print(f"Success! venv with key -- {args.key} -- successfully added to envm.")
		else:
			print("Oeps! Initialization failed:\n\n")
			for m in messages:
				print(f"   {m}")
			print("\n\n")

	elif command == "init":
		OK, messages = initialize_envm(args) 
		if OK:
			print("Success! envm successfully initialized.")
		else:
			print("Oeps! Initialization failed:\n\n")
			for m in messages:
				print(f"   {m}")
			print("\n\n")

	elif command == "list":
		list_envs(args)
	




if __name__ == '__main__':
	run = True
	#
	# ARGUMENTS
	#
	# create parser and subparser
	parser = argparse.ArgumentParser(
		prog = "envm (alias)", 
		description = __doc__,
		formatter_class = argparse.RawDescriptionHelpFormatter
	)
	parser.add_argument("-d", "--debug", action='store_true', help=argparse.SUPPRESS)
	subparsers = parser.add_subparsers(
		help = "Run command with -h for more info", 
		required = True,
		dest = "command"
	)


	# Initialize envm
	initp = subparsers.add_parser("init", 
		help="Initializes envm for user."
	)
	initp.add_argument("-l", "--envm-home", 
		type=str, 
		default=ENVMHOME, 
		help=f"Set the loaction to initialize envm. (Default: {ENVMHOME})"
	)
	initp.add_argument("-e", "--envm-dir", 
		type=str, 
		default=ENVMDIR, 
		help=f"Set name of the envm directory, which will be written \
		in ENVM_HOME and contain envm files. (Default: {ENVMDIR}))"
	)


	# Add env to envm
	addp = subparsers.add_parser("add", 
		help="Adds an existing venv to envm."
	)
	addp.add_argument("-k", "--key", type=str, required=True, help="Key for venv")
	addp.add_argument("-e", "--env", 
		type=str, 
		default=".", 
		help="Path to venv. (Default: '.')"
	)
	addp.add_argument("-d", "--description", 
		type=str, 
		help="Short description of venv."
	)
	addp.add_argument("-r", "--add-rc", action="store_true", help="Adds envmrc file to venv/bin/activate.")


	# Create env via envm
	createp = subparsers.add_parser("create", 
		help="[under dev] Create a new venv and add to envm"
	)


	# Activate env via envm
	activatep = subparsers.add_parser("activate",
		help="Aactivate venv by key."
	)
	activatep.add_argument("-c", "--copy", action="store_true", help="Add 'source <path_to_venv>/bin/activate' to clipboard.")
	activatep.add_argument("key", type=str, help="Key of venv to activate.")


	# List
	listp = subparsers.add_parser("list",
		help="Show venvs envm knows about."
	)
	listp.add_argument("-v", "--verbose", action="store_true", help="Show details.")

	
	# Removes env from envm
	rmp = subparsers.add_parser("remove", 
		help="[under dev] Removes venv from envm (doesn't delete venv)."
	)
	rmp.add_argument("-k", "--key", type=str, help="Key for venv")


	# parse args
	args = parser.parse_args()




	#
	# pre-MAIN checks
	#
	debug = args.debug
	command = args.command
	if command != "init":
		if debug:
			print("Running init_precheck")
		if not init_precheck():
			if debug:
				print(" -> init_precheck: FAIL")
			initp.print_help()
			sys.exit()
		else:
			if debug:
				print(" -> init_precheck: PASS")
	else:
		if debug:
			print("called 'init'")
			print("running init_check")
		if not init_check(args):
			if debug:
				print(" -> init_check: FAIL")
			sys.exit()
		else:
			if debug:
				print(" -> init_check: PASS")

	if command == "create":
		print("called 'create'")
	elif command == "remove":
		print("called 'remove'")




	#
	# RUN MAIN ?
	#
	if run:
		main(args)
	else:
		parser.print_help()

