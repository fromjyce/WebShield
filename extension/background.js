chrome.webRequest.onBeforeRequest.addListener(
  async function (details) {
    const url = details.url;
    try {
      const response = await fetch("http://localhost:8000/predict/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: url }),
      });
      const result = await response.json();
      if (result.prediction === "phishing") {
        chrome.notifications.create({
          type: "basic",
          iconUrl: "icon.png",
          title: "Warning",
          message: "This site might be phishing!",
        });
      }
    } catch (error) {
      console.error("Error:", error);
    }
  },
  { urls: ["<all_urls>"] },
  ["blocking"] // Add this to use the webRequest API to block requests
);
