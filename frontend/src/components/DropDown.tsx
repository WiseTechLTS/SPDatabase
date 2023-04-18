import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Offcanvas from "react-bootstrap/Offcanvas";
import scrap from '../../Scrap.jpg';
import { Link } from "react-router-dom";
import Row from "react-bootstrap/Row";
import AuthContext from "../context/AuthContext";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";

function DropDown() {
  const [show, setShow] = useState(false);
  const { logoutUser, user } = useContext(AuthContext);
  const navigate = useNavigate();
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <>
      <Button className="scrapButton" variant="outline" onClick={handleShow}>
        <img src={scrap} alt={scrap} />
      </Button>

      <Offcanvas className="Offcanvas" show={show} onHide={handleClose}>
        <Offcanvas.Header closeButton>
          <Offcanvas.Title>
            <Row>
              <Link to="/search">
                <Button variant="outline">SEARCH</Button>
              </Link>
              <Link to="/store">
                <Button variant="outline">STORE</Button>
              </Link>
            </Row>
          </Offcanvas.Title>
        </Offcanvas.Header>
        <Offcanvas.Body>
          <Link to="/register">
            <Button variant="outline">REGISTER</Button>
          </Link>
          <Link to="/login">
            <Button variant="outline">LOGIN</Button>
            <li>
              {user ? (
                <Button onClick={logoutUser} variant="outline">
                  Logout
                </Button>
              ) : (
                <Button onClick={() => navigate("/login")}>Login</Button>
              )}
            </li>
          </Link>
        </Offcanvas.Body>
      </Offcanvas>
    </>
  );
}
export default DropDown;