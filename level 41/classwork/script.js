function dosomething(){
    console.log("hello world");
}

dosomething()

function sumthree(a, b, c) {
    console.log(a + b + c)
  }
  
sumthree()

function greet(name = "Guest", message = "Welcome!") {
    console.log(`${message}, ${name}`);
}

greet()
