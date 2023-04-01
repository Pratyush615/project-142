from flask import Flask,jsonify,request
import csv
from storage import all_articles,liked_articles,not_liked_articles
from demographics_filtering import output
from content_filtering import get_reccomandations



all_articles = []

with open('articles.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-article")
def liked_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/not-liked-article")
def not_liked_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

if __name__ == "__main__":
  app.run()