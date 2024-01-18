from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/success/<name>")
def success(name):
    return f"<h1>welcome {name}</h1>"

@app.route("/login",methods=['POST',"GET"])
def login():
    if request.method=="POST":
        name1=request.form.get("name")
        return redirect(url_for("success",name=name1))
    else:
        name1=request.args.get("name")
        return redirect(url_for("success",name=name1))
if __name__=="__main__":
    app.run(debug=True)