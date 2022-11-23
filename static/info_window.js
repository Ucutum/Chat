function deleteMessage(message_id) {
    var send_data = {delete_id: message_id}

    console.log("DEL")

    var data = JSON.stringify(send_data)

    const xhr = new XMLHttpRequest()

    xhr.open("DELETE", "/message")
    xhr.setRequestHeader("Content-Type", "application/json")

    xhr.onload = () => {
    }

    xhr.send(data)
}

function banUser(user_ip) {
    var send_data = {ban_ip: user_ip}

    var data = JSON.stringify(send_data)

    const xhr = new XMLHttpRequest()

    xhr.open("BAN", "/message")
    xhr.setRequestHeader("Content-Type", "application/json")

    xhr.onload = () => {
        var status = xhr.status

        if (status == 409) {
            alert("You can't ban yourself.")
        }
    }

    xhr.send(data)
}