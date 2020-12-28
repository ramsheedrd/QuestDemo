var a = 10 //number
var b = "15" //string
console.log(this)
var d = {
         firstname:"jestin",
         lastname:'joseph',
         getFullname: function(){
            
             setInterval(() => {
                 console.log(this.firstname)
             }, 2000)

             return this.firstname +" "+this.lastname
         }
        } //object

console.log(d.getFullname())
















// console.log(typeof b)


// console.log(b.slice(0, 5))
// console.log(b.indexOf("w"))
// console.log(b.search(/\d/))
// console.log(b.replace("5", ""))
// console.log(b.split(" "))
// console.log(typeof a.toString())

// c.push(5)
// c.unshift(0)

// c.pop()
// c.shift()

// delete c[2]
// c.splice(start = 2,deleteCount =  1)
// console.log(c)

// c.join("-")
// c.indexOf(3)
// c.slice(0,2)

var digits = [1,2,3,4] //Array


// function sqr(value){
//     console.log(value*value)
// }
// digits.forEach(sqr)

// digits.forEach(function(value){
//     console.log(value*value)
// }{

// digits.forEach((value) => console.log(value * value))

// var new_arr = digits.map(function(value){
//     return value*value
// })

// var new_arr = digits.filter((value) => value < 3 )
// console.log(new_arr)










