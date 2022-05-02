const users = document.getElementsByClassName("employeeBlock");
const userNames = document.getElementsByClassName("name");
for (let i = 0; i < users.length; i++) {
  users[i].addEventListener("click", () => {
    console.log("Button " + i + " has been clicked");
    document.location.href = 'search+' + (i + 1)
  });
}
