async function processPaymentAsync() {
  console.log("Processing Payment...");
  await new Promise(resolve => setTimeout(resolve, 2000));
  console.log("Payment Confirmed");
}
