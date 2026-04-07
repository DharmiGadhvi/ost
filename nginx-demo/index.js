const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("<h1>Hello BE 6th SEM - Deployed using Nginx</h1>");
});

app.get("/about", (req, res) => {
  res.send("<h2>About Page - Nginx Reverse Proxy Demo</h2>");
});

app.listen(3000, () => {
  console.log("App running on http://localhost:3000");
});