import React from "react";
import { slide as Menu } from "react-burger-menu";

import "./Burger.css";

export default (props) => {
  return (
    <Menu>
      <a className="menu-item" href="/">
        Home
      </a>

      <a className="menu-item" href="/search">
        Search Inventory
      </a>
      <a className="menu-item" href="/login">
        Login
      </a>

      <a className="menu-item" href="/register">
        Register
      </a>

      <a className="menu-item" href="http://127.0.0.1:8000/admin">
        Database
      </a>
    </Menu>
  );
};
