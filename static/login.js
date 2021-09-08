function togglePassword(){
  var x = document.querySelector("form > input[name=password]");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
  x.nextElementSibling.classList.toggle('fa-eye-slash');
}