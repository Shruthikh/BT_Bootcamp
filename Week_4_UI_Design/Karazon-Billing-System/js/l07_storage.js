function saveToLocalStorage(cart, invoiceData) {
  let data = {
    cart,
    invoiceData,
    timestamp: new Date().toLocaleString()
  };

  localStorage.setItem("karazonData", JSON.stringify(data));
}
