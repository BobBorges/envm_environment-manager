"""
utilities
"""
from app.config import *
import os




def init_precheck():
	OK = True 
	messages = []

	# if HOME
	if not os.path.exists(ENVMHOME):
		messages.append(f"The home directory ({ENVMHOME}) doesn't exist.")
		OK = False
	# if ENVMDIR
	if not os.path.exists(ENVMHOME+ENVMDIR):
		messages.append(f"The User envm directory ({ENVMHOME+ENVMDIR}) doesn't exist.")
		OK = False
	# if ENVMDIR/envs.json
	if not os.path.exists(f"{ENVMHOME+ENVMDIR}envs.json"):
		messages.append(f"The User envs file ({ENVMHOME+ENVMDIR}envs.json) doesn't exist.")
		OK = False
	# if ENVMDIR/config.json
	if not os.path.exists(f"{ENVMHOME+ENVMDIR}config.json"):
		messages.append(f"The user config ({ENVMHOME+ENVMDIR}config.json) doesn't exist.")
		OK = False

	if not OK:
		print("¡¡¡WARNING!!! There may be some issue with your instance of envm:\n\n")
		for m in messages:
			print(f"    {m}")
		print("\n\nIf you're just getting started, run 'envm init -h' to see how to set things up. After running init, this message should disappear.\n\n")
		return False
	else:
		return True




def init_check(args):
	OK = True
	messages = []
	# check home dir
	if not os.path.exists(args.envm_home):
		messages.append(f"The home directory ({args.envm_home}) doesn't exist.")
		OK = False
	else:
		# check home dir is writable
		if not os.access(args.envm_home, os.W_OK):
			messages.append(f"The home directory ({args.envm_home}) isn't writable.")
			OK = False
	if not OK:
		print("¡¡¡ERROR!!! envm can't be initialized where you want.\n\n")
		for m in messages:
			print(f"    {m}")
		print("\n\nFix that and try again.")
		return False
	else:
		return True




def get_venv_pyversion(venvpath):
	version = None
	with open(f"{venvpath}/pyvenv.cfg", "r") as inf:
		lines = inf.readlines()
	[line.strip() for line in lines]
	for line in lines:
		if line.startswith("version ="):
			v, V = line.split('=')
			version = V.strip()
	if not version:
		print("\n\n    !!!WARNING!!! No venv version info found.\n\n")
	return version




def add_precheck(venvpath):
	OK = True
	messages = []
	if not os.path.exists(f"{venvpath}/bin/activate"):
		messages.append(f"{venvpath}/bin/activate doesn't exist")
		OK = False
	if not os.path.exists(f"{venvpath}/lib"):
		messages.append(f"{venvpath}/lib/ doesn't exist")
		OK = False
	if not os.path.exists(f"{venvpath}/pyvenv.cfg"):
		messages.append(f"{venvpath}/pyvenv.cfg doesn't exist")
		OK = False
	if not OK:
		print(f"\n\n¡¡¡ERROR!!! It seems like {venvpath} isn't a python venv directory.\n\n")
		for m in messages:
			print("    {m}")
		print("\n\n")
		return False
	else:
		return True




def add_keycheck(key, envs):
	OK = True
	if key in envs:
		OK = False
	if not OK:
		return False
	else:
		return True
	


