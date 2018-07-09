import argparse
import os
import subprocess
import getpass


def getarg():
	parser = argparse.ArgumentParser(description='get dir and channel owner')

	parser.add_argument("directory")
	parser.add_argument("channel_owner")

	args = parser.parse_args()
	arg_dict = vars(args)

	return arg_dict

def upload_package(arg_dict):
	with os.scandir(arg_dict["directory"]) as it:
		for entry in it:
			if entry.name.endswith(".tar.bz2"):

				directory = arg_dict["directory"]

				package_name = entry.name
				
				upload_cli = f"anaconda upload {directory}/{package_name}"

				subprocess.call(upload_cli, shell = True)


if __name__ == "__main__":

	# subprocess.call("anaconda upload ~/anaconda3/conda-bld/linux-64/tdutils-0.0.3-py36_0.tar.bz2", shell = True)
	upload_package(getarg())

# get the directory using argparse

# ergodic all folders and files through folders

# upload each tar.bz2 files to a certain channel

