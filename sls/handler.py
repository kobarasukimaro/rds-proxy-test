import json
import os
import logging
import sys
import re
import boto3
import pprint
import base64

sys.path.append(os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'vendor'))

import mysql.connector

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
pp = pprint.PrettyPrinter(indent=4)

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]

def execute_query(event):
    config = {
        'user': DB_USER,
        'password': DB_PASSWORD,
        'host': DB_HOST,
        'database' : DB_NAME,
    }

    logging.info("connection start")
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(prepared=True)
    logging.info("connection ok")

    query = ("SELECT SLEEP(10)")
    logging.info("query start")
    cursor.execute(query)
    logging.info("query end")

    logging.info("end")

def lambda_handler(event, context):
    logging.debug("<event>: \n" + json.dumps(event))
    execute_query(event)
