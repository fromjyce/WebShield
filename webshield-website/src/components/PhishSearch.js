
import React, { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import { db } from "./firebase";
import "../styles/PhishSearch.css";

function PhishSearch() {
  const [phishingSites, setPhishingSites] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const snapshot = await db.collection("phishing_sites").get();
      const sites = snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }));
      setPhishingSites(sites);
    };
    fetchData();
  }, []);

  return (
    <Container>
      <h2 className="recent-submissions-heading">Recent Submissions</h2>
      {/* Add additional content here */}
    </Container>
  );
}

export default PhishSearch;
