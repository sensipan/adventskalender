from flask import Flask, render_template  
app = Flask(__name__)   # Flask constructor
from datetime import datetime


  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello():
    today = datetime.today().date().day
    song = today%13 + 1
    info = {"tag": today, "song": f"../static/audio/{song}.mp3"}
    return render_template("index.html", info=info)
  
if __name__=='__main__': 
   app.run()