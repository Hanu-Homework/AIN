import express from "express";
import solve from "./driver";
import cors from "cors";

const app = express();
const port = 6969;

app.use(express.json());
app.use(cors());

app.post("/solve", (req, res) => {
  console.log(req.body);
  const rows = req.body.rows as number[];
  solve(rows, (gameTree, solution) => {
    res.send({
      gameTree: gameTree,
      solution: solution,
    });
  });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
