function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
}

function postData(string) {
  if (!string) {string = "none"}
  fetch("/inputapi/increment_balance", {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({payload: string})
  })
  .then(response => response.json())
  .then(data => {
    $("#balance").text(data.balance)
    console.log(data)
  })
}

function postIfClicked(id, data) {
  $(id).click(function(){
    postData(data);
  })
}

postData("doNotUpBalance")

$(document).ready(function(){
  postIfClicked("#clicker")
})