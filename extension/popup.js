document.getElementById("visit-site").addEventListener("click", () => {
  chrome.tabs.create({ url: "https://example.com" }); // Replace with the URL you want to open
});
