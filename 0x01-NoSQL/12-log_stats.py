#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def count_documents(collection, query={}):
    """Counts the number of documents based on a given query"""
    return collection.count_documents(query)


def main():
    """Print logs as required"""
    client = MongoClient()
    db = client.logs
    nginx_collection = db.nginx

    total_logs = count_documents(nginx_collection)
    print(f"{total_logs} logs")

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = count_documents(nginx_collection, {"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_check_count = count_documents(
        nginx_collection,
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    main()
