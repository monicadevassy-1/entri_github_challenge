// console.log("hello my dear")

function calc(val)
{
    document.getElementById('inscreen').value+=val;
}
val=""

function result()
{
    document.getElementById('inscreen').value=eval(document.getElementById('inscreen').value)
}

function clearsp()
{
    document.getElementById('inscreen').value="";
}

function square()
{
    document.getElementById('inscreen').value=eval(document.getElementById('inscreen').value) ** 2;
}

function sqrt()
{
    document.getElementById('inscreen').value = Math.sqrt(eval(document.getElementById('inscreen').value));
}


function backspace() 
{
    document.getElementById('inscreen').value =document.getElementById('inscreen').value.slice(0, -1);
}