from flask import Flask, request, render_template, abort
import time
import uuid

app = Flask(__name__)

chat = []

blask_list = []

admins = ["127.0.0.1"]


@app.route("/", methods=["GET", "POST"])
def start():
    return render_template("chat.html")


@app.route("/message", methods=["GET", "POST", "DELETE", "BAN"])
def message():
    global chat

    client_ip = request.remote_addr

    if client_ip in blask_list:
        return {"chat": [{
            "user": "Server", "time": 0, "id": 0, "ip": 0,
            "type": "post", "message": "You was bunned."
            }]}

    if request.method == "POST":
        data = request.get_json()
        print("data", data)
        data["user"] = "Fake server" if data["user"] == "Server" else data["user"]
        data["time"] = time.perf_counter()
        data["id"] = uuid.uuid1()
        data["ip"] = client_ip
        data["type"] = "post"
        chat.append(data)
        return {}
    if request.method == "GET":
        print("GET")
        i = 0
        while i < len(chat):
            mes = chat[i]
            mes["owner"] = mes["ip"] == client_ip
            if time.perf_counter() - mes["time"] >= 3:
                del chat[i]
                i -= 1
            i += 1
        return {"chat": chat, "admin": client_ip in admins}

    if request.method == "DELETE":
        if client_ip not in admins:
            return abort(403)
        data = request.get_json()
        print("delete data", data)
        data["time"] = time.perf_counter()
        data["id"] = uuid.uuid1()
        data["ip"] = client_ip
        data["type"] = "delete"
        chat.append(data)
        return {}
    if request.method == "BAN":
        if client_ip not in admins:
            return abort(403)
        data = request.get_json()
        
        if client_ip == data["ban_ip"]:
            return abort(409)

        if client_ip in blask_list:
            return abort(400)

        print("bun user", data)
        blask_list.append(data["ban_ip"])

        print("data", data)
        data["user"] = "Server"
        data["message"] = f"Ip {data['ban_ip']} was banned."
        data["time"] = time.perf_counter()
        data["id"] = uuid.uuid1()
        data["ip"] = client_ip
        data["type"] = "post"
        chat.append(data)

        return {}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    # app.run(debug=True)