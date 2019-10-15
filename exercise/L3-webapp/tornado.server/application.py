#!/usr/bin/env python
#coding:utf-8

from url import url 

import tornado.web
import os

# import pymongo
# from pymongo import MongoClient

setting = dict(
  # template_path=os.path.join(os.path.dirname(__file__),"template"),
  static_path=os.path.join(os.path.dirname(__file__),"./"), #.. 上级目录，.当前目录
  template_path=os.path.join(os.path.dirname(__file__), "./")
)

application = tornado.web.Application(
  handlers=url,
  debug=True,
  **setting
)
