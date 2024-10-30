// src/components/Homepage.js
import React from 'react';
import './css/Homepage.css';

const Homepage = () => {
    return (
        <div className="homepage">
            <section className="intro-section">
                <div className="intro-content">
                    <h1>A New Way to Learn</h1>
                    <p>LeetCode is the best platform to help you enhance your skills, expand your knowledge and prepare for technical interviews.</p>
                    <button className="create-account-button">Create Account</button>
                </div>
            </section>
            <section className="explore-section">
                <h2>Start Exploring</h2>
                <p>Explore is a well-organized tool that helps you get the most out of LeetCode by providing structure to guide your progress towards the next step in your programming career.</p>
                <button className="get-started-button">Get Started</button>
            </section>
        </div>
    );
};

export default Homepage;
