const car1 = {
    brand: "Toyota",
    model: "Corolla",
    year: 2020
  };
  
  const car2 = {
    brand: "Ford",
    model: "Mustang",
    year: 2022
  };
  
  const car3 = {
    brand: "BMW",
    model: "X5",
    year: 2021
  };
  
  console.log(car1, car2, car3);
  
  function Car(brand, model, horsePower) {
    this.brand = brand;
    this.model = model;
    this.horsePower = horsePower;
  
    this.increaseHorsePower = function () {
      this.horsePower += 50;
      return this.horsePower;
    };
  }
  
 
  const car = new Car("Toyota", "Supra", 300);
  console.log(car1.horsePower);
  console.log(car1.increaseHorsePower()); 
  
  const fruits = ["apple", "banana", "cherry", "orange", "grape"];
  const colors = new Array("red", "blue", "green", "yellow", "purple");

console.log("Fruits:");
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

console.log("Colors:");
for (let i = 0; i < colors.length; i++) {
  console.log(colors[i]);
}

console.log(fruits[0]);
console.log(colors.slice(0, 3))

// ჯავა სკრიპტში სინამდვილეში არ მუშაობს, და იმისგამო არ უნდა გამოვიყენიოთ რადგან ობიექტის ნამდვილ ტვისებებს არ შეესაბამება