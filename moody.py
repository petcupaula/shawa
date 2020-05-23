from random import randint, choice
import requests
from time import sleep

ASSISTANT_URL = 'http://localhost:3000/assistant'
min_sleep = 18
max_sleep = 180
file = 'talking_things.txt'

with open(file,'r') as f:
  stories = f.readlines()

print(stories)

def say_smthing():
  print("Time to say something")
  smthing = choice(stories).strip()
  r = requests.post('{0}'.format(ASSISTANT_URL), json={"command": smthing, "broadcast": "true", "user":"robot"})
  print(r.status_code)
  print(r.json())

while True:
  sleep(randint(min_sleep, max_sleep)) #sleep for a random number of seconds
  say_smthing()
