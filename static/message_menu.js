const menu = document.getElementById("message_menu")

var menu_left = 105
var menu_target_left = 105

menu.style = "left: " + String(menu_left) + "%;"

function messangeMenu() {
    if (menu_target_left == 105) {
        menu_target_left = 70
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