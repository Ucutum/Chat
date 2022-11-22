user_name = getCookie("user_name")

if (user_name == undefined) {
    setCookie("user_name", "Guest")
    user_name = getCookie("user_name")
}

function sendMessage(){

    var line = document.getElementById("message_line").value

    var send_data = {user: user_name, message: line}

    var data = JSON.stringify(send_data)

    document.getElementById("message_line").value = ""

    const xhr = new XMLHttpRequest()

    xhr.open("POST", "/message")
    xhr.setRequestHeader("Content-Type", "application/json")

    xhr.onload = () => {
    }

    xhr.send(data)

    return false
}