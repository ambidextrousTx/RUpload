'''
Handles everything about S3
Uses the boto API

~ Ambidextrous
Aug, 2014
'''

from boto.s3.connection import S3Connection
from boto.s3.key import key
import boto


class S3Handler(object):
    def __init__(self, id_key, secret_key):
        self.id_key = id_key
        self.secret_key = secret_key

    def create_connection():
        connection = S3Connection(self.id_key, self.secret_key)
        boto.connect_s3()
        bucket = connection.get_bucket('RUpload')
        print bucket
