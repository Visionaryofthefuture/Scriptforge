import React from 'react';
import './css/Navbar.css';

const Navbar = () =>
{
    return(
        <nav className="navbar">
            <div className="navbar-logo">ScriptForge</div>
            <ul className="navbar-links">
                <li><a href="#explore">Explore</a></li>
                <li><a href="#product">Product</a></li>
                <li><a href="#developer">Developer</a></li>
                <li><a href="#signin">Sign In</a></li>
            </ul>
        </nav>
    );

};

export default Navbar;