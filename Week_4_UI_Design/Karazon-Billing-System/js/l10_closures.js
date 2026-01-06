function getDiscountFunction(membershipType) {
  let rate = 0;

  if (membershipType === "Gold") rate = 0.10;
  else if (membershipType === "Silver") rate = 0.05;

  return function (amount) {
    return amount * rate;
  };
}
