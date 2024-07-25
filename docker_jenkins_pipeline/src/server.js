const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello from Dockerized Node.js app!');
});

app.get('/api', (req, res) => {
  res.json({ message: 'Hello, API!' });
});

app.listen(port, () => {
  console.log(`App running at http://localhost:${port}`);
});

module.exports = app; // Export the app for testing

