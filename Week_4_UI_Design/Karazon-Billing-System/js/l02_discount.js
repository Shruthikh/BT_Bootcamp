function applyMembershipDiscount(grandTotal) {
  let discountRate = 0;
  let discountAmount = 0;

  let isMember = confirm("Are you a member?");
  if (isMember) {
    let type = prompt("Enter Membership Type (Silver / Gold / Platinum)");

    if (type === "Silver") discountRate = 0.05;
    else if (type === "Gold") discountRate = 0.10;
    else if (type === "Platinum") discountRate = 0.15;
  }

  discountAmount = grandTotal * discountRate;

  return {
    discountedTotal: grandTotal - discountAmount,
    discountAmount
  };
}
