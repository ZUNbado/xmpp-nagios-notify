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
        pynotify.init("image")
        print args
        exec args
        print atype
        if atype == "host":
            title='Host ' + host + ' is ' + state

        if atype == "service":
            title == 'Service ' + servdesc + ' in state ' + state

        n = pynotify.Notification(title,output,os.getcwd() + '/img/critical.png')
        n.show()


config = RawConfigParser()
config.read(['/etc/nagiosbot.cfg','nagiosbot.cfg'])

bot = NagiosBot(config.get('nagiosbot','username'),
                config.get('nagiosbot','password'))
bot.serve_forever()
