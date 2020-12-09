import solve from "./api";

solve([1, 3, 5, 6], (gameTree, solution) => {
  console.log(JSON.stringify(gameTree, undefined, 2));
  console.log(solution);
});
