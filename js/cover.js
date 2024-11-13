let bg = document.getElementById("bg")
let moon = document.getElementById("moon")
let mountain = document.getElementById("mountain")
let road = document.getElementById("road")
let judul = document.getElementById("judul")
let judul2 = document.getElementById("judul2")
let btn = document.getElementById("btn")

window.addEventListener('scroll', function(){
    var value = window.scrollY;

    bg.style.top = value * 0.5 + "px";
    moon.style.left = -value * 0.5 + "px";
    mountain.style.top = -value * 0.15 + "px";
    road.style.top = value * 0.1 + "px";
    judul.style.left = -value * 2.5 + "px";
    judul2.style.left = value * 2.5 + "px";
    btn.style.left = value * 0.3 + "px"
})