# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:33:00 2017

@author: 11314
"""

#
#from IPython.core.interactiveshell import InteractiveShell
import time
import numpy as np
import os


#
#
#def get_text(obj):
#    '''
#    OBJ: Any python objects,except PICTURE
#    '''
#    fmt = InteractiveShell.instance().display_formatter.format
#    if obj.__class__ != None.__class__:
#        if isinstance(obj,list):
#            n = len(obj)
#            s = np.array(obj).__str__()
#            st = 'list : %s\nlength : %s'%(s,n)
#            return st
#        else:
#            f_d,md_d = fmt(obj,None,None)
#            return f_d['text/plain']
#    else:
#        raise ValueError


def get_text(obj):
    '''
    OBJ: Any python objects,except PICTURE
    '''
    if obj.__class__ != None.__class__:
        if isinstance(obj,list):
            n = len(obj)
            s = np.array(obj).__str__()
            st = 'list : %s\nlength : %s'%(s,n)
            return st
        else:
            s = obj.__repr__()
            return s
    else:
        return 'None'        
###

     
    
###
#html frame
def ht_frame():
    '''
    Generate a html frame
    '''
    s = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="10">
    <title>Python Outputs --- setting by @Merz</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/uikit/3.0.0-beta.6/css/uikit.min.css" />
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/uikit/3.0.0-beta.6/js/uikit.min.js"></script>
    </head>
    <body>  
    <a class="uk-button uk-button-secondary uk-width-1-1" href="#target" uk-scroll="">Scroll down</a>
    <b><input class="uk-button uk-button-secondary uk-width-1-1 uk-margin-small-bottom" type=button value="Python Outputs" onclick="history.go(0)"></b>
    <br>
    <span class="uk-label"><b>Created on {{date}}</span>
    <br>
    <br>
    <ul uk-accordion="multiple: true" class="uk-accordion">
    {{content}}
    </ul>
    </body>
    <div class = "uk-position-bottom uk-position-fixed">
    <a id="target" class="uk-button uk-button-secondary uk-width-1-1" href="#top" uk-scroll="">Scroll up</a>
    </div>
    </html>'''
    return s
###
def ht_body():
    '''
    Generate a html body
    '''
    s = '''
    <li class="uk-open">
    <h3 class="uk-accordion-title">[OUT %s]: </h3>
    <div class="uk-accordion-content">
    <pre class="uk-background-muted uk-margin-small uk-card uk-card-default uk-card-body uk-text-danger"><b>%s</b></pre>
    </div>
    </li>'''
    return s
###
class htmlprint(object):
    def __init__(self,head,content):
        self.dt = time.strftime('%d-%b-%Y %H:%M',time.localtime(time.time()))
        self._n = 0
        self._h = head.replace('{{date}}',self.dt)
        self._c = content
        self._store = ''
        self.dtt = self.dt.replace(':','-').replace('-','').strip()
        self.file = '%s.html'%(self.dtt)
        self._addres = r'E:\pyoutput\%s'%(self.file)
    def out(self,obj):
        self._n +=1
        st = get_text(obj)#string
        cnew = self._c%(self._n,st)#body
        self._store += cnew
        self.wpage = self._h.replace('{{content}}',self._store)
        with open(self._addres,'w') as tmp:
            tmp.write(self.wpage)
    def cout(self,obj):
        '''
        STDOUT IN CURRENT DIR
        '''
        self._n +=1
        st = get_text(obj)#string
        cnew = self._c%(self._n,st)#body
        self._store += cnew
        self.wpage = self._h.replace('{{content}}',self._store)
        self._dir = os.path.join(dirname,self.file)
        with open(self._dir,'w') as tmp:
            tmp.write(self.wpage)
            print('Result saved at %s !\n'%(self._dir))
            
            
###
#__init__
hed = ht_frame()
cont = ht_body()

p = htmlprint(hed,cont)
