for arg in ' '.join(params).split('-#-'):
  print arg
  exec arg

notification("OTRS Ticket " + ticket,msg,os.getcwd() + '/img/otrs.ico')
