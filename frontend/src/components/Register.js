import React, { useState } from 'react';
import './css/Form.css';

const Form = () => {
    const [formData, setFormData] = useState({
        username: '',  // Changed from 'name' to 'username'
        email: '',
        password1: '', // Ensure this matches your backend requirements
        password2: '',
    });
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (formData.password1 !== formData.password2) {
            setError('Passwords do not match');
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:8000/auth/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: formData.username,
                    email: formData.email,
                    password1: formData.password1,
                    password2: formData.password2,
                }),
            }).then((data) => {
                console.log("Registration successful:", data);
            })
            .catch((error) => {
                console.error("Registration error:", error);
            });

            if (response.ok) {
                setSuccess('Registration successful!');
                setFormData({ username: '', email: '', password1: '', password2: '' });
                setError('');
            } else {
                const data = await response.json();
                setError(data.detail || 'Registration failed'); 
            }
        } catch (err) {
            setError('An error occurred. Please try again.');
        }
    };

    return (
        <div className="form-container">
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">Username</label>
                <input
                    type="text"
                    id="username"
                    name="username"
                    value={formData.username}
                    onChange={handleChange}
                    required
                />

                <label htmlFor="email">Email</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                />

                <label htmlFor="password1">Password</label>
                <input
                    type="password"
                    id="password1"
                    name="password1"
                    value={formData.password1}
                    onChange={handleChange}
                    required
                />

                <label htmlFor="password2">Confirm Password</label>
                <input
                    type="password"
                    id="password2"
                    name="password2"
                    value={formData.password2}
                    onChange={handleChange}
                    required
                />

                {error && <p className="error">{error}</p>}
                {success && <p className="success">{success}</p>}

                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Form;
