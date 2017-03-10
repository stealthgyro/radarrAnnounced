# radarrAnnounced

Python script to notify radarr of tracker announcements from IRC announce channels.  (still an ealry fork of sonarrAnnounced, work has just begun DON'T EXPECT THIS TO WORK!))
1st draft after all the changes....

## Requirements
1. Python 3.5.2 or newer
2. requirements.txt modules

## Supported Trackers
1. PTP (being worked on)
2. IPTorrents

Open to suggestions/pull requests!

## To-Do



# Installation (on Debian Jessie)
## Python 3.5.2

1. `wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz`
2. `tar xvf Python-3.5.2.tar.xz`
3. `cd Python-3.5.2`
4. `sudo apt-get install make git build-essential libssl-dev zlib1g-dev libbz2-dev libsqlite3-dev`
5. `sudo ./configure --enable-loadable-sqlite-extensions && sudo make && sudo make install`

This should automatically install pip3.5 for you

## radarrAnnounced
1. `cd /opt`
2. `sudo git clone https://github.com/stealthgyro/radarrAnnounced`
3. `sudo chown -R user:group radarrAnnounced`
4. `sudo pip3.5 install -r /opt/radarrAnnounced/requirements.txt`
5. `mv settings.cfg.default settings.cfg`
6. `nano settings.cfg`
- Configure it how you want
7. Edit systemd/announced.service with your user and group
8. `sudo cp announced.service /etc/systemd/system/rannounced.service`
9. `sudo systemctl daemon-reload`
10. `sudo systemctl start rannounced`
- Check it is working properly, http://localhost:PORT - use user/pass you chosen in the [server] section of settings.cfg
11. if you want auto start @ boot, `sudo systemctl enable rannounced`
