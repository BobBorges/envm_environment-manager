"""
Lists venvs envm knows about.
"""
from app.config import *
import json


def list_envs(args):
	print("Venvs available to envm.\n")
	with open(f"{ENVMHOME+ENVMDIR}envs.json", "r") as inf:
		d = json.load(inf)
	if args.verbose:
		for k, v in d["envs"].items():
			print(f'    {k: <15}{"Desctription:": <20}{v["DESCRIPTION"]: <40}')
			print(f'    {"": <15}{"Path:": <20}{v["PATH"]: <40}')	
			print(f'    {"": <15}{"Python version:": <20}{v["PYVERSION"]: <40}')
			print("")
	else:
		for k, v in d["envs"].items():
			print(f'    {k: <15}{v["DESCRIPTION"]: <20}')
		print("")


