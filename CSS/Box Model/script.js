var close = document.querySelectorAll(".close")

close.forEach((el)=>{
    el.addEventListener('click', function(event){
    event.target.parentNode.style.display = "none"
})
})


var create = document.getElementById("create")

create.addEventListener('click', function(){
    var div = document.createElement('div')

    var txt = document.getElementById('txt')
    div.innerText = txt.value
    div.classList.add("alert")
    div.addEventListener('click', function(){
        div.remove()
    })

    setTimeout(function(){
        div.remove()
    }, 4000)

    wrapper = document.querySelector(".alert-wrapper")
    wrapper.appendChild(div)
})