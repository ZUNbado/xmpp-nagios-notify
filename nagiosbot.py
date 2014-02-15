#!/usr/bin/python

import xmpp
import pynotify
import os
from jabberbot import JabberBot, botcmd
from ConfigParser import RawConfigParser

class NagiosBot(JabberBot):
    @botcmd
    def notify(self, mess, args):
        """Send notify"""
        pynotify.init("Basic")
        n = pynotify.Notification('title',args)
        n.show()

    def who(self, mess, args):
        """Display who's currently logged in."""
        who_pipe = os.popen('/usr/bin/who', 'r')
        who = who_pipe.read().strip()
        who_pipe.close()

        return who

config = RawConfigParser()
config.read(['/etc/nagiosbot.cfg','nagiosbot.cfg'])

bot = NagiosBot(config.get('nagiosbot','username'),
                config.get('nagiosbot','password'))
bot.serve_forever()
