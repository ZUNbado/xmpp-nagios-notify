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
        params=args.split('-#-')
        for arg in params:
            exec arg

        if atype == "host":
            title='Host ' + host + ' is ' + state

        if atype == "service":
            title='Service ' + servdesc + ' in state ' + state

        if state == 'OK':
            img = 'greendot.gif'
        elif state == 'WARNING':
            img = 'warning.png'
        elif state == 'CRITICAL':
            img = 'critical.png'
        else:
            img = 'notify.gif'

        n = pynotify.Notification(title,output,os.getcwd() + '/img/' + img)
        n.show()


config = RawConfigParser()
config.read(['/etc/nagiosbot.cfg','nagiosbot.cfg'])

bot = NagiosBot(config.get('nagiosbot','username'),
                config.get('nagiosbot','password'))
bot.serve_forever()
