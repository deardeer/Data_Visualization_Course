
import tornado.web
from tornado.options import options

import pymongo
from pymongo import MongoClient

import setting

from PIL import Image
import io
import os.path

import json

import subprocess

import pandas as pd

import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Weixin_2016']
db_share = db['share']
db_users = db['infor']

graphIndex = 5
df_subgraph = pd.read_csv('subgraph_node_new_' + str(graphIndex) + '.csv')
df_sublink = pd.read_csv('subgraph_new_' + str(graphIndex) + '.csv')

class TestHandler(tornado.web.RequestHandler):
    def get(self, word):
        print('getsurvey handler', word);       
        self.write('ok');

class GraphHandler(tornado.web.RequestHandler):
	def post(self):
		self.set_header('Access-Control-Allow-Origin', "*")
		liNodeInfo = []
		liNodeId = list(df_subgraph['node'])
		liLabel = list(df_subgraph['label'])
		print(liLabel)
		for index in range(0, len(liNodeId)):
			openId = liNodeId[index]
			# nodeId = liId[index]
			node = db_users.find_one({'open_id': openId})
			liNodeInfo.append(node)
		print('getgraph')

		liEdge = []
		for index, row in df_sublink.iterrows():
			# print(type(row['target']))
			liEdge.append(str(row['target']) + '-' + str(row['source']))
		print('edge', liEdge[0:5])
      
		self.write({'nodeInfo': liNodeInfo, 'ids': liNodeId, 'labels': liLabel, 'edges': liEdge});

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')
