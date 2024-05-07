var countDownDate = new Date("May 7, 2024 16:00:00 UTC").getTime();

var x = setInterval(function () {

    var now = new Date().getTime();
    var distance = countDownDate - now;

    // var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("countdown").innerHTML = "Live: " + hours + "h "
        + minutes + "m " + seconds + "s ";

    if (distance < 0) {
        clearInterval(x);
        document.getElementById("countdown").innerHTML = "En directo";
    }
}, 1000);