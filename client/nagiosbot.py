#!/usr/bin/python

import xmpp,random,subprocess,os,sys,syslog,dbus
from jabberbot import *
from ConfigParser import RawConfigParser

class NagiosBot(JabberBot):
    @botcmd
    def action(self, mess, args):
      params=args.split(' ')
      action = params.pop(0)
      if action in dir(self):
        print 'existeix'
      else:
        actionpy = os.getcwd()+'/actions/'+action+'.py'
        if os.path.isfile(actionpy):
          execfile(actionpy)

    @botcmd
    def notify(self,mess,args):
      execfile(os.getcwd()+'/actions/notify.py')

def notification(title,text,icon):
      item              = "org.freedesktop.Notifications"
      path              = "/org/freedesktop/Notifications"
      interface         = "org.freedesktop.Notifications"
      app_name          = "xmpp-notifier"
      id_num_to_replace = 0
      actions_list      = ''
      hint              = ''
      time              = 4000   # Use seconds x 1000

      bus = dbus.SessionBus()
      notif = bus.get_object(item, path)
      notify = dbus.Interface(notif, interface)
      notify.Notify(app_name, id_num_to_replace, icon, title, text, actions_list, hint, time)

def checkpid(pid,pidfile):
  if os.path.exists(pidfile):
    pfd = open(pidfile, 'r')
    oldpid = pfd.readline()
    if len(oldpid):
      syslog.syslog('Killing old process')
      try:
        os.kill(int(oldpid), 9)
      except OSError:
        pass
  pfd = open(pidfile, 'w')
  pfd.write("%s" % pid)
  pfd.close()

config = RawConfigParser()
#config.read(['/etc/nagiosbot.cfg','nagiosbot.cfg',os.getcwd()+'/nagiosbot.cfg'])
config.read('/home/marti/nagiosbot/nagiosbot.cfg')
bot = NagiosBot(config.get('nagiosbot','username'),
                config.get('nagiosbot','password'),
                res=os.environ['USER']+`random.randrange(0, 1000001, 5)`)

pid = os.fork()
if pid > 0:
  sys.exit(0)

checkpid(os.getpid(),'/tmp/nagiosbot.client.pid')
bot.serve_forever()
