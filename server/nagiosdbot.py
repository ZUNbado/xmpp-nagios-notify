#!/usr/bin/python

import xmpp, sys, os
from jabberbot import JabberBot, botcmd
from ConfigParser import RawConfigParser

class NagiosdBot(JabberBot):
    @botcmd
    def notify(self, mess, args):
        print 'hola'+args
        """Send notify"""
       
def nagbot(bot):
  checkpid(os.getpid(),'/tmp/nagiosdbot.server.pid')
  bot.serve_forever()

def fifo(bot):
  pipe = '/tmp/nagios.fifo'
  checkpid(os.getpid(),'/tmp/nagiosdbot.fifo.pid')
  if not os.path.exists(pipe):
    os.mkfifo(pipe)

  fifo = open(pipe, 'r')
  while 1:
    line = fifo.readline()
    if len(line):
      # aqui faig
      args=line.split('===')
      print "TO: "+args[0]
      print "MSG: "+args[1]
      bot.send(args[0],args[1])
    else:
      newfifo = open(pipe, 'r')
      fifo.close()
      fifo = newfifo

def writepid(pid,pidfile):
  pfd = open(pidfile, 'w')
  pfd.write("%s" % pid)
  pfd.close()

def checkpid(pid,pidfile):
  if os.path.exists(pidfile):
    pfd = open(pidfile, 'r')
    oldpid = pfd.readline()
    if len(oldpid):
      try:
        os.kill(int(oldpid), 9)
      except OSError:
        pass
  pfd = open(pidfile, 'w')
  pfd.write("%s" % pid)
  pfd.close()

if __name__ == "__main__":
  config = RawConfigParser()
  config.read(['/etc/nagiosdbot.cfg','nagiosdbot.cfg'])

  pid = os.fork()
  if pid == 0:
    botfifo = NagiosdBot(config.get('nagiosdbot','username'),config.get('nagiosdbot','password'),'fifo')
    fifo(botfifo)
    sys.exit(0)
  pid = os.fork()
  if pid == 0:
    bot = NagiosdBot(config.get('nagiosdbot','username'),config.get('nagiosdbot','password'),'bot')
    nagbot(bot)
    sys.exit(0)
