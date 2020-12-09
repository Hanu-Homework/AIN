"use strict";
exports.__esModule = true;
var python_shell_1 = require("python-shell");
function solve(rows, onResultCallBack) {
    python_shell_1.PythonShell.run("brute_force/main.py", {
        args: rows.map(function (num) { return num.toString(); }),
        scriptPath: "../engine"
    }, function (err, results) {
        if (err)
            throw err;
        var gameTree = JSON.parse(results[0].split("'").join("\""));
        console.log(gameTree.w);
        var solution = JSON.parse(results[1].split("'").join("\""));
        onResultCallBack(gameTree, solution);
    });
}
exports["default"] = solve;
