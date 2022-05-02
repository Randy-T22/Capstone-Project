const users = document.getElementsByClassName("employeeBlock");
const userNames = document.getElementsByClassName("name");
for (var i = 0; i < users.length; i++) {
  users[i].addEventListener("click", () => {
    console.log("Button " + users[i] + " has been clicked");
  });
}
