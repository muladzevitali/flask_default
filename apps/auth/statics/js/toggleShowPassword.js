const toggleShowPassword = () => {
    let currentText = document.getElementById("toggleShowPassword").innerText;
    if (currentText === 'Show') {
        document.getElementById("toggleShowPassword").innerText = 'Hide';
        document.getElementById("loginPasswordInput").type = 'text';
    } else {
        document.getElementById("toggleShowPassword").innerText = 'Show';
        document.getElementById("loginPasswordInput").type = 'password'
    }
};

document.getElementById("toggleShowPassword").addEventListener('click', toggleShowPassword);
