from tornado.options import define,options

define("port",default=22025,help="run on th given port",type=int)
#define("db", default="trajlit", help="database", type=str)
#define("title", default="Survey of trajectory visual analytics", help="the topic of literature, e.g. trajlit", type=str)