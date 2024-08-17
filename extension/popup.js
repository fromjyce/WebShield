document.getElementById("visit-site").addEventListener("click", () => {
  chrome.tabs.create({ url: "http://localhost:3000" });
});
