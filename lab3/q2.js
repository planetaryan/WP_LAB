function wishUser() {
    const hour = new Date().getHours();
    let greeting = "";

    if (hour < 12) {
        greeting = "Good Morning!";
    } else if (hour < 18) {
        greeting = "Good Afternoon!";
    } else {
        greeting = "Good Evening!";
    }
    alert(greeting); // Show a dialog box
}

function updateClock() {
    const time = new Date().toLocaleTimeString();
    document.getElementById('clock').textContent = time;
}

wishUser();  // Call wish function when page loads
setInterval(updateClock, 1000);  // Update the clock every second
