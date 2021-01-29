function clipboard() {
  var copyText = document.getElementById("result");
  copyText.select();
  document.execCommand("copy");
  alert("Copied To Clipboard: " + copyText.value);
}
