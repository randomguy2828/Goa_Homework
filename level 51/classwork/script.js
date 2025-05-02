// const div = document.getElementById("div");
// let x = 0;
// let y = 0;

// const moveRight = setInterval(() => {
//     x += 5;
//     div.style.left = `${x}px`;

//     if (x === 400) {
//         clearInterval(moveRight);

//         const moveDown = setInterval(() => {
//             y += 5;
//             div.style.top = `${y}px`;

//             if (y === 400) {
//                 clearInterval(moveDown);

//                 const moveLeft = setInterval(() => {
//                     x -= 5;
//                     div.style.left = `${x}px`;

//                     if (x === 0) {
//                         clearInterval(moveLeft);

//                         const moveUp = setInterval(() => {
//                             y -= 5;
//                             div.style.top = `${y}px`;

//                             if (y === 0) {
//                                 clearInterval(moveUp);
//                             }
//                         }, 20);
//                     }
//                 }, 20);
//             }
//         }, 20);
//     }
// }, 20);

const child = document.getElementById("div");

let x = 0;
let y = 0;
let direction = "Right";

const move = setInterval(function() {
    if (direction === "Right") {
        x++;
        if (x === 400) {
            direction = "Bottom";
        }
    } else if (direction === "Bottom") {
        y++;
        if (y === 400) {
            direction = "Left";
        }
    } else if (direction === "Left") {
        x--;
        if (x === 0) {
            direction = "Top";
        }
    } else {
        y--;
        if (y === 0) {
            direction = "Right";
        }
    }
    child.style.left = `${x}px`;
    child.style.top = `${y}px`;
}, 1);