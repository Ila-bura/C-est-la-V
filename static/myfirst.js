// Closing Alert Messages

setTimeout(function () {
    let messages = document.getElementById("msg");
    // Check if the element with ID "msg" exists
    if (messages) {
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }
}, 2500);


// Countdown
document.addEventListener("DOMContentLoaded", function () {
    var countDownDate = new Date("Jan 01, 2024 00:00:00").getTime();
    var x = setInterval(function () {
        var now = new Date().getTime();
        var distance = countDownDate - now;
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor(
            (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
        );
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        document.getElementById("days").innerHTML = days;
        document.getElementById("hours").innerHTML = hours;
        document.getElementById("minutes").innerHTML = minutes;
        document.getElementById("seconds").innerHTML = seconds;
        if (distance < 0) {
            clearInterval(x);
            document.getElementById("days").innerHTML = "00";
            document.getElementById("hours").innerHTML = "00";
            document.getElementById("minutes").innerHTML = "00";
            document.getElementById("seconds").innerHTML = "00";
            document.getElementById("veg").innerHTML =
                "Veganuary 2024 is here!";
        }
    }, 1000);
});