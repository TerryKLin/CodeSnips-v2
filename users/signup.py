#!/local/bin/python

import os, sys, time, cPickle,urllib,urllib2
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands
from codesnips.models.User import *
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

url_args = cgi.FieldStorage()
args = {x: url_args.getvalue(x) for x in url_args.keys()}

print "Content-type: text/html\n" 
print "<html><head></head><body>"
print "<h1>Homepage</h1>"


print '''<form action="process.py" method="post">
	<br>Name:</br><input type="text" name="Name">
	<br>Email:</br><input type="text" name="Email">
	<br>Password:</br><input type="password" name="pass">
	<br>Date of birth:</br><input type="text" name="dob">
	<br>Bio:</br><input type="text" name="bio">
	<br>Specialization:</br><input type="text" name="spec">
	<br>Gravatar Link:</br><input type="text" name="grav">
    <input type="submit" value="Confirm">
    </form>'''
	
	
	
print "</body></html>"

