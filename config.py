import profig

cfg = profig.Config('settings.cfg')


def init():
    global cfg

    # Settings
    cfg.init('server.host', 'localhost')
    cfg.init('server.port', '3468')
    cfg.init('server.user', 'admin')
    cfg.init('server.pass', 'password')

    cfg.init('sonarr.apikey', '')
    cfg.init('sonarr.url', 'http://localhost:7878')

    cfg.init('bot.debug_file', True)
    cfg.init('bot.debug_console', True)

    # Trackers
    cfg.init('iptorrents.nick', '')
    cfg.init('iptorrents.nick_pass', '')
    cfg.init('iptorrents.auth_key', '')
    cfg.init('iptorrents.torrent_pass', '')

    cfg.init('ptp.nick', '')
    cfg.init('ptp.site_username', '')
    cfg.init('ptp.nick_pass', '')
    cfg.init('ptp.auth_key', '')
    cfg.init('ptp.torrent_pass', '')
    cfg.init('ptp.irc_key', '')
    cfg.init('ptp.announcer', 'Hummingbird')

    cfg.sync()
    return cfg
