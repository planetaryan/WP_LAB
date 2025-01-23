function checkAns() {
    let score = 0;

    // Check answers for each question
    if (document.querySelector('input[name="q1"]:checked') && document.querySelector('input[name="q1"]:checked').nextSibling.textContent.trim() === "Donald Trump") {
        score++;
    }
    if (document.querySelector('input[name="q2"]:checked') && document.querySelector('input[name="q2"]:checked').nextSibling.textContent.trim() === "26th January") {
        score++;
    }
    if (document.querySelector('input[name="q3"]:checked') && document.querySelector('input[name="q3"]:checked').nextSibling.textContent.trim() === "Manipal Institute of Technology") {
        score++;
    }

    // Display the score
    document.getElementById("score").innerHTML = "Your score: " + score + "/3";
}
