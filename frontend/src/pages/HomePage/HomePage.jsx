import React from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import { Container, Table } from "react-bootstrap";

import axios from "axios";
const HomePage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  //TODO: Add an Addproducts Page to add a product for a logged in user's garage
  const [user, token] = useAuth();
  const [products, setProducts] = useState([]);
  
  const baseURL = "http://127.0.0.1:8000/";
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/products/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setProducts(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchProducts();
  }, [token]);
  return (
    <Container fluid style={{display: 'responsive'}}>
      <h1>Inventory Page for {user.username}!</h1>
      {products &&
        products.map((product) => (
          <Table className="product-table" key={product.id} striped bordered hover>
            <thead className="t-head">
              <tr>
                <th>Product ID</th>
                <th>Category</th>
                <th>Name</th>
                <th>Size</th>
                <th>Price</th>
                <th>Stock</th>
                <th>Image</th>
              </tr>
            </thead>
            <tbody className="t-body" fluid>
              <tr>
                <td>
                  {product.id}
                </td>
                <td>
                  {product.category}
                </td>
                  {product.name}
                <td>
                  {product.size}
                </td>
                  {product.price}
                <td>
                  {product.in_stock}
                </td>
                <td>
              {product.image && (
                <img src={baseURL+product.image} alt={product.image} width={'150px'} height={'150px'} display={'grid'} />
                )}
                </td>
              </tr>
              </tbody>
          </Table>
        ))}
    </Container>
  );
};

export default HomePage;
