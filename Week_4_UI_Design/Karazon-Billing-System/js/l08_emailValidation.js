function validateEmail(email) {
  let regex = /^[a-zA-Z0-9._%+-]+@karunya\.edu$/;
  return regex.test(email);
}
