function applyTax(discountedTotal) {
  const gstRate = 0.18;
  const platformFeeRate = 0.002;

  let gstAmount = discountedTotal * gstRate;
  let platformFee = discountedTotal * platformFeeRate;

  return {
    gstAmount,
    platformFee,
    totalWithTax: discountedTotal + gstAmount + platformFee
  };
}
