
import tornado.web
from tornado.options import options

# import pymongo
# from pymongo import MongoClient

import setting

# from PIL import Image
import io
import os.path

import json

# import subprocess
import random

class TestHandler(tornado.web.RequestHandler):
    def get(self, word):
        print('getsurvey handler', word);       
        self.write('ok');


class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class CheckHandler(tornado.web.RequestHandler):
	def post(self):
		self.set_header('Access-Control-Allow-Origin', '*');
		# self.write('ok')

		# graph = json.loads(self.get_argument('time'));
		time = self.get_argument('time');
		# todo 
		print('time', time);
		# fit = (random.randint(12, 20)%2==0)? True: False
		fit = True
		self.write({'result': fit})
