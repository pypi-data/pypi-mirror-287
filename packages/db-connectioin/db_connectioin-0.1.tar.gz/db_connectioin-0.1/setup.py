# db_connection/setup.py
from setuptools import setup, find_packages

setup(
    name='db_connectioin',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',
        'pymongo',
        'cassandra-driver',
        'redis',
        'couchdb',
        'boto3',
        'neo4j',
        'python-dotenv',
    ],
    description='A package for handling database connections and table creation across different databases',
    author='periyanayagam',
    author_email='periyanayagam.anthonysamy@itbeezone.in',
    url='https://github.com/yourusername/db_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
