import React from "react";
import { Navbar, Nav, Form, FormControl, Button } from "react-bootstrap";
import "../styles/NavbarComponent.css";
import BrandLogo from "../assets/brand_logo.png";

function NavbarComponent() {
  return (
    <Navbar bg="dark" variant="dark" expand="lg">
      <Navbar.Brand href="#home" className="d-flex align-items-center">
        <img
          src={BrandLogo}
          alt="Logo"
          width="60"
          height="60"
          className="d-inline-block align-top"
        />
        <span className="brand-name ml-3">WebShield</span>{" "}
        {/* Increased margin */}
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="#home" className="nav-link">
            Home
          </Nav.Link>
          <Nav.Link href="#phishsearch" className="nav-link">
            PhishSearch
          </Nav.Link>
        </Nav>
        <Form inline className="ml-auto d-flex align-items-center">
          <FormControl type="text" placeholder="Username" className="mr-2" />
          <FormControl
            type="password"
            placeholder="Password"
            className="mr-2"
          />
          <Button  className="login-button" variant="outline-light">Login</Button>
        </Form>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default NavbarComponent;
