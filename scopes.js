for (let i = 0; i <10; i++) {
    console.log(i);
}

// si la variable i n'a pas été définie dans le scope global, elle n'est pas utilisable
// si la variable i à été définie avec le mot clé let, elle n'est accessible que 
//si elle a été définie dans le même scope (ou un scope extérieur)
console.log(i);

for (var i = 0; i <10; i++) {
    console.log(i);
}

// si la variable i à été définie avec le mot clé var, elle est accessible même si elle a été définie dans un scope intérieur
console.log(i);

function myFunc1() {
    var myVar1 = 123;
}

myFunc1();
// même si la variable myVar1 est déclarée avec le mot clé var, comme elle est déclarée à l'intérieur d'une fonction, 
// elle n'est pas accessible depuis un scope extérieur
// ReferenceError: myVar1 is not defined
console.log(myVar1);
