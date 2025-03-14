let grade = 93;

if (grade >= 90 && score <= 100){
    console.log("A");
} else if (grade >= 80 && score < 90){
    console.log("B");
} else if (grade >= 70 && score < 80){
    console.log("C");
} else if (grade >= 60 && score < 70){
    console.log("D");
} else{
    console.log("F");
}

let age = 15;

if(age < 13){
    console.log("you are a kid")
} else if(age > 13 && age < 18){
    console.log("you are not adult yet")
} else if(age > 18){
    console.log("you are adult")
} 

for(let i = 0; i < 100; i++){
    console.log(i)
}

for(let i = 50; i < 100; i += 2){
    console.log(i)
}