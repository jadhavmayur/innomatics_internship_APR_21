from flask import Flask, render_template, request,session
from flask_session.__init__ import Session 

app = Flask(__name__)
app.config["SECRETE_KEY"]="some_random"
app.config["SESSION_TYPE"]="filesystem"
app.config["SESSION_PERMANENT"]=False

Session(app)

@app.route('/',methods=["POST","GET"])
def index():
    if session.get("notes") is None:
        session["notes"]=[]
    
    if request.method =="POST":
        note=request.form.get("note")
        if(note != ""):
            session["notes"].append(note)
    return render_template("home.html", notes=session['notes'])
    

app.add_url_rule("/",'index',index)

if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1",threaded=True)