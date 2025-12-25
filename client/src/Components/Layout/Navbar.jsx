import {Link} from 'react-router-dom';
import React from 'react';

const Navbar = () => {
    return (
        <nav>
            <Link to="/">Kicks_Kenya</Link>
            <Link to="/">Home</Link>
            <Link to="/login">Login</Link>
            <Link to="/about">About</Link>
        </nav>
    );
};

export default Navbar;
