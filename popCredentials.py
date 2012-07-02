# class in the poppins thingamajig
from poplib import *

class poppinsMary:
    def __init__(self):
        popIp='aaa.bbb.ccc.ddd'
        popAddr='email@address.com'
        popPass='EmailPassword'

class poppins:

  def __init__(self):
    x=poppinsMary()
    self.popSrvr = POP3(x.popIp) # ip works better than url
    print self.popSrvr.getwelcome() # todo: convert print to debug
    print self.popSrvr.user(x.popAddr) # todo: chng print to dbg
    print self.popSrvr.pass_(x.popPass) # todo: s/print/debug.validate(
    messagesInfo = self.popSrvr.list()[1]
    self.numMessages = len(messagesInfo)
