// const child = document.getElementById("div");

// let left = 0;
// let y = 0;
// let direction = "down"; 

// const moveCounterClockwise = setInterval(function() {
//     if (direction == "down") {
//         y++;
//         if (y == 400) { 
//             direction = "right";
//         }
//     } else if (direction == "right") {
//         left++;
//         if (left == 400) { 
//             direction = "up";
//         }
//     } else if (direction == "up") {
//         y--;
//         if (y == 0) {
//             direction = "left";
//         }
//     } else {
//         left--;
//         if (left == 0 && y == 0) { 
//             clearInterval(moveCounterClockwise);
//         }
//     }

//     child.style.left = left + 'px';
//     child.style.top = y + 'px';
// }, 10);

const child = document.getElementById("div");

let left = 0;
let y = 0;

document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowDown") {
        y += 10; 
    } else if (event.key === "ArrowRight") {
        left += 10;
    } else if (event.key === "ArrowUp") {
        y -= 10; 
    } else if (event.key === "ArrowLeft") {
        left -= 10; 
    }

    child.style.left = left + "px";
    child.style.top = y + "px";
});