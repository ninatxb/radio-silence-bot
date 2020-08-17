from os import environ
from flask import Flask
import rs_bot

app = Flask(__name__)

@app.route("/")
def home():
    bot.tweet_quote()
    return "tweeting a radio silence quote..."

app.run(host= "0.0.0.0", port=environ.get("PORT"))
