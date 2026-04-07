const express = require("express");
const app = express();

const PORT = process.env.PORT || 3000;
const SERVER_NAME = process.env.SERVER_NAME || `Server - Port ${PORT}`;
const DELAY_MS = Number(process.env.DELAY_MS || 0);

app.get("/", (req, res) => {
  const response = `Response from Server running on port ${PORT}`;

  if (DELAY_MS > 0) {
    setTimeout(() => {
      res.send(response);
    }, DELAY_MS);
    return;
  }

  res.send(response);
});

app.listen(PORT, () => {
  console.log(`${SERVER_NAME} started on port ${PORT}`);
});