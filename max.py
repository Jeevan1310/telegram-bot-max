from dotenv import load_dotenv
import json
import os
import requests

load_dotenv()

print("Mark 8 is booting up")
print('Requesting permission to start ----')

API_KEY=os.getenv("TOKEN")
URL = "https://api.telegram.org/bot{}/".format(API_KEY)

print("Acess granted    --Bot activated----  ")