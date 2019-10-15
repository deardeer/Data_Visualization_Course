#!/usr/bin/env python
#coding:utf-8

import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf-8')

from handler.pointhandler import IndexHandler
from handler.pointhandler import TestHandler

from handler.pointhandler import CheckHandler

url=[
	# (r'/', IndexHandler),
    (r'/test/(\w+)', TestHandler),
    (r'/check', CheckHandler),
]