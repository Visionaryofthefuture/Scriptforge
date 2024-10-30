import React from 'react';
import './css/Navbar.css';
import Form from './Register';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <Router>
            <nav className="navbar">
                <div className="navbar-logo">ScriptForge</div>
                <ul className="navbar-links">
                    <li><Link to="/explore">Explore</Link></li>
                    <li><Link to="/product">Product</Link></li>
                    <li><Link to="/developer">Developer</Link></li>
                    <li><Link to="/signin">Sign In</Link></li>
                </ul>
            </nav>
            <Routes>
                <Route path="/explore" element={<Form />} />
                {/* Add more routes as needed */}
            </Routes>
        </Router>
    );
};

export default Navbar;
