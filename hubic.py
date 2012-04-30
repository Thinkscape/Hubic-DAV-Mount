#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Hubic Dav Mount
Mounts your hubic account using davfs

usage : sudo hubic.py username password mount_point

Based on a pythons script by Nicolas P
Based on a perl script written by GR

'''

import httplib, urllib, sys, subprocess

headers = {'Content-type'   : 'application/x-www-form-urlencoded',
          'User-Agent'      : 'ubiC/1.0.9 (Windows NT 6.1; fr_FR)'}

def hubic_credentials(login, password):
    id  = get_session_id(login, password)
    url = get_url(id)
    login, password = get_dav_credentials(id)
    return url, login, password

def get_session_id(login, password):
    params = 'session=&params={"email":"%s","password":"%s"}' % (urllib.quote(login), urllib.quote(password))
    conn = httplib.HTTPSConnection('ws.ovh.com')
    #conn.set_debuglevel(5)
    conn.request("POST", "/cloudnas/r0/ws.dispatcher/nasLogin", params, headers)
    response = conn.getresponse()
    s = response.status
    r = response.reason
    data = response.read()
    if r == 'OK' :
        null = None # null appears inside data
        d = eval(data)
        return d['answer']['id']
    else :
        print data
    conn.close()
    return None

def get_url(id):
    params = 'session=%s' % id
    conn = httplib.HTTPSConnection('ws.ovh.com')
    conn.request("POST", "/cloudnas/r0/ws.dispatcher/getNas", params, headers)
    response = conn.getresponse()
    s = response.status
    r = response.reason
    data = response.read()
    if r == 'OK' :
        null = None # null appears inside data
        d = eval(data)
        return d['answer']['url']
    else :
        print data
    conn.close()
    return None

def get_dav_credentials(id):
    params = 'session=%s' % id
    conn = httplib.HTTPSConnection('ws.ovh.com')
    conn.request("POST", "/cloudnas/r0/ws.dispatcher/getCredentials", params, headers)
    response = conn.getresponse()
    s = response.status
    r = response.reason
    data = response.read()
    if r == 'OK' :
        null = None # null appears inside data
        d = eval(data)
        return d['answer']['username'], d['answer']['secret']
    else :
        print data
    conn.close()
    return None
      

    
if __name__ == '__main__':
    try:
        login       = sys.argv[1]
        password    = sys.argv[2]
        mount_point = sys.argv[3]
    except:
        print "Usage: hubic username password mount_point"
        sys.exit()
        
    hubic_url, hubic_login, hubic_password = hubic_credentials(login, password)
    
    cmd = "echo \"%s\\n%s\" | mount -t davfs %s %s" % (hubic_login, hubic_password, hubic_url, mount_point)
    subprocess.call(cmd, shell=True)
