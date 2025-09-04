from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

users={

}

chats={

}


@app.route("/", methods= ["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        birth = request.form["birth"]
        gender = request.form["gender"]
    
        user_id = len(users) +1
        users[user_id]= {
            "name" : name,
            "surname" : surname,
            "birth" : birth,
            "gender" : gender,
        }
        chats[user_id] = []
        return redirect(url_for("match",user_id=user_id))
    return render_template("index.html")

@app.route("/match/<int:user_id>", methods=["GET", "POST"])
def match(user_id):
    if request.method == "POST":
        match = random.choice([True, False])
        if match:
            return redirect(url_for("chat", user_id=user_id))
        else:
            return render_template("match.html",user_id=user_id, error= "Ni matcha 😂lol")
    return render_template("match.html", user_id=user_id)

@app.route("/chat/<int:user_id>", methods=["GET", "POST"])
def chat(user_id):
    if request.method == ["POST"]:
        msg= request.form["msg"]

        responses=[
            "Haha ja res😂",
            "Nej se hecaš? 😏",
            "Hmm, mogoče si ti pa res pravi...",
            "Si že slišal za Rick Astleyja?",
            "Hej Kako gre tvoj dan?",
            
        ]
        reply= random.choice(responses)

        chats[user_id].append({"user": msg, "bot": reply})

        if random.randint(1,6) == 3:
            return(url_for("rickroll"))
        return render_template("chat.html",user_id=user_id, messages= chats[user_id])
    return render_template("chat.html",user_id=user_id, messages= chats[user_id])

@app.route("/rickroll")
def rickroll():
    return render_template("rickroll.html")



if __name__ == "__main__":
    app.run(debug=True)