# Be sure to modify the ADAFRUIT_IO_KEY and ADAFRUIT_IO_USERNAME variables to
# set your AIO key and username!

# Import standard python modules.
import random
import sys
import time

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

# Import requests library used for making HTTP calls to the dashboard server.
import requests

# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = 'xxx'       # Set to your Adafruit IO key.
ADAFRUIT_IO_USERNAME = 'xxx'  # See https://accounts.adafruit.com

ASSISTANT_URL = 'http://localhost:3000/assistant'

# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for feed changes...')
    client.subscribe('home_messaging')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    print('Will now send it to the assistant relay...')
    # The requests.post function will make an HTTP request against the assistant relay
    r = requests.post('{0}'.format(ASSISTANT_URL), json={"command": payload, "broadcast": "true", "user":"robot"})
    print(r.status_code)
    print(r.json())


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Use the loop_blocking function to run the message loop for processing Adafruit
# IO events.  Since this script doesn't do any other processing this blocking
# version of the message loop is fine.  All the program logic will occur in the
# callback functions above when Adafruit IO feeds are changed.
client.loop_blocking()
#client.loop_background()

#while True:
#  time.sleep(100)
