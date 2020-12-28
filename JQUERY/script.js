$(document).ready(function(){

    function getMovie(name){
        console.log(name)
        $.get(`http://www.omdbapi.com/?t=${name}&apikey=7d5a3cd7`, function(res){
            console.log(res)
            $('body').append(`<h2>${res.Title}</h2>`)
            $('body').append(`<h3>${res.Genre}</h3>`)
            $('body').append(`<h4>${res.Director}</h4>`)
            $('body').append(`<img src='${res.Poster}'>`)



        })
    }

    $('button').click(function(){
        let name = $('#name').val()
        getMovie(name)
    })
})


// 7d5a3cd7