const toggleShowPassword = () => {
    let currentText = document.getElementById("toggleShowPassword").innerText;
    if (currentText === 'ჩვენება') {
        document.getElementById("toggleShowPassword").innerText = 'დამალვა';
        document.getElementById("loginPasswordInput").type = 'text';
    } else {
        document.getElementById("toggleShowPassword").innerText = 'ჩვენება';
        document.getElementById("loginPasswordInput").type = 'password'
    }
};

document.getElementById("toggleShowPassword").addEventListener('click', toggleShowPassword);
