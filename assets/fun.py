# lib
import os
import sys
import json
from termcolor import colored

# variables

# classes

# functions
def add(num1,num2):
	return num1 + num2

def _logo_(file):
	if os.path.exists(file):
		return os.system(f"cat {file}")
	else:
		return " > The file {} is missing".format(file)

def _xshell_(cmd):
	if cmd != "":
		return f"""
		 echo "checking for {cmd}";
		 if pip show {cmd} -q
		 then
		 	echo "installed"
		 else
		 	pip install {cmd}
		 fi
		"""
	else:
		print("no")
		
		
	
