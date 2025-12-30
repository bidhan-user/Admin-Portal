from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_users = [
    {"name": "Alice", "role": "Admin"},
    {"name": "Bob", "role": "Guest"}
]

@app.route("/")
def home():
    return render_template("index.html", users=all_users)

@app.route("/add", methods=["POST"])
def add_user():
    name = request.form.get("name")
    role = request.form.get("role")
    
    if name and role:
        all_users.append({"name": name, "role": role})
    return redirect(url_for("home"))

@app.route("/delete/<name>", methods=["POST"])
def delete_user(name):
    global all_users

    all_users = [person for person in all_users if person["name"] != name]
    return redirect(url_for("home"))

@app.route("/update/<name>", methods=["POST"])
def update_user(name):
    new_role = request.form.get("new_role")
    
    for person in all_users:
        if person["name"] == name:
            person["role"] = new_role 
            break 
            
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)