# shawa

Youtube demo video: https://youtu.be/yRTgMlEAdNM

## Schematic

<img src="SHAWa schematic.png" width="800">

## Install Assistant Relay on Raspberry Pi

Docs: https://greghesp.github.io/assistant-relay/docs/getting-started/installation

```
# Create a dir for the project on the RPi
cd ~
mkdir shawa

# Install node if not already installed
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v
# Node.js version >= 10.13.0 for Assistant Relay
# PM2 is a pre-requisite
sudo npm i pm2 -g

# Download the Assistant Relay release and copy to Rpi
# Releases: https://github.com/greghesp/assistant-relay/releases
# Because I have Python 3.5 only on this Rpi, then I use version 3.2.0
scp -P 12 release.zip pi@ipaddress:/home/pi/shawa/

unzip release.zip -d assistant-relay
cd assistant-relay
sudo npm run setup

# Start the Assistant Relay
npm run start
# The Assistant Relay page will be hosted at port :3000

# Stop?
#pm2 stop ./bin/www

```

## Configure Assistant Relay

Docs: https://greghesp.github.io/assistant-relay/docs/getting-started/configuration

```
# Follow instructions from docs
# Copy json credential file to RPi
scp -P 12 client_secret_numbers.apps.googleusercontent.com.json pi@ipaddress:/home/pi/shawa/
```
Doesn't show the auth code, shows a blank screen :(

Issue fixed! The type of OAuth that is needed should be 'Other', and not Web. Went again through some of the Google config steps and then it worked - it should pop up a new tab to select account and the consent form. Then it is connected, and the Google Home will say something :D


## Sending requests

```
curl -d '{"command":"hello","broadcast":true,"user":"robot"}' -H 'Content-Type: application/json'  http://ipaddress:3000/assistant
```


## Using AdafruitIO as an MQTT Pub/Sub system

Service homepage: https://io.adafruit.com/

* New feed, called "home_messaging"
* Other services will be able to write to this one using IFTTT

## IFTTT Setup

Service homepage: https://ifttt.com/discover

* Connect as many services as possible/available

## Python script for the "home brain" on the Raspberry Pi

* Script to check for the MQTT "home_messaging" feed and when a message is coming, send it to Google Home to read aloud

```
python3 brainy.py
```

* Generate a brain with a personality (due to the limited time, random script)

```
nano talking_things.txt
python3 moody.py
```

## Running stuff on RPi upon restart

```
# Start Assistant Relay
cd ~/shawa/assistant-relay
npm run start

# Start MQTT brain communication
cd ~/shawa
python3 brainy.py &
python3 moody.py &
```
