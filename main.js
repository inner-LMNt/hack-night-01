function sendWord(form) {
    var word = form.inputbox.value;
    alert(word);
}
window.addEventListener("DOMContentLoaded", () => {
    let button = document.querySelector("#hello");
    const websocket = new WebSocket("ws://localhost:8001/");
    websocket.onclose = () => {
        console.log("closed")
    }
    button.onclick = () => {
        let value = document.querySelector("#input").value;
        console.log(value);
        websocket.send(value);
    }
});
