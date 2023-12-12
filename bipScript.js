let beepSound = new Audio('beep.mp3');

document.getElementById('beepBtn').style.backgroundColor = 'white';
document.getElementById('beepBtn').disabled = true;

document.getElementById('calculateBtn').addEventListener('click', function() {
    let pace = document.getElementById('paceInput').value.split('.');
    let paceMin = parseInt(pace[0]);
    let paceSec = parseInt(pace[1]);
    let distance = parseInt(document.getElementById('coneDistanceInput').value);

    let totalMin = paceMin + paceSec / 60;
    let speed = 60 / totalMin;
    document.getElementById('speedDisplay').innerText = `Velocità (km/h): ${speed.toFixed(2)}`;

    let totalSec = paceMin * 60 + paceSec;
    let timePerKm = totalSec / 1000;
    let beepTime = timePerKm * distance;
    document.getElementById('beepTimeDisplay').innerText = `Tempo per 'bip' ogni ${distance} metri: ${beepTime.toFixed(2)} secondi`;

    window.beepInterval = beepTime * 1000;
    
    let beepButton = document.getElementById('beepBtn');
    beepButton.style.backgroundColor = 'green';
    beepButton.disabled = false;
});

document.getElementById('beepBtn').addEventListener('click', function() {
    if (window.beepTimer) {
        clearInterval(window.beepTimer);
        window.beepTimer = null;
        this.innerText = 'AVVIA';
        this.style.backgroundColor  = 'green';
    } else {
        window.beepTimer = setInterval(playBeep, window.beepInterval);
        this.innerText = 'FERMA';
        this.style.backgroundColor  = 'red';
    }
});


function playBeep() {
    beepSound.play();
}
