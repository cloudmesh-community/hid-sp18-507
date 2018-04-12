import os, time
import datetime
#from pprint import pprint
from flask import request
from stat import *
import connexion


def original(FILE):

	data = {}
	file = os.stat(FILE)
	data["file_name"] = FILE
	data["location"] = os.path.dirname(os.path.realpath(FILE))
	data["bytes_size"] = file[ST_SIZE]
	data["modified"] = time.asctime(time.localtime(file[ST_MTIME]))
	data["accessed"] = time.asctime(time.localtime(file[ST_ATIME]))
	# data["replica"] = str("(Replica) "+FILE)
	# data["replication_time"] = time.asctime(time.localtime())
	return data


def replica(FILE):

	data = {}
	file = os.stat(FILE)
	data["file_name"] = FILE
	data["location"] = os.path.dirname(os.path.realpath(FILE))
	data["bytes_size"] = file[ST_SIZE]
	data["modified"] = time.asctime(time.localtime(file[ST_MTIME]))
	data["accessed"] = time.asctime(time.localtime(file[ST_ATIME]))
	data["replica"] = str("(Replica) "+FILE)
	data["replication_time"] = time.asctime(time.localtime())
	return data

#FILE = "replica.yaml"

#pprint(get_replica_info(FILE))