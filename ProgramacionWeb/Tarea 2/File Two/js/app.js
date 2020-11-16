var arr = Array();

function agregar(){
  var n = parseInt(document.getElementById("num").value);
  arr.push(n);
  document.getElementById("nums").value += n+" ";
}

function obtPromedio(){
  var suma=0;
  for(var i=0; i < arr.length; i++) suma += arr[i];
  alert(suma/arr.length);
  document.getElementById('Promedio').innerHTML = p;
}