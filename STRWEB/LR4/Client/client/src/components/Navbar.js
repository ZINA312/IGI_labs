import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import Auth from "./Auth";
import '../styles/Navbar.css';

const Navbar = () => {
    const [currentDate, setCurrentDate] = useState("");
    const [timeZone, setTimeZone] = useState("");

    const handleClick = (page) => {
        console.log(`Navigating to ${page}`);
    };

    useEffect(() => {
        const updateDate = () => {
            const date = new Date();
            setCurrentDate(date.toLocaleString());
            setTimeZone(
                new Intl.DateTimeFormat("en-US", {
                    timeZoneName: "short",
                }).format(date)
            );
        };

        updateDate();
        const intervalId = setInterval(updateDate, 1000);

        return () => clearInterval(intervalId);
    }, []);

    return (
        <nav className="navbar">
            <ul className="nav-links">
                <li><Link to="/" onClick={() => handleClick('Home')}>Home</Link></li>
                <li><Link to="/properties" onClick={() => handleClick('Properties')}>Properties</Link></li>
                <li><Link to="/news" onClick={() => handleClick('News')}>News</Link></li>
            </ul>
            <div className="date-time">
                <p>Current Date: {currentDate}</p>
            </div>
            <div className="date-time">
              <p>Time Zone: {timeZone}</p>
            </div>
            
            <Auth />
        </nav>
    );
};

export default Navbar;