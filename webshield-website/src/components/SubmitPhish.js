import React, { useState } from "react";
import { db } from "./firebase";

function SubmitPhish() {
  const [url, setUrl] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await db.collection("phishing_sites").add({
        url: url,
        status: "Not verified",
        createdAt: firebase.firestore.FieldValue.serverTimestamp(),
      });
      setUrl("");
    } catch (error) {
      console.error("Error adding document: ", error);
    }
  };

  return (
    <div>
      <h2>Submit a Suspected Phishing Site</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter URL"
          required
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default SubmitPhish;
