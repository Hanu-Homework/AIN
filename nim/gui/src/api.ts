import StateNode from "./stateNode";

export default function solve(
  rows: number[],
  onResultCallBack: (gameTree: StateNode, solution: any) => void
) {
  fetch("http://localhost:6969/solve", {
    method: "POST",
    body: JSON.stringify({
      rows: rows,
    }),
  }).then((result) => {
    console.log(result);
    result.json().then((parsed) => {
      console.log(parsed);
      onResultCallBack(parsed.gameTree, parsed.solution);
    });
  });
}
