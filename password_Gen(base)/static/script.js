document.getElementById('generateBtn').addEventListener('click', function() {
    const length = parseInt(document.getElementById('length').value);
    const includeUpper = document.getElementById('includeUpper').checked;
    const includeNumbers = document.getElementById('includeNumbers').checked;
    const includeSymbols = document.getElementById('includeSymbols').checked;

    const lowerCaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const upperCaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numbers = '0123456789';
    const symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?';

    let characters = lowerCaseChars;
    if (includeUpper) characters += upperCaseChars;
    if (includeNumbers) characters += numbers;
    if (includeSymbols) characters += symbols;

    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters[randomIndex];
    }

    // Glitch Typing Effect
    let passwordDisplay = document.getElementById('generatedPassword');
    passwordDisplay.textContent = "";
    let i = 0;
    function typeGlitch() {
        if (i < password.length) {
            passwordDisplay.textContent += password.charAt(i);
            i++;
            setTimeout(typeGlitch, 50);
        }
    }
    typeGlitch();
});
