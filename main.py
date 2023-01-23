import requests
import json
from termcolor import colored
## Small program to get the top album on your day of birth from the Billboard 200 chart

banner = """
  ____  _ _ _                         _   ___   ___   ___                     
 |  _ \(_) | |                       | | |__ \ / _ \ / _ \                    
 | |_) |_| | |__   ___   __ _ _ __ __| |    ) | | | | | | |                   
 |  _ <| | | '_ \ / _ \ / _` | '__/ _` |   / /| | | | | | |                   
 | |_) | | | |_) | (_) | (_| | | | (_| |  / /_| |_| | |_| |                   
 |____/|_|_|_.__/ \___/ \__,_|_|  \__,_| |____|\___/ \___/                    
 |  _ \(_)    | | | |       | |                 /\   | | |                    
 | |_) |_ _ __| |_| |__   __| | __ _ _   _     /  \  | | |__  _   _ _ __ ___  
 |  _ <| | '__| __| '_ \ / _` |/ _` | | | |   / /\ \ | | '_ \| | | | '_ ` _ \ 
 | |_) | | |  | |_| | | | (_| | (_| | |_| |  / ____ \| | |_) | |_| | | | | | |
 |____/|_|_|   \__|_| |_|\__,_|\__,_|\__, | /_/    \_\_|_.__/ \__,_|_| |_| |_|
                                      __/ |                                   
                                     |___/
"""

print(colored(banner, "green"))

## API URL 
url = "https://billboard-api2.p.rapidapi.com/billboard-200"

## User input for birthday
birthday = input(str("What is your birthday? (YYYY-MM-DD) ?\n"))

## print(birthday)

## API query string 
querystring = {"date": birthday,"range":"1-10"}

# print(querystring)

headers = {
	"X-RapidAPI-Key": "YOUR_API_KEY",
	"X-RapidAPI-Host": "billboard-api2.p.rapidapi.com"
}


## Try to get the response from the API and print the status code. If there is an error, print the error.
try:
    response = requests.request("GET", url, headers=headers, params=querystring, timeout=(2,4))
    print(f'Status Code:{response.status_code} Success! \n')
    response.close()
except requests.exceptions.RequestException as e:
    print(e)
    

## Parse the response and place the album and artist in variables
birthday_album = json.loads(response.text)
album = birthday_album["content"]["1"]["album"]
artist = birthday_album["content"]["1"]["artist"]


print("**************************************************")
print("Your birthday album is: " + album + " by " + artist)