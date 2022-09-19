

from pickle import TRUE

from flask import Flask , render_template, request
import prediction as pr


app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    return render_template("index.html")
@app.route("/home", methods=['POST','GET'])
def home():
    if request.method == 'POST':
        title=request.form['title']
        title_src=request.form['source']
        str_pr,str_pro=pr.detecting_fake_news(title)
        str_pro = int(100*str_pro)
        print(str_pr,str_pro)
        if str(str_pr)=="True":
            return render_template("approved.html", prediction = str_pr, score = str_pro, title_html = title , source_html = title_src)
        else:
            return render_template("declined.html", prediction = str_pr, score = str_pro, title_html = title , source_html = title_src)
        
        

    else:
        return render_template("home.html")
@app.route("/loading", methods=['POST', 'GET'])
def loading():
    return render_template("load1.html"), {"Refresh": "4; url = /home "}
if __name__ == "__main__":
    app.run(debug=TRUE)
