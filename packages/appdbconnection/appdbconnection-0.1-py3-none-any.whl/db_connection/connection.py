import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from cassandra.cluster import Cluster
import redis
import couchdb
import boto3 #Amazon DynamoDB using  in boto3 
from neo4j import GraphDatabase

def create_db_connection(config):

    keys = ['db_type', 'db_host', 'db_port', 'db_user', 'db_pass', 'db_name']
    db_type, db_host, db_port, db_user, db_pass, db_name = [config.get(key) for key in keys]

    db_urls = {
			'sqlite': f"{db_type}:///{db_name}",
			'mysql': f"{db_type}+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}",
			'postgresql': f"{db_type}://{db_user}:{db_pass}@{db_host}/{db_name}",
			'mongodb': f"{db_type}://{db_host}:{db_port}",
			'cassandra': db_host,
			'redis': f"{db_type}://{db_host}:{db_port}",
			'couchdb': f"http://{db_user}:{db_pass}@{db_host}:{db_port}",
			'dynamodb': db_host,
			'neo4j': f"bolt://{db_user}:{db_pass}@{db_host}:{db_port}"
    }

    db_url = db_urls.get(db_type)
    if db_url is None:
      raise ValueError(f"Unsupported database type: {db_type}")

    db_connections = {
			'mongodb': lambda: MongoClient(db_url)[db_name],
			'cassandra': lambda: Cluster([db_url]).connect(),
			'redis': lambda: redis.Redis.from_url(db_url),
			'couchdb': lambda: couchdb.Server(db_url)[db_name],
			'dynamodb': lambda: boto3.resource(
				'dynamodb',
				endpoint_url=config.get('db_host'),
				region_name=config.get('aws_region'),
				aws_access_key_id=config.get('aws_access_key'),
				aws_secret_access_key=config.get('aws_secret_key')
			).Table(db_name), # Table is the DynamoDB table name
			'neo4j': lambda: GraphDatabase.driver(db_url).session()
    }

    if db_type in db_connections:
      return db_connections[db_type]()
    else:
      engine = create_engine(db_url)
      SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
      return SessionLocal