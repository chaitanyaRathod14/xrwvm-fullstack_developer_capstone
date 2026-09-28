import React, { useState } from 'react';
import "./Register.css";
import "../assets/style.css";
import Header from '../Header/Header';

const Register = () => {
  const [userName, setUserName] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const register = async () => {
    if (!userName || !firstName || !lastName || !email || !password) {
      setError("All fields are required.");
      return;
    }

    const data = {
      userName,
      firstName,
      lastName,
      email,
      password,
    };

    const res = await fetch('/djangoapp/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });

    const json = await res.json();

    if (json.status === "Authenticated") {
      sessionStorage.setItem("username", json.userName);
      setSuccess("Registration successful! Redirecting...");
      window.location.href = "/";
    } else if (json.error === "Already Registered") {
      setError("Username already exists. Please choose a different one.");
    } else {
      setError("Registration failed. Please try again.");
    }
  };

  return (
    <div>
      <Header />
      <div
        style={{
          maxWidth: '420px',
          margin: '60px auto',
          background: 'white',
          borderRadius: '12px',
          boxShadow: '0 4px 24px rgba(0,0,0,0.12)',
          padding: '40px',
        }}
      >
        <h2 style={{ textAlign: 'center', color: '#1e3a5f', marginBottom: '24px', fontWeight: 700 }}>
          Create Account
        </h2>

        {error && (
          <div style={{ color: '#dc3545', background: '#fde8e8', borderRadius: '6px', padding: '10px 14px', marginBottom: '16px', fontSize: '0.9rem' }}>
            {error}
          </div>
        )}
        {success && (
          <div style={{ color: '#155724', background: '#d4edda', borderRadius: '6px', padding: '10px 14px', marginBottom: '16px', fontSize: '0.9rem' }}>
            {success}
          </div>
        )}

        <div style={{ marginBottom: '16px' }}>
          <label style={{ fontWeight: 600, display: 'block', marginBottom: '6px', color: '#333' }}>Username</label>
          <input
            type="text"
            placeholder="Enter username"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            style={{ width: '100%', padding: '10px 12px', borderRadius: '6px', border: '1px solid #ccc', fontSize: '0.95rem', boxSizing: 'border-box' }}
          />
        </div>

        <div style={{ marginBottom: '16px' }}>
          <label style={{ fontWeight: 600, display: 'block', marginBottom: '6px', color: '#333' }}>First Name</label>
          <input
            type="text"
            placeholder="Enter first name"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            style={{ width: '100%', padding: '10px 12px', borderRadius: '6px', border: '1px solid #ccc', fontSize: '0.95rem', boxSizing: 'border-box' }}
          />
        </div>

        <div style={{ marginBottom: '16px' }}>
          <label style={{ fontWeight: 600, display: 'block', marginBottom: '6px', color: '#333' }}>Last Name</label>
          <input
            type="text"
            placeholder="Enter last name"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            style={{ width: '100%', padding: '10px 12px', borderRadius: '6px', border: '1px solid #ccc', fontSize: '0.95rem', boxSizing: 'border-box' }}
          />
        </div>

        <div style={{ marginBottom: '16px' }}>
          <label style={{ fontWeight: 600, display: 'block', marginBottom: '6px', color: '#333' }}>Email</label>
          <input
            type="email"
            placeholder="Enter email address"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={{ width: '100%', padding: '10px 12px', borderRadius: '6px', border: '1px solid #ccc', fontSize: '0.95rem', boxSizing: 'border-box' }}
          />
        </div>

        <div style={{ marginBottom: '24px' }}>
          <label style={{ fontWeight: 600, display: 'block', marginBottom: '6px', color: '#333' }}>Password</label>
          <input
            type="password"
            placeholder="Create a password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={{ width: '100%', padding: '10px 12px', borderRadius: '6px', border: '1px solid #ccc', fontSize: '0.95rem', boxSizing: 'border-box' }}
          />
        </div>

        <button
          onClick={register}
          style={{
            width: '100%',
            padding: '12px',
            background: 'darkturquoise',
            color: 'white',
            border: 'none',
            borderRadius: '6px',
            fontSize: '1rem',
            fontWeight: 700,
            cursor: 'pointer',
            transition: 'background 0.3s ease',
          }}
          onMouseOver={(e) => { e.target.style.background = '#00a0a0'; }}
          onMouseOut={(e) => { e.target.style.background = 'darkturquoise'; }}
        >
          Register
        </button>

        <p style={{ textAlign: 'center', marginTop: '16px', fontSize: '0.9rem', color: '#666' }}>
          Already have an account?{' '}
          <a href="/login" style={{ color: '#1e90ff', fontWeight: 600, textDecoration: 'none' }}>Login here</a>
        </p>
      </div>
    </div>
  );
};

export default Register;
