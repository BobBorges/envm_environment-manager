"""
Activate venv by key.
"""
from app.config import *
import json, os, pyperclip, subprocess


def activate_venv(args):
	#print("ACTIVATE")
	with open(f"{ENVMHOME+ENVMDIR}envs.json", "r") as inf:
		d = json.load(inf)
	if args.key in d["envs"]:
		path = f"{d['envs'][args.key]['PATH']}/bin/activate"
		if args.copy:
			pyperclip.copy(f'source {path}')
			print(f"Paste into terminal (already copied): \nsource {path}")
		else:
			print("")
			print("")
			print(f"     +-----------{'-'*len(args.key)}-------------------------------------------------+")
			print(f"  ~~~|  Starting {args.key} environment. Use the 'exit' command to finish.  |~~~")
			print(f"     +-----------{'-'*len(args.key)}-------------------------------------------------+")
			print("")
			print("")
			os.system(f'bash --rcfile {path}')
			print("")
			print("")
			print(f"     +---------{'-'*len(args.key)}---------------+")
			print(f"  ~~~|  Exited {args.key} environment.  |~~~ ")
			print(f"     +---------{'-'*len(args.key)}---------------+")
			print("")	
	else:
		print("¡¡¡ERROR!!! Bad key.")

