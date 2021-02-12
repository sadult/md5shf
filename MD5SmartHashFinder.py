import requests,json,os

# MD5 Smart Hash Key Finder
# Ordered by BlackSecurity Team | @BSecurity

IBlue = "\033[0;94m"
IYellow="\033[0;93m"
IRed="\033[0;91m"
ICyan="\033[0;96m"
IGreen="\033[0;92m"
WhiteC = '\033[37m'
RedC = '\033[31m'
GreenC = '\033[32m'
YellowC = '\033[33m'
BlueC = '\033[34m'

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printOurLogo():
	return print(IYellow+f"MD5 Smart Hash Key Finder\n{YellowC}Black Security  |  @BSecurity\n{RedC}------------------------------")

def startApp():
	Clear()
	printOurLogo()
	enterhash = input(IBlue+f"╾──╸ {ICyan}Please Enter Your Hash >> "+WhiteC)
	Clear()
	printOurLogo()
	print(IBlue+f"╾╥──╸ {ICyan}Please Enter Your Hash >> "+WhiteC+enterhash)
	print(IBlue+f" ╙──╸ {ICyan}Please wait...")
	getkon = requests.get(f"http://www.nitrxgen.net/md5db/{enterhash}.json").text
	if(getkon == "" or getkon == None):
		Clear()
		printOurLogo()
		print(IBlue+f"╾╥──╸ {ICyan}Please Enter Your Hash >> "+WhiteC+enterhash)
		print(IBlue+f" ╟──╸ {ICyan}Please wait...")
		input(IBlue+f" ╙──╸ {IRed}Hash is invalid ")
		startApp()
	else:
		pass
	results = json.loads(getkon)
	check = results["result"]["found"]
	if(check == False):
		Clear()
		printOurLogo()
		print(IBlue+f"╾╥──╸ {ICyan}Please Enter Your Hash >> "+WhiteC+enterhash)
		print(IBlue+f" ╟──╸ {ICyan}Please wait...")
		input(IBlue+f" ╙──╸ {IRed}Hash key not found ")
		startApp()
	elif(check == True):
		hashpass = results["result"]["pass"]
		hexpass = results["result"]["hexpass"]
		Clear()
		printOurLogo()
		print(IBlue+f"╾╥──╸ {ICyan}Hash >> "+WhiteC+enterhash)
		print(IBlue+f" ║")
		print(IBlue+f" ╙──╾╥╸ {IGreen}Hash key founded ! ")
		print(IBlue+f"     ║")
		print(IBlue+f"     ╟╸ {IYellow}Password : {hashpass}")
		print(IBlue+f"     ╙╸ {IYellow}HexPassword : {hexpass}")
	input(GreenC+"\n\n* Press Enter To Continue "+WhiteC)
	startApp()

while True:
	startApp()