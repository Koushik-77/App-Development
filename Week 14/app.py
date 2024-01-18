from flask import render_template,redirect,request,url_for,Flask

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

database={"saketh":"1234","ashrith":"12345","stayak":"0987"}

@app.route("/form_login",methods=["post","get"])
def home():
    if request.method=="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        if name not in database:
            return render_template("login.html",info="Enter correct username")
        else:
            if database[name]!=password:
                return render_template("login.html",info="Enter correct Password")
            else:
                return render_template("home.html",name=name)
    else:
        return render_template("login.html",info="Enter valid data")
    
if __name__=="__main__":
    app.run(debug=True)    