# ENVM - VENV manager

This is a small manager for python venv virtual environments.

Features:

- Activate venv by key from anywhere in the file system
- Add existing venv environments to envm
- Create venv environments via envm
- Remove venv environments from envm

## Installation

### Currently, while under dev:

Clone this repo, create bash alias `envm` and point it to main.py.

### Plan

Eventually, I want to put this on pypi with an entry point so you just pip install and have `envm` available anywhere.


## Commands

### `init`

Initializes envm. 

The command sets an envm home directory and envm directory, by default these are `~/` and `.envm/`.

It writes a `config.json` file in the envm directory with config options and an `envs.json` file via which envm has access to venv environments.

It also creates and `envmrc` file which contains a basic `bashrc` and link to `.bash_aliases` file -- this has to do with the hacky way envm activates a venv in the same terminal. If the user chooses, this `envmrc` file will be linked via the created/added venv `bin/activate` file to maintain terminal color and bash aliases in the activeated venv.

### `add`

Adds a venv to the `~/.envm/envs.json` database. The user provides a key and path (required), and optionally a description and the option to link `envmrc` in the venv `bin/activate` file.

### `create`

Not yet written. (Create a venv and add it to `.envm/envs.json`.)

### `activate`

Activates a venv by key. Optionally,, with `-c`, instead of activating the venv directly, copies `source path/to/venv/bin/activate`. Handy, e.g. with file manager-embedded terminals that won't change directories if a subprocess like venv is opened.

### `list`

Lists venv environments known to envm (in the `.envm/envs.json` file) and description. Verbose option also lists each venv's full path and python version.

### `remove`

Not yet written. (remove venv from `.envm/envs.json`.)