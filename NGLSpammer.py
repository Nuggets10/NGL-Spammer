from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pystyle import Colors, Colorate

#------------------------------------------ METHODS

def DataCollect():
    link = input(f"{Fore.CYAN}Enter link to the NGL user:   {Style.RESET_ALL}")
    if 'http' in link.lower():
        print(f"{Fore.GREEN}🟩 | LINK FOUND{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🟨 | wait...{Style.RESET_ALL}")
        OpenNGL(link)
    else:
        print(f"{Fore.RED}🟥 | Invalid link, please try again{Style.RESET_ALL}")
        DataCollect()

def OpenNGL(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print(f"{Fore.GREEN}🟩 | Successfully accessed the link{Style.RESET_ALL}")
            GetInfoOnSite(response, link)
        else:
            print(f"{Fore.RED}🟥 | Failed to access the link, status code: {response.status_code}{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}🟥 | An error occurred: {e}{Style.RESET_ALL}")

def GetInfoOnSite(response, link):
    numberOfRequestsStr = input(f"{Fore.CYAN}How many requests would you like to make?{Style.RESET_ALL}")
    numberOfRequests = int(numberOfRequestsStr)
    soup = BeautifulSoup(response.content, 'html.parser')
    input_field = soup.find('textarea', {'id': 'question'})
    print(f"{Fore.YELLOW}🟨 | wait...{Style.RESET_ALL}")
    if input_field:
        print(f"{Fore.GREEN}🟩 | Found GUI components: {input_field}{Style.RESET_ALL}")
        startAttack = input(f"{Fore.CYAN}Start attack? Y/n     {Style.RESET_ALL}")
        if startAttack.lower() == 'y':
            print(f"{Fore.GREEN}🟩 | Starting...{Style.RESET_ALL}")
            MessageLoop(link, numberOfRequests)
        elif startAttack.lower() == 'n':
            print(f"{Fore.RED}🟥 | Killing the script{Style.RESET_ALL}")
        else:
            print("Invalid input. Please enter 'Y' or 'n'.")
    else:
        print(f"{Fore.RED}🟥 | Input field not found{Style.RESET_ALL}")
        retrySearch = input("Retry? Y/n     ")
        if retrySearch.lower() == 'y':
            print(f"{Fore.GREEN}🟩 | Starting...{Style.RESET_ALL}")
            GetInfoOnSite()
        elif retrySearch.lower() == 'n':
            print(f"{Fore.RED}🟥 | Killing the script{Style.RESET_ALL}")

        else:
            print("Invalid input. Please enter 'Y' or 'n'.")

def MessageLoop(link, numberOfRequests):
    
    
    print(Colorate.Vertical(Colors.red_to_yellow,"""
 █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗    ███████╗████████╗ █████╗ ██████╗ ████████╗███████╗██████╗ 
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
███████║   ██║      ██║   ███████║██║     █████╔╝     ███████╗   ██║   ███████║██████╔╝   ██║   █████╗  ██║  ██║
██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗     ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ██╔══╝  ██║  ██║
██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗    ███████║   ██║   ██║  ██║██║  ██║   ██║   ███████╗██████╔╝
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ """))
    count = 0
    while count < numberOfRequests:
        start_time = time.time()
        elapsed_time = 0  # Initialize elapsed_time

        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')  # Non carica la grafica della finestra
            options.add_argument('--disable-gpu')  # Disabilita accelerazione GPU
            options.add_argument('--no-sandbox')  # Bypass OS security model
            options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
            options.add_argument('--incognito')  # Attiva modalità in incognito
            options.add_argument("--disable-tracking")
            options.add_argument("--disable-third-party-cookies")

            driver = webdriver.Chrome(options=options)
            driver.get(link)
            print(f"{Fore.GREEN}🟨 | Found {driver} and {link} {Style.RESET_ALL}")

            textarea = driver.find_element(By.ID, 'question')
            print(f"{Fore.GREEN}🟨 | Found {textarea}{Style.RESET_ALL}")
            submitButton = driver.find_element(By.CLASS_NAME, 'submit')
            print(f"{Fore.GREEN}🟨 | Found {submitButton}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}🟩 | Found every element. Ready to go{Style.RESET_ALL}")


            textarea.send_keys("TEST")
            textarea.send_keys(Keys.RETURN)
            submitButton.click()


            count += 1
            end_time = time.time()
            elapsed_time = (end_time - start_time)  # Convert to milliseconds
            
            print(f"{Fore.GREEN}🟩 | Sent request in {elapsed_time:.2f} seconds. Request number: {count}{Style.RESET_ALL}")
        except Exception as failure:
            handle_error(failure, elapsed_time, count, link)
        finally:
            driver.quit()

def handle_error(failure, elapsed_time, count, link):
    print(f"{Fore.RED}🟥 | Error: {failure} | Elapsed time: {elapsed_time:.2f} seconds | Request number: {count} | Link: {link}{Style.RESET_ALL}")

    

colorama_init()

#------------------------------------------ START CODE

print(Colorate.Vertical(Colors.cyan_to_green,"""
                          █████                    
                 ███████████                 
                ██░  ██░░░░░░░░░░            
              █████████░░░░░░░░░░░░          
             ███████████████████░░░░         
            ████▒   ▒███▒   ▒████            
           ████               ████           
         ████▓                 ▓████         
        █████                   █████        
      ██████                     ██████      
     ███████                     ▓██████     
     ██████░                     ░██████     
    ███████                       ███████    
   ████████                       ████████   
   ████████░                      ████████   
   ████████▓                     ▓████████   
   █████████                     █████████   
   ███  ████▓                   ▓████  ████  
   ██    ████▒                 ░████    ██   
          ████▓               ▒████          
         ░░█████             █████░░         
        ░░░░░▒▒███▒       ▒███▓▒░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░           ░░░░░░░░░     """)) 
print(Colorate.Horizontal(Colors.green_to_cyan,"""

███╗   ██╗ ██████╗ ██╗         ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
████╗  ██║██╔════╝ ██║         ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██╔██╗ ██║██║  ███╗██║         ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║╚██╗██║██║   ██║██║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝"""))      
print (Colorate.Vertical(Colors.red_to_yellow,"""MADE BY NUGGETS WITH <3         
                         
"""))

startProgram = input(f"{Fore.CYAN}Do you want to proceed? Y/n   {Style.RESET_ALL}")

if startProgram.lower() == 'y':
    print(f"{Fore.GREEN}🟩 | Starting...{Style.RESET_ALL}")
    DataCollect()
elif startProgram.lower() == 'n':
    print(f"{Fore.RED}🟥 | Killing the script{Style.RESET_ALL}")

else:
    print("Invalid input. Please enter 'Y' or 'n'.")





                                                                                                                




