from appJar import gui
from jsonload import loadinfo
app = gui()
app.addLabel('appname',loadinfo['appname'])
app.setLabel('appname',)