// ES6 Features  

// Arrow Function
// Single line arrow function a return likhte hoy na 
// doesn't work with new keyword 
// doesn't care about this , not work wit call and bind

let fun = ()=>10;

let fun2 = ()=>{
    return 10
}

//  This keyword confusion clear , 

var javascript ={
    name : "Js",
    dev : "google",
    lib : ["vue","react","angular"],
    libprint:function () {
        var self = this;
        javascript.lib.forEach(function (params) {
            console.log(`${self.name} loves ${params}`)
        })
    }
}

javascript.libprint();

var javascript2 ={
    name : "Js",
    dev : "google",
    lib : ["vue","react","angular"],
    libprint:function () {
        javascript.lib.forEach((params) => {
            console.log(`${this.name} loves ${params}`)
        })
    }
}

javascript2.libprint();


// Truthy or flase value 
// False, null,0,undefined,"",NaN   These values are false value and all other true



// Ternary Operator or ? Symbol 

var age = 35 ;
var type ;
if (age>18){
type = "adult";
}else{
    type="Child"
}

// above program solved with ternary operator

var age2 =35;
var type2 = (age2>35 ) ? "adults":"Child";

// multiple ternary operator 

var age3 = 28;
var age3 = (age3>20) ? "adult":(age3<10) ? "child":"young";


// Array Find Method
// return single value
// When return true exit the execution
// wont't change my main array
// Has three parameter 1.CurrentValue 2.curentIndex 3.mainArray
// Also can run without parameter

var num = [1,2,3,4,5,6]

var result = num.find(function (currentValue) {
    return currentValue >4 ;
})

console.log(result)

// Multiple parameter

var num2 = [2,3,4,5,6]

var result2 = num2.find(function(currentValue,currentIndex,mainArray) {
    console.log(currentIndex)
    console.log(mainArray)
    return currentValue>4;
})

console.log(result2)


// array findindex method
// Return index
// same as find method just return true value index



// Array filter method 
// this return an array
// doesn't change main array





// array slice ,splice, concat method
// return array

// map Method 
// return a new array

var numbers = [1,2,3,4,5,6]
var resul = numbers.map((a)=> a*2);

console.log(resul)


// Reduce Method important

var red = [1,2,3,4,5,6]

var sum = red.reduce((previousValue,currentValue,curIndex,arr)=>{
return previousValue+currentValue;

},0)

console.log(sum)


// for loop , for in , for of

for (let i=0;i<=5;i++){
    console.log(i)
}

// for in object iterator

const myObj = {
    name:'js',
    estd:'1995',
    founder:'Brendan Erich'
};

for(property in myObj){
    console.log(property)
}

// for of for array , for of for index
var d = [1,2,3]
for(element of d){
    console.log(element)
}


// Important Objects methods *** 

const myObj2 = {
    name:'js',
    estd:'1995',
    founder:'Brendan Erich'
};

var keys = Object.keys(myObj2)
console.log(keys)

var values = Object.values(myObj2)
console.log(values)

var entries = Object.entries(myObj2)
console.log(entries)

// Object short shand (if value and key is same you can write like )

var x =5;
var myob3 = {
    name:"Hasan",
    x
}

// Spread operator ***

var spOp = [1,2,3,4]

var spOp2 = [...spOp,5,6,]

console.log(spOp2)

// Rest operator 
// Must assign as last parameter in function

function one(a,...rest){
    console.log(a,rest)
}

one(1,2,3,7)


// Most importing things 
// Destructuring Objects 

// Objects

const user = {
    id:221,
    name:"Hasan",
    age22:38,
    education:{
        degree:"HSC",
    }
};

// Normal destructure 
const {age22} = user;
console.log(age22)

// name as 

const {age22:yourage} = user;
console.log(yourage)

// nested object

const {education:{degree}} = user;

console.log(degree)


// default value when destructuring and name as

const {education:{degree:title} = {}} = user;

// ******* Array destructuring ********

var anumbers = [1,2,3,4,5];

var [a,b] = anumbers;

var [,c,,,d]=anumbers;

console.log(a,d)