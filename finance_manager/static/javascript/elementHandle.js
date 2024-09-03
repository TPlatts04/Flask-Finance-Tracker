function copyClipboard() {
    // Gets the text from the span element
    let copyDiscord = document.getElementById('discord_username').innerText;
    // Copy text to the clipboard
    navigator.clipboard.writeText(copyDiscord).then(function() {
        alert("Copied to clipboard!");
    }).catch(function(error) {
        console.error("Error copying text: ", error);
    })
}

function slideArrowLeft() {
    const formHolder = document.getElementById('form-holder')
    const createHolder = document.getElementById('create-holder')
    
    formHolder.style.transform = 'TranslateX(-150%)'
    formHolder.style.transition = 'all 2s'
    createHolder.style.transform = 'TranslateX(-57%)'
    createHolder.style.transition = 'all 2s'
}

function slideArrowRight() {
    const formHolder = document.getElementById('form-holder')
    const createHolder = document.getElementById('create-holder') 

    formHolder.style.transform = 'TranslateX(59%)'
    formHolder.style.transition = 'all 2s'
    createHolder.style.transform = 'TranslateX(150%)'
    createHolder.style.transition = 'all 2s'
}