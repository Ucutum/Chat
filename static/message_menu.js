const menu = document.getElementById("message_menu")

var menu_left = 105
var menu_target_left = 105

menu.style = "left: " + String(menu_left) + "%;"

function messangeMenu(message_id, user_ip) {
    if (menu_target_left == 105) {
        menu_target_left = 70
        document.getElementById("message_menu_message").innerHTML = "Id: " + String(message_id)
        document.getElementById("delete_message_button").setAttribute("onclick", "deleteMessage('{}')".replace("{}", message_id))
        document.getElementById("ban_user_button").setAttribute("onclick", "banUser('{}')".replace("{}", user_ip))
    } else {
        menu_target_left = 105
    }
    setTimeout(resizeMenu, 10)
}

function resizeMenu() {
    if (menu_target_left - menu_left > 1) {
        menu_left += 0.5
    } else if (menu_left - menu_target_left > 1) {
        menu_left -= 0.5
    } else {
        return
    }
    menu.style = "left: " + String(menu_left) + "%;"
    setTimeout(resizeMenu, 5)
}