var form = document.getElementById("regform")
var email = document.getElementById("email")
var err = document.querySelector(".err")

form.addEventListener('submit', function(event){
    if(!email.validity.valid){
        showError()
        event.preventDefault()
    }
})

email.addEventListener('input', function(){
    if(!email.validity.valid){
        showError()
    }
    else{
        err.innerHTML = ""
    }
})


function showError(){

    if(email.validity.valueMissing){
        err.innerHTML = "*Email Required"
    }

    if(email.validity.typeMismatch){
        err.innerHTML = "Invalid Format"
    }

}