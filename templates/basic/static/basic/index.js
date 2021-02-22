document.getElementById("button").innerText = "Hide Image";
document.getElementById("button").addEventListener("click", function () {
  if (document.getElementById("avatar").style.display === "none") {
    document.getElementById("avatar").style.display = "block";
    document.getElementById("button").innerText = "Hide Image";
  } else {
    document.getElementById("avatar").style.display = "none";
    document.getElementById("button").innerText = "Show Image";
  }
});
