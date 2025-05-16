document.getElementById("parent").addEventListener("click", function() {
    alert("parent div");
});

document.getElementById("child").addEventListener("click", function() {
    alert("child div");
 });

//  უბრალოდ True უნდა მიუწერო ფუნცქციას მესამე ოპტიმალურ ჩასაწერში და გამოვა Capturing

const img = document.getElementById("img");
const next = document.getElementById("next");
const prev = document.getElementById("prev");
let i = 0;
const images = ["./image1.jpg", "./image2.jpg", "./image3.jpg", "./image4.jpg", "./image5.jpg"];

next.addEventListener("click", function(){
    i++;
    if (i >= images.length) {
        i = 0;
    }
    img.src = images[i];
});

prev.addEventListener("click", function(){
    i--;
    if (i <= -1) {
        i = images.length - 1;
    }
    img.src = images[i];
});