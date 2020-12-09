"use strict";
exports.__esModule = true;
var api_1 = require("./api");
api_1["default"]([1, 3, 5, 6], function (gameTree, solution) {
    console.log(JSON.stringify(gameTree, undefined, 2));
    console.log(solution);
});
