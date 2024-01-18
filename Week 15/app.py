from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

def load_questions():
    questions={}
    with open ("questions.txt") as file:
        for i in file:
            question,answer=i.split("|||")
            questions[question]=answer
    return questions
questions=load_questions()

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/ask",methods=["POST","GET"])
def ask():
    if request.method=="POST":
        question=request.form.get("question")
        if question in questions:
            return render_template("chatbot.html",user_question=question,answer=questions[question])
        else:
            return render_template("chatbot.html",user_question=question,answer="Sorry i don't know the answer")
if __name__=="__main__":
    app.run(debug=True)