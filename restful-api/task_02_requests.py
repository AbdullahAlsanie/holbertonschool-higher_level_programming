#!/usr/bin/python3
"""
fetch posts from JSONPlaceholder using requests.get().
"""


import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
    for post in posts:
        print(post["title"])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        posts_data = []
        for post in posts:
            record = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            posts_data.append(record)
        
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
