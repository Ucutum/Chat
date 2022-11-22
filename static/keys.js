document.getElementById("message_line").addEventListener("keydown", function(e){
    if (e.keyCode == 13){
        return sendMessage()
    }    
})