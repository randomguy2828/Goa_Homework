    let button1 = document.getElementById("button1");
    let button2 = document.getElementById("button2");
    let button3 = document.getElementById("button3");

    button1.addEventListener("click", function(event) {
        event.preventDefault
        button1.style.backgroundColor = "cyan";
        button1.textContent = "anthem";
    });

    button2.addEventListener("click", function(event) {
        event.preventDefault
        button2.style.backgroundColor = "green";
        button2.textContent = "zwei";
    });

    button3.addEventListener("click", function(event) {
        event.preventDefault
        button3.style.backgroundColor = "purple";
        button3.textContent = "Hello earth";
    });

    function changeText() {
        let button4 = document.getElementById("button4"); 
        button4.innerHTML = "Hello world"; 
        button4.style.fontSize = "20px";
    }


    function changeFont() {
        let button5 = document.getElementById("button5"); 
        button5.innerHTML = "Terraria"; 
        button5.style.fontSize = "27px"; 
    }

    let fruits = ["apple", "peach", "berry"];
    fruits.push("Dragonfruit");
    console.log(fruits);

    let cars = ["BMW", "Toyota", "mercedes", "Ford"];
    cars.pop(); 
    cars.push("Tesla");
    console.log(cars);

    let items = ["GTA", "Minecraft", "God of war", "cyberpunk"];

    items.pop();
    items.shift();
    console.log(items);