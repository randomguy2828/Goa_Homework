var fruits = ["apple", "Peach", "Banana"];

for (var i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

var person = { name: "nika", age: 17, city: "tbilisi" };

for (var key in person) {
    console.log(key + ": " + person[key]);
}

var nam = "Nika";
var age = 25;

console.log("My name is " + nam + " and I am " + age + " years old.");

var numbers = [1, 2, 3, 4, 5];

numbers.forEach(function(num) {
    console.log("Number: " + num);
});

var multiply = function(a, b) {
    return a * b;
};

console.log(multiply(5, 3)); 

const surename = "erekle";
const age = 25;

const person = { surename, age }; 

console.log(person);

const propertyName = "age";
const person = {
  name: "daviti",
  [propertyName]: 19
};

console.log(person.age); 