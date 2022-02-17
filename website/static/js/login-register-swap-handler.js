const loginPanel = document.getElementById('login-modal');
const registerPanel = document.getElementById('register-modal');

function switchPanel(panel) {
    if (panel === "register") {
        loginPanel.style.display = "none";
        registerPanel.style.display = "block";
    } else if (panel === "login") {
        registerPanel.style.display = "none";
        loginPanel.style.display = "block";
    }
}