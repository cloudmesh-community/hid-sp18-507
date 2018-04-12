# Swagger Replica

The purpose of this resource is to provide file metadata for a file being replicated on a server/system. This will produce information such as the file name, location, date accessed and modiefied, and filesize.

Genrating the swagger service:

	make

Running the service:

	make run

Example output in pretty-print format (JSON):

	{'accessed': 'Wed Apr 11 11:27:27 2018',
	 'bytes_size': 705,
	 'file_name': 'replica.yaml',
	 'location': '/home/datasci/school/bigdata/github/cloudmesh-community/hid-sp18-507/swagger/replica',
	 'modified': 'Wed Apr 11 11:47:33 2018',
	 'replica': '(Replica) replica.yaml',
	 'replication_time': 'Wed Apr 11 12:28:51 2018'}
