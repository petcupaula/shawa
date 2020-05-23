# shawa

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
Doesn't show the auth code :(
