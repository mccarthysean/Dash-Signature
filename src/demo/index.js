import React from 'react';
import App from './App';
import { createRoot } from 'react-dom/client';
const container = document.getElementById('react-entry-point');
const root = createRoot(container);
root.render(<App tab="home" />);
