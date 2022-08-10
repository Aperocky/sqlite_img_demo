let goButton = document.getElementById("login-go");
let userIdInput = document.getElementById("login-box");

goButton.addEventListener("click", () => {
    let userId = userIdInput.value
    location.href = `/survey?userId=${userId}`;
});
