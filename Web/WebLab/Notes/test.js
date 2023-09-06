const greatestCommonDivisor = (a, b) => {
    if (b > a){
        const temp = a;
        a = b;
        b = a;
    }
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
};

const x = 50;
const y = 15;
const gcd = greatestCommonDivisor(x, y);
console.log(gcd);



let myBoolean = true;
myBoolean = false;


let pets = ["cat", 42, true];
console.log(pets[0]);

pets[1] = "turtle";
pets.pop();
pets.push("rabbit");



for (let i = 0; i < pets.length; i++) {
    const phrase = "I love my" + pets[i];
    console.log(phrase);
}

for (const animal of pets) {
    const phrase = "I love my" + animal;
    console.log(phrase);
}



const addTwo = x => {
    return x + 2;
};

const modifyArray = (array, callback) => {
    for (let i = 0; i < array.length; i++) {
        array[i] = callback(array[i]);
    }
};

let myArray = [5, 10 ,15];
modifyArray(myArray, addTwo);
modifyArray(myArray, x => {
    return x + 2;
}
    );

myArray[1, 2, 3, 4, 5];
let modifiedArray = myArray.map(x => x * 3);
let posiveValues = value.filter(x => x > 0);


const myCar = {
    make : "Ford",
    model : "Mustang",
    year : 2005,
    color : "red"
};

const { make, model } = myCar;


class Rectangle{
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }

    getArea = () => {
        return this.width * this.height;
    };
}

const smallRect = new Rectangle(3, 4);

setInterval(() => {
    
}, interval);

setTimeout(() => {
    
}, timeout);