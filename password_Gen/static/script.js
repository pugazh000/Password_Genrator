document.getElementById('generateBtn').addEventListener('click', function() {
    const apiUrl = "https://jmyevuvhma.execute-api.ap-southeast-1.amazonaws.com/dev/generate";
    
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            let password = data.password;
            let passwordDisplay = document.getElementById('generatedPassword');
            passwordDisplay.textContent = password;
        })
        .catch(error => console.error("Error fetching password:", error));
});
