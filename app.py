from flask import Flask,request
import telegram
from settings import TOKEN

app=Flask(__name__)

@app.route('/',methods=["POST"])
def home():
    bot=telegram.Bot(TOKEN)

    data=request.get_json()
    print(data)