#!/usr/bin/python

import popCredentials

popJones=popCredentials.poppins()
for i in range(popJones.numMessages):
  messageIs = popJones.popSrvr.retr(i+1)[1]
  print "==========================",
  print " message number",i,
  print "=========================="
  for j in messageIs:
    print j
    continue
