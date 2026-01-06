async function runKarazonBilling() {
  addItemsToCart();

  let grandTotal = calculateGrandTotal();
  console.log("Grand Total:", grandTotal);

  let discountData = applyMembershipDiscount(grandTotal);
  let taxData = applyTax(discountData.discountedTotal);
  let paymentData = applyPaymentCharges(taxData.totalWithTax);

  await processPaymentAsync();

  generateInvoice(paymentData);

  let email = prompt("Enter Email ID (@karunya.edu)");
  if (validateEmail(email)) {
    sendInvoiceEmail(email);
  } else {
    alert("Invalid Email Format");
  }

  saveToLocalStorage(cart, paymentData);

  completeBilling(msg => console.log(msg));
}

/* AUTO EXECUTION */
runKarazonBilling();
