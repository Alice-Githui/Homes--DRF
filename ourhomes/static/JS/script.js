let quantity=document.getElementById('quantity').value
let capacity=document.getElementById('currentcapacity')
// set the default attribute value of disabled to the add button
document.querySelector(".plus-btn").setAttribute("disabled", "disabled");

// taking value to increment decrement input value
var valueCount

// minus button
document.querySelector('.minus-btn').addEventListener('click', function(){
    // get value of input
    valueCount=document.getElementById("quantity").value;

    // input value decrement
    valueCount--;

    // storing in localstorage
    let valueCount_serialized=JSON.stringify(valueCount)
    localStorage.setItem("valueCount", valueCount_serialized)
    console.log(valueCount_serialized)


    // set decrement input value
    document.getElementById("quantity").value=valueCount_serialized   

    if(valueCount < quantity){
        document.querySelector(".plus-btn").removeAttribute("disabled")
        document.querySelector(".plus-btn").classList.remove("disabled")
    }
    capacity.innerHTML=localStorage.getItem('valueCount')
})

// plus button
document.querySelector('.plus-btn').addEventListener('click', function(){
    // get value of input
    valueCount=document.getElementById("quantity").value;

    // input value decrement
    valueCount++;

    // storing in localstorage
    let valueCount_serialized=JSON.stringify(valueCount)
    localStorage.setItem("valueCount", valueCount_serialized)
    console.log(valueCount_serialized)

    // set decrement input value
    document.getElementById("quantity").value=valueCount_serialized   

    // set decrement input value
    document.getElementById("quantity").value=valueCount

    if(valueCount == quantity){
        document.querySelector(".plus-btn").setAttribute("disabled", "disabled")
    }
    capacity.innerHTML=localStorage.getItem('valueCount')
})