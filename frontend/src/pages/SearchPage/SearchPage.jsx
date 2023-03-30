import { useState } from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import "bootstrap/dist/css/bootstrap.min.css";
import { data } from "../../data.js";

function SearchPage() {
  const [items, setItems] = useState(data);
  const [search, setSearch] = useState("");

  // const sortName = () => {
  //   setContacts(
  //     data.sort((a, b) => {
  //       return a.first_name.toLowerCase() < a.first_name.toLowerCase()
  //         ? -1
  //         : a.first_name.toLowerCase() > a.first_name.toLowerCase()
  //         ? 1
  //         : 0;
  //     })
  //   );
  // };

  return (
      <Container>
        <h1>The Scrap Soldier Store</h1>
        <Form>
          <InputGroup className="my-3">
            {/* onChange for search */}
            <Form.Control
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Search Inventory"
            />
          </InputGroup>
        </Form>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Id</th>
              <th>Price</th>
              <th>Name</th>
              <th>Size</th>
              <th>In Stock</th>
              <th>Image</th>
            </tr>
          </thead>
          <tbody>
            {data
              .filter((item) => {
                return search.toLowerCase() === ""
                  ? item
                  : item.Name.toLowerCase().includes(search);
              })
              .map((item, index) => (
                <tr key={index}>
                  <td>{item.Id}</td>
                  <td>{item.Price}</td>
                  <td>{item.Name}</td>
                  <td>{item.Size}</td>
                  <td>{item.InStock}</td>
                  <td>
                    {item.Image_URL && (
                      <img
                        src={item.Image_URL}
                        alt={item.URL}
                        width="100px"
                        height="100px"
                      />
                    )}
                  </td>
                </tr>
              ))}
          </tbody>
        </Table>
      </Container>
  );
}

export default SearchPage;