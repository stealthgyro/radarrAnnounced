import datetime
import logging

import config
import db
import radarr
import utils

cfg = config.init()

############################################################
# Tracker Configuration
############################################################
name = "PTP"
irc_host = "irc.passthepopcorn.me"
irc_port = 7000
irc_channel = "#ptp-announce"
irc_tls = True
irc_tls_verify = False

# these are loaded by init
auth_key = None
torrent_pass = None
nick = None
irc_key = None
announcer = None
authstring = None
site_username = None

logger = logging.getLogger(name.upper())
logger.setLevel(logging.DEBUG)

############################################################
# Tracker Framework (all trackers must follow)
############################################################
# Parse announcement message
torrent_title = None

@db.db_session
def parse(announcement):
    global name, torrent_title

    # extract required information from announcement
    torrent_title = utils.formatted_torrent_name(utils.str_before(announcement, ' - http'))
    torrent_id = utils.get_id(announcement, 1)

    if torrent_id is not None and torrent_title is not None:
        download_link = get_torrent_link(torrent_id, utils.replace_spaces(torrent_title, '.'))

        announced = db.Announced(date=datetime.datetime.now(), title=utils.replace_spaces(torrent_title, '.'),
                                 indexer=name, torrent=download_link)
        approved = radarr.wanted(torrent_title, download_link, name)
        if approved:
            logger.debug("Radarr approved release: %s", torrent_title)
            snatched = db.Snatched(date=datetime.datetime.now(), title=utils.replace_spaces(torrent_title, '.'),
                                   indexer=name, torrent=download_link)
        else:
            logger.debug("Radarr rejected release: %s", torrent_title)
        torrent_title = None


# Generate torrent link
def get_torrent_link(torrent_id, torrent_name):
    torrent_link = "https://passthepopcorn.me/torrents.php?action=download&id={}&authkey={}&torrent_pass={}" \
        .format(torrent_id, auth_key, torrent_pass)
    return torrent_link


# Initialize tracker
def init():
    global auth_key, torrent_pass

    auth_key = cfg["{}.auth_key".format(name.lower())]
    torrent_pass = cfg["{}.torrent_pass".format(name.lower())]
    
    #site_username = cfg["{}.site_username".format(name.lower())]
    #irc_key = cfg["{}.irc_key".format(name.lower())]
    #nick = cfg["{}.nick".format(name.lower())]
    #announcer = cfg["{}.announcer".format(name.lower())]
    #authstring = "ENTER {} {} {}".format(site_username, irc_key, irc_channel)

    # check auth_key && torrent_pass was supplied
    if not auth_key or not torrent_pass:
        return False

    return True
