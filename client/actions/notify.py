for arg in args.split('-#-'):
  exec arg

if atype == "host":
  title=host + ' is ' + state

if atype == "service":
  title=host + '/' + servdesc + ' is ' + state

if state == 'OK':
  img = 'greendot.gif'
elif state == 'WARNING':
  img = 'warning.png'
elif state == 'CRITICAL':
  img = 'critical.png'
else:
  img = 'notify.gif'

notification(title,output,os.getcwd() + '/img/' + img)
