function containsObject(obj, list) {
    var i;
    for (i = 0; i < list.length; i++) {
        if (list[i].id == obj.id) {
            return true;
        }
    }

    return false;
}


var is_working = true;

var chat = []

const div = document.getElementById("server_input")

const message_html = `<div {{ is_owner }} id="{{ MessageId }}" class="message">
<div inline class="message_content">
    <p class="message_user_text">{{ User }}</p>
    <hr class="message_hr">
    <p class="message_text">{{ Message }}</p>
</div>
<button type="button" inline class="open_message_menu_button" onclick="messangeMenu('{{ MessageId }}', '{{ UserIp }}')"></button>
</div>`

const admin_message_html = `<div {{ is_owner }} id="{{ MessageId }}" class="message">
<div inline class="message_content">
    <p inline class="message_user_text">{{ User }}</p>
    <p inline class="message_user_ip">Ip: {{ UserIp }}</p>
    <button type="button" class="delete_message_button" onclick="deleteMessage('{{ MessageId }}')">Delete message</button>
    <button type="button" class="ban_user_button" onclick="bunUser('{{ UserIp }}')">Ban user</button>
    <hr class="message_hr">
    <p class="message_text">{{ Message }}</p>
</div>
<button type="button" inline class="open_message_menu_button" onclick="messangeMenu('{{ MessageId }}', '{{ UserIp }}')"></button>
</div>`

function GetJSON(){
    var xhr = new XMLHttpRequest()
    xhr.open("GET", "/message", true)
    xhr.responseType = "json"
    xhr.onload = function() {
        var status = xhr.status

        data_chat = this.response.chat

        is_admin = this.response.admin

        for (var i = 0; i < data_chat.length; i++)
        {
            if (!containsObject(data_chat[i], chat))
            {
                if (data_chat[i].type == "post") {

                    var scrollBottom = div.scrollTop - div.scrollHeight + div.clientHeight
                    
                    var new_message_div

                    // if (is_admin) {
                    //     new_message_div = admin_message_html.replace("{{ UserIp }}",
                    //     data_chat[i].ip).replace("{{ MessageId }}", data_chat[i].id)
                    // } else {
                    new_message_div = message_html
                    // }

                    new_message_div = new_message_div.replace("{{ User }}",
                    data_chat[i].user).replace("{{ Message }}",
                    data_chat[i].message).replace("{{ MessageId }}",
                    data_chat[i].id).replace("{{ MessageId }}",
                    data_chat[i].id).replace("{{ UserIp }}",
                    data_chat[i].ip)
                    
                    if (data_chat[i].owner) {
                        new_message_div = new_message_div.replace("{{ is_owner }}", "is_owner")
                    } else {
                        new_message_div = new_message_div.replace("{{ is_owner }}", "")
                    }

                    chat.push(data_chat[i])
                    div.innerHTML = div.innerHTML + new_message_div
                    
                    
                    if (scrollBottom == 0)
                    {
                        div.scrollTo(0, div.scrollHeight)
                    }
                } else if (data_chat[i].type == "delete") {
                    var mes_div = document.getElementById(data_chat[i].delete_id)
                    if (mes_div)
                    {
                        div.removeChild(mes_div)
                    }
                    chat.push(data_chat[i])
                }
                else {
                    console.log("eslse")
                }
            }
        }
    }
    xhr.send()

    if (is_working){
        setTimeout(GetJSON, 100)
    }
}


window.onbeforeunload = function() {
    is_working = false
}


setTimeout(GetJSON, 100)