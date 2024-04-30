#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    logs = client.logs.nginx

    total_logs = logs.count_documents({})

    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs.count_documents({"method": method})
        print("    method {}: {}".format(method, count))

    status_check = logs.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))
