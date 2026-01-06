let cart = [];

function addItemsToCart() {
  try {
    let addMore = true;

    while (addMore) {
      let itemCode = prompt("Enter Item Code:");
      let description = prompt("Enter Description:");
      let quantity = Number(prompt("Enter Quantity:"));
      let pricePerUnit = Number(prompt("Enter Price per Unit:"));

      if (quantity <= 0 || pricePerUnit <= 0) {
        throw new ValidationError("Quantity and Price must be greater than zero");
      }

      let totalPrice = quantity * pricePerUnit;

      cart.push({
        itemCode,
        description,
        quantity,
        pricePerUnit,
        totalPrice
      });

      addMore = confirm("Add another item?");
    }
  } catch (err) {
    alert(err.message);
  }
}

function calculateGrandTotal() {
  return cart.reduce((sum, item) => sum + item.totalPrice, 0);
}
