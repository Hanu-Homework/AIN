"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
var express_1 = __importDefault(require("express"));
var driver_1 = __importDefault(require("./driver"));
var cors_1 = __importDefault(require("cors"));
var app = express_1.default();
var port = 6969;
app.use(express_1.default.json());
app.use(cors_1.default());
app.post("/solve", function (req, res) {
    console.log(req.body);
    var rows = req.body.rows;
    driver_1.default(rows, function (gameTree, solution) {
        res.send({
            gameTree: gameTree,
            solution: solution,
        });
    });
});
app.listen(port, function () {
    console.log("Example app listening at http://localhost:" + port);
});
