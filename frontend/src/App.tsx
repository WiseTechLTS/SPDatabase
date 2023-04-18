import { Routes, Route } from 'react-router-dom'
import './App.css'
import { Container } from 'react-bootstrap'
// Pages Imports
import HomePage from './pages/HomePage/HomePage'
import RegisterPage from './pages/RegisterPage/RegisterPage'
import LoginPage from './pages/LoginPage/LoginPage'
import SearchPage from './pages/SearchPage/SearchPage'


// Components Imports
import Navbar from './components/NavBar/NavBar'
import Footer from './components/Footer/Footer'
import PromoBanner from './components/PromoBanner/PromoBanner'
// Util imports
import PrivateRoute from './utils/PrivateRoute'


function App() {

  return (
    <Container className="App" fluid>
        <PromoBanner />
        <Navbar />
        <Routes>
          <Route
            path="/"
            element={
              <PrivateRoute>
                <HomePage />
              </PrivateRoute>
            }
          />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/search" element={<SearchPage />} />
        </Routes>
          <Footer />
    </Container>
  );
}

export default App
