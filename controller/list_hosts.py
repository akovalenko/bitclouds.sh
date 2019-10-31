import configparser
import os
import datetime
import time
import sys

config = configparser.ConfigParser()

config.read('../controller/config.ini')

from ctrldbops import find_hosts, deduct_host, get_suspended, delete_host
from orchestrator import del_server

hosts = find_hosts()
for host in hosts:
    if host['status'] == sys.argv[1]:
        print(host)

