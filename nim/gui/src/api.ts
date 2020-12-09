import { PythonShell } from "python-shell";
import StateNode from "./stateNode";

export default function solve(
  rows: number[],
  onResultCallBack: (gameTree: StateNode, solution: any) => void
) {
  PythonShell.run(
    "brute_force/main.py",
    {
      args: rows.map((num) => num.toString()),
      scriptPath: "../engine",
    },
    function (err, results) {
      if (err) throw err;

      const gameTree = JSON.parse(
        (results![0] as string).split(`'`).join(`"`)
      ) as StateNode;
      console.log(gameTree.w);
      const solution = JSON.parse((results![1] as string).split(`'`).join(`"`));

      onResultCallBack(gameTree, solution);
    }
  );
}
