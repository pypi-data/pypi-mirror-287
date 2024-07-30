import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import redis
import couchdb
import boto3
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable, AuthError

def create_db_connection(config):
  # Retrieve database configuration from environment variables
  keys = ['db_type', 'db_host', 'db_port', 'db_user', 'db_pass', 'db_name']
  db_type, db_host, db_port, db_user, db_pass, db_name = [config.get(key) for key in keys]

  db_urls = {
    'sqlite': f"sqlite:///{db_name}",
    'mysql': f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}",
    'postgresql': f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}",
    'mongodb': f"mongodb://{db_host}:{db_port}",
    'cassandra': db_host,
    'redis': f"redis://{db_user}:{db_pass}@{db_host}:{db_port}",
    'couchdb': f"http://{db_user}:{db_pass}@{db_host}:{db_port}",
    'dynamodb': f"https://dynamodb.{os.getenv('AWS_REGION')}.amazonaws.com",
    'neo4j': f"bolt://{db_user}:{db_pass}@{db_host}:{db_port}"
  }

  db_connections = {
    'mongodb': lambda: MongoClient(db_urls['mongodb'])[db_name],
    'cassandra': lambda: Cluster([db_host], auth_provider=PlainTextAuthProvider(username=db_user, password=db_pass)).connect(),
    'redis': lambda: redis.Redis.from_url(db_urls['redis']),
    'couchdb': lambda: couchdb.Server(db_urls['couchdb'])[db_name],
    'dynamodb': lambda: boto3.resource(
      'dynamodb',
      endpoint_url=db_urls['dynamodb'],
      region_name=os.getenv('AWS_REGION'),
      aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
      aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
    ).Table(db_name),
    'neo4j': lambda: GraphDatabase.driver(db_urls['neo4j'], auth=(db_user, db_pass)).session()
  }

  def test_connection(db_type, db_connection):
    tests = {
      'mongodb': lambda: db_connection.list_collection_names(),
      'redis': lambda: db_connection.ping(),
      'couchdb': lambda: db_connection.info(),
      'dynamodb': lambda: db_connection.scan(TableName=db_name),
      'neo4j': lambda: db_connection.run("RETURN 1")
    }
    test_func = tests.get(db_type)
    if test_func:
        test_func()
    print(f"Connected to {db_type} database successfully.")

  try:
    if db_type in db_connections:
      db_connection = db_connections[db_type]()
      test_connection(db_type, db_connection)
      return db_connection
    else:
      engine = create_engine(db_urls.get(db_type))
      SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
      with engine.connect() as connection:
        print(f"Connected to {db_type} database successfully.")
      return SessionLocal
  except (OperationalError, ServerSelectionTimeoutError, OperationFailure, AuthError,
        redis.AuthenticationError, couchdb.http.Unauthorized, ServiceUnavailable) as e:
      print(f"Failed to connect to {db_type} database: {e}")
      raise
  except Exception as e:
      print(f"General Error: {e}")
      raise

      
