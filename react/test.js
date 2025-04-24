const macbook={
    display:55,
    price:442,
    color:"red"
}

//add
const obj={...macbook,region:"india"}

//remove
const {color,...obj1}=macbook

//update
const obj2={...macbook,price:44}

console.log(obj)