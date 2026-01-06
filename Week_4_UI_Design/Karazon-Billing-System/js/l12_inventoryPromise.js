function checkInventory(quantity) {
  return new Promise((resolve, reject) => {
    if (quantity <= 10) {
      resolve("Stock Available");
    } else {
      reject("Stock Not Available");
    }
  });
}















// checkInventory(5)
//   .then(result => console.log(result))
//   .catch(error => console.log(error));
