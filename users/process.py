#!/local/bin/python

import os, sys, inspect
import cgi
import cgitb; cgitb.enable()
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands

print "Content-type: text/html\n"

form = cgi.FieldStorage()
name = form.getvalue('Name')
email = form.getvalue('Email')
passw = form.getvalue('pass')
dob = form.getvalue('dob')
bio = form.getvalue('bio')
spec = form.getvalue('spec')
grav = form.getvalue('grav')


cmd = dbCommands.AddToDatabaseCommand("User", "name,email,password, dob, bio, specialization, gravatarLink", "'"+str(name) + "', '" + str(email) + "', '" + str(passw) + "', '" + str(dob) + "','" + str(bio) + "', '" + str(spec) + "', '" + str(grav) + "'")
cmd.execute()

print '<meta http-equiv="refresh" content="1;url=http://web.cs.dal.ca/~coelho/oop/index1.py" />'
