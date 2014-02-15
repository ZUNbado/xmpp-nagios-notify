#!/usr/bin/python

import xmpp
import sys
from jabberbot import JabberBot, botcmd
from ConfigParser import RawConfigParser

class NagiosdBot(JabberBot):
    @botcmd
    def notify(self, mess, args):
        """Send notify"""
        

config = RawConfigParser()
config.read(['/etc/nagiosdbot.cfg','nagiosdbot.cfg'])

bot = NagiosdBot(config.get('nagiosdbot','username'),
                config.get('nagiosdbot','password'))
bot.send(sys.argv[1],sys.argv[2])
