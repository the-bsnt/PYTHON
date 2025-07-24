const loginForm = document.getElementById("login-form");
const baseEndpoint = "http://localhost/8000/api";
if (loginForm) {
  loginForm.addEventListener("submit", handleLogin);
}

function handleLogin(event) {
  console.log(event);
  event.preventDefault();
  let loginFormData = new FormData(loginForm);
  const loginEndpoint = `${baseEndpoint}/token/`;
  const options = {
    method: "POST",
    headers: {
      contentType: "application/json",
    },
    body: "",
  };
  fetch(loginEndpoint, options);
}
