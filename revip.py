import time
import requests
import os,sys
from termcolor import colored
os.system("clear")
print(colored(""" 
      ____
    ,'    '.
   /  RevIP \\
   \ ()  () /
    `. /\ ,'
×EVIL| "" |TWIN×
     'UUUU'
"""
,"""red"""))
def rev():
	try:
		inp=input(colored("Target IP: ", "white"))
		if inp=='':
			print(colored("No Address Found !", "red"))
		get=requests.get(f"http://api.hackertarget.com/reverseiplookup/?q={inp}")
		file=open(f"./{inp}.txt", "w")
		if get.text== "error check your search parameter":
			sys.exit(colored(f"(!) '{inp}' Not Valid Address Please Check Your Brain !", "red"))
		elif get.text==f"No DNS A records Found For {inp}":
			print(colored(f"\n(!) No DNS Found On {inp}\n","red"))
			sys.exit()
		else:
			print(file.write(str(get.text)))
			print(colored(f"(✓) Successfully Check {inp}.txt file.", "red"))
	except Exception:
		print(colored(f"Are You Poor ? Please Buy Connection Internet", "red"))
	except KeyboardInterrupt:
		x=input(colored("\n(!) Sure Close ? {Y/N}: ","red"))
		if x=="Y" or x=="y":
			sys.exit
		elif x=="N" or x=="n":
			rev()
		else:
			sys.exit(colored("(!) Application disconnected.","red"))
rev()
