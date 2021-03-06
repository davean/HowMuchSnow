#!/usr/bin/env python2.7
import sys
from flup.server.fcgi import WSGIServer
sys.path.append('/home/mmachenry/HowMuchSnow')
import howmuchsnow

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    response_body = make_html_page(howmuchsnow.how_much_snow_ipv4(environ['REMOTE_ADDR']))
    yield response_body

def make_html_page (inches):
    return """
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	  <title>How Much Snow Am I Going To Get?</title>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	</head>

	<body style="text-align: center; padding-top: 200px;">

	<a style="font-weight: bold; font-size: 120pt; font-family: 
	Arial, sans-serif; text-decoration: none; color: black;">
	""" + str(int(round(inches))) + """ inches
	</a>


	</body>
	</html>
    """

WSGIServer(application).run()

