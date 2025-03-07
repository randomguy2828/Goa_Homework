const submit = document.getElementById("submit");
const form = document.getElementById("form");

submit.addEventListener('click', function(event){
    event.preventDefault();

    // const name = document.getElementById("name");
    // const email = document.getElementById("email");
    // const pass = document.getElementById("pass");
    const name = form.elements.name;
    const email = form.elements.email;
    const pass = form.elements.pass;

    // console.log(name.value);
    // console.log(email.value);
    // console.log(pass.value);
    console.log(name.value);
    console.log(email.value);
    console.log(pass.value);
})
