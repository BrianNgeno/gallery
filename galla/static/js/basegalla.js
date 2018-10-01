function copyLink() {
    var copyText = document.getElementById("thislinkhere");
    copyText.select();
    document.execCommand("copy");
  
    /* Alert the copied text */
    alert("Text Copied : " + copyText.value);
  }