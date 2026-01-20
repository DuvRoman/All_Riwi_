

let products= [];

products.push( {id : "01", name : "Banana", price: "2.000"  });
products.push( {id : "02", name : "Manzana", price: "3.500"  });
products.push( {id : "03", name : "Sandia", price: "7.000"  });
products.push( {id : "04", name : "Piña", price: "5.000"  });
products.push( {id : "05", name : "Durazno", price: "2.700"  });

console.log(products);

let set_1= new Set([22, 45, 66, 66, 34, 23, 22, 55, 98, 66]);

console.log([...set_1]);

set_1.add(14);
set_1.add(11);

console.log([...set_1]);

console.log(set_1.has(98))

set_1.delete(23);
console.log([...set_1]);

for(const num of set_1){
    console.log(num);
};

// let products_2 = [
//     {
//         "vegetables" :{
//                 id: "1", name : "carrot", price: "2.000",
//                 id: "2", name : "potato", price: "5.000",
//                 id: "3", name : "corn", price: "3.200",
//                 id: "4", name : "tomato", price: "2.500",
//         },

//          "fruits" :{
//                 id: "1", name : "apple", price: "2.000",
//                 id: "2", name : "banana", price: "1.000",
//                 id: "3", name : "pineapple", price: "3.700",
//                 id: "4", name : "orange", price: "1.500",
//         },
//     }
// ];

const mapOne = new Map ();

mapOne.set('id', 1)
mapOne.set('name', 'potato')
mapOne.set('price', 5.000)

console.log(mapOne)


