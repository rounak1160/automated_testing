#!/usr/bin/python
import urllib, urllib2
import cookielib

base_url='https://ras.virtual-labs.ac.in/wiki/index.php/Special:UserLogin'
login_action='/account/login'
cookie_file = 'mfp.cookies'



cj = cookielib.MozillaCookieJar(cookie_file)
opener = urllib2.build_opener(
     urllib2.HTTPRedirectHandler(),
     urllib2.HTTPHandler(debuglevel=0),
     urllib2.HTTPSHandler(debuglevel=0),            
     urllib2.HTTPCookieProcessor(cj)
)


opener.addheaders = [('User-agent',
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) '
     'AppleWebKit/535.1 (KHTML, like Gecko) '
     'Chrome/13.0.782.13 Safari/535.1'))
]


response = opener.open(base_url)
cj.save()
#Then finally we can call the login action with our username and password and login to the website:
#<pre># parameters for login action
login_data = urllib.urlencode({
    'username' : 'rounak.patni',
    'password' : 'hellorounak123',
    'remember_me' : True
})
# construct the url
login_url = base_url + login_action
# then open it
response = opener.open(login_url, login_data)
# save the cookies and return the response       
cj.save()
