async function logSubmit(event) {
  event.preventDefault();
  //   console.log(event);
  alert("libert");
  log.textContent = `Form Submitted! Timestamp: ${event.timeStamp}`;
}

const form = document.getElementById("form");
const log = document.getElementById("log");
form.addEventListener("submit", logSubmit);
