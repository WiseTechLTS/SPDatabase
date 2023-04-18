import React from "react";
import { Container } from "react-bootstrap";
import "./NavBar.css";
import DropDown from "../DropDown";

const Navbar = () => {
  return (
    <Container className="navBar" fluid>
            <DropDown />
    </Container>
  );
};

export default Navbar;
