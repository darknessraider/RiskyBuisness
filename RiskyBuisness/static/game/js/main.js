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

async function postData(string) {
  if (!string) {string = "none"}
  await fetch("/inputapi/increment_balance", {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({payload: string})
  })
  .then(response => response.json())
  .then(json => {console.log("Sent Post")})
}

async function getSetBalance() {
  await $.get("/outputapi/get_balance", function (data, textStatus, jqXHR) {
      $("#balance").text(data.balance)
      console.log("Balance Got")
    },
  )
}

getSetBalance()

$(document).ready(function(){
  $("#clicker").click(async function(){
    await postData();
    await getSetBalance()
    console.log("Clicked")
  })
})