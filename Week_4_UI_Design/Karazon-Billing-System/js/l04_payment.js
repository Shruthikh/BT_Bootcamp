function applyPaymentCharges(totalWithTax) {
  let paymentMode = prompt("Payment Mode (Card / UPI / Cash)");
  let charge = 0;

  if (paymentMode === "Card" && totalWithTax < 1000) {
    charge = totalWithTax * 0.025;
  } else {
    charge = totalWithTax * 0.01;
  }

  return {
    paymentMode,
    charge,
    finalTotal: totalWithTax + charge
  };
}
