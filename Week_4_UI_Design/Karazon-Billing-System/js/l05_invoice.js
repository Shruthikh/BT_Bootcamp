function generateInvoice(paymentData) {
  let invoiceNumber = "INV" + Math.floor(Math.random() * 100000);
  let invoiceDate = new Date();

  console.log("========= FINAL INVOICE =========");
  console.log("Invoice No:", invoiceNumber);
  console.log("Invoice Date:", invoiceDate.toLocaleString());
  console.table(cart);
  console.log("Final Payable Amount:", paymentData.finalTotal);
  console.log("Payment Successful");
  console.log("Invoice Generated");
}
