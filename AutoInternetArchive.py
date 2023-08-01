from waybackpy import WaybackMachineSaveAPI
import waybackpy.exceptions
from user_agent import generate_user_agent
import threading
import time
from datetime import datetime
import os

urls = []

print("Enter the URL you wish to save: ")
while True:

    # Grab URL to archive, if URL is empty, move on
    url = input()
    if url == "" or " " in url and len(url) < 3:
        break

    # Grab interval in hours at which the script will archive the URLs
    while True:
        interval = input("How many hours between each archive do you wish for this URL?: ")
        if interval.isnumeric() == False:
            print("You need to enter a number here!")
        else:
            break

    # Append URL and interval to urls list
    urls.append([url, int(interval)])
    print(url + " added!\n\nEnter a new additional URL or press ENTER to start:")

os.system("cls")

def user_agent():
    user_agent = generate_user_agent()
    return user_agent

def Time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return str("[" + current_time + "]")

def ArchiveURL(url, interval):
    while True:
        print(Time() + "Archive started for: " + url)
        save_api = WaybackMachineSaveAPI(url, user_agent())
        save_api.save()
        if interval == 1:
            hour = " hour!"
        else:
            hour = " hours!"
        print(Time() + "Archive completed for: " + url + "\nNext archive for " + url + " will start in " + str(interval) + hour)
        time.sleep(interval * 3600)

for list in urls:
    try:
        x = threading.Thread(target= ArchiveURL, args=(list[0], list[1])).start()
    except waybackpy.exceptions.TooManyRequestsError:
        # Archive limit of 15 archives per minute per webpage might cause an error if too many archives are attempted at once.
        pass

