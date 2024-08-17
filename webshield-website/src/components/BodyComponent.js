import React from "react";
import { Container, Row, Col, Button, Form } from "react-bootstrap";
import "../styles/BodyComponent.css";

function BodyComponent() {
  return (
    <Container fluid>
      <Row className="vh-100">
        {/* Left Half */}
        <Col md={8} className="left-half">
          <h2>Join the fight against phishing</h2>
          <p className="lines-paragraph">
            <a href="/submit-phishes" className="text-link">
              Submit
            </a>{" "}
            suspected phishes.{" "}
            <a href="/track-status" className="text-link">
              Track
            </a>{" "}
            the status of your submissions.{" "}
            <a href="/verify-submissions" className="text-link">
              Verify
            </a>{" "}
            other users' submissions.
          </p>
          <div className="yellow-box">
            <p className="submit-paragraph">
              Found a phishing site? Get started now — see if it's in the Tank:
            </p>
            <Form inline className="d-flex align-items-center">
              <Form.Control
                type="text"
                placeholder="http://"
                className="input-box"
              />
              <Button variant="danger" className="ml-2">
                Is it a phish?
              </Button>
            </Form>
          </div>
          <h3 className="recent-submissions-heading">Recent Submissions</h3>
        </Col>
        {/* Right Half */}
        <Col md={4} className="right-half">
          <div className="box mb-3">
            <h3>What is Phishing?</h3>
            <p>
              Phishing is a type of cyber attack that involves tricking
              individuals into disclosing sensitive information, such as
              passwords or credit card numbers, by pretending to be a
              trustworthy entity.
            </p>
            <a
              href="https://www.cisco.com/c/en_in/products/security/email-security/what-is-phishing.html"
              className="text-link"
            >
              Learn more
            </a>
          </div>
          <div className="box">
            <h3>About WebShield</h3>
            <p>
              <strong>WebShield</strong> is a robust browser extension designed
              to enhance online security by detecting and alerting users about
              potential phishing sites. It employs machine learning models to
              analyze and classify web pages in real-time, providing immediate
              notifications if a site is suspected to be malicious. With
              features such as a customizable user interface and integration
              with a centralized database for phishing submissions, WebShield
              aims to protect users from fraudulent websites and ensure safer
              browsing experiences.
            </p>
            <a
              href="https://github.com/fromjyce/WebShield"
              className="text-link"
            >
              Click here to see the repo
            </a>
          </div>
        </Col>
      </Row>
    </Container>
  );
}

export default BodyComponent;
