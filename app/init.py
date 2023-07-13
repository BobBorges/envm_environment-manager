"""
Everything related to initializing envm.
"""
import os, json


envmrc = """# Color your terminal (Copied from ~/.bashrc)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# Include bash aliases
if [ -f ~/.bash_aliases ]; then
	. ~/.bash_aliases
fi

"""

def initialize_envm(args):
	OK = True
	messages = []
	debug = args.debug
	if debug:
		print("Running init")

	# ENVM DIR
	ENVMDIR = args.envm_home+args.envm_dir
	if not os.path.exists(ENVMDIR):
		if debug:
			print("|-- making envdir")
		try:
			os.mkdir(ENVMDIR)
			if debug:
				print(" -> made envmdir")
		except:
			if debug:
				print(" -> Init failed at mkdir envmdir")
			messages.append(f"Couldn't create ENVMDIR at {ENVMDIR}.")
			OK = False
	else:
		if debug:
			print(" -> envmdir exists: skipping")

	# ENVs FILE
	if not os.path.exists(f"{ENVMDIR}envs.json"):
		if debug:
			print("|-- making envs file")
		try:
			envs = {"envs":{}}
			with open(f"{ENVMDIR}envs.json", "w+") as _:
				json.dump(envs, _, ensure_ascii=False, indent=4)
			if debug:
				print(" -> made envs file")
		except:
			if debug:
				print(" -> Init failed at touch envs file")
			messages.append(f"Couldn't touch {ENVMDIR}envs.json")
			OK = False
	else:
		if debug:
			print(" -> envs file exists: skipping")

	# USER CONFIG
	if not os.path.exists(f"{ENVMDIR}config.json"):
		if debug:
			print("|-- making user config file")
		try:
			cfg = {}
			cfg["ENVMHOME"] = args.envm_home
			cfg["ENVMDIR"] = args.envm_dir
			print(cfg)
			with open(f"{ENVMDIR}config.json", "w+") as j:
				json.dump(cfg, j, ensure_ascii=False, indent=4)
			print("here")
		except:
			if debug:
				print(" -> Init failed at create config file")
			messages.append(f"Couldn't create {ENVMDIR}config.json")
			OK = False
	else:
		if debug:
			print(" -> User config exists: updating")
		try:
			with open(f"{ENVMDIR}config.json", "w+") as j:
				cfg = json.load(j)
				cfg["ENVMHOME"] = args.envm_home
				cfg["ENVMDIR"] = args.envm_dir
				with open(f"{ENVMDIR}config.json", "w+") as j:
					json.dump(cfg, j, ensure_ascii=False, indent=4)
		except:
			if debug:
				print(" -> Init failed at update config file")
			messages.append(f"Couldn't touch {ENVMDIR}config.json")
			OK = False
	if not os.path.exists(f"{ENVMDIR}envmrc"):
		try:
			with open(f"{ENVMDIR}envmrc", "w+") as rc:
				rc.write(envmrc)
		except:
			messages.append(f"Couldn't touch {ENVMDIR}envmrc")
			OK = False
	return OK, messages










