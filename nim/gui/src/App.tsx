import { Button, Paper } from "@material-ui/core";
import React from "react";
import MatchStick from "./MatchStick";
import Tree, { ReactD3TreeItem } from "react-d3-tree";
import solve from "./api";
import StateNode from "./stateNode";

function App() {
  const [rows, setRows] = React.useState<number[]>([1, 3, 5, 7]);

  const [treeData, setTreeData] = React.useState<ReactD3TreeItem | null>(null);

  const [activeRowIndex, setActiveRowIndex] = React.useState<number | null>(
    null
  );

  const [isDialogOpen, setIsDialogOpen] = React.useState<boolean>(false);

  const [selectedElementIndexes, setSelectedElementIndexes] = React.useState<
    number[]
  >([]);

  const walk = (node: StateNode) => {
    setTreeData({
      ...treeData,
      name: `${node.m.i},${node.m.n}`,
      attributes: {
        Winning: node.w ? "true" : "false",
      },
    });
    node.c.forEach((child) => {
      walk(child);
    });
  };

  React.useEffect(() => {
    solve(rows, (gameTree, solution) => {
      walk(gameTree);
      console.log(solution);
    });
  }, [rows]);

  return (
    <div>
      <Paper style={{ padding: 10 }}>
        <div style={{ display: "flex" }}>
          <div>
            {rows.map((count, rowIndex) => (
              <div
                key={rowIndex}
                style={{
                  display: "flex",
                  minWidth: "50%",
                  justifyContent: "center",
                }}
              >
                {[...Array(count)].map((_, elementIndex) => (
                  <div style={{ margin: 10 }} key={elementIndex}>
                    <MatchStick
                      isSelected={
                        elementIndex in selectedElementIndexes &&
                        activeRowIndex === rowIndex
                      }
                      rowIndex={rowIndex}
                      onSelfClick={(rowIndex, elementIndex) => {
                        if (
                          activeRowIndex !== null &&
                          rowIndex !== activeRowIndex
                        )
                          setSelectedElementIndexes([]);

                        setActiveRowIndex(rowIndex);

                        const index = selectedElementIndexes.indexOf(
                          elementIndex
                        );

                        // If the element is not selected
                        if (index === -1) {
                          setSelectedElementIndexes([
                            ...selectedElementIndexes,
                            elementIndex,
                          ]);
                        }
                        console.log(selectedElementIndexes);
                      }}
                      selfIndex={elementIndex}
                      isInActiveRow={
                        activeRowIndex === null || activeRowIndex === rowIndex
                      }
                    />
                  </div>
                ))}
              </div>
            ))}
          </div>
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              justifyContent: "space-between",
              padding: "20px",
              marginLeft: "40px",
            }}
          >
            <Button
              onClick={() => {
                setActiveRowIndex(null);
                setSelectedElementIndexes([]);
              }}
              variant="contained"
              color="primary"
            >
              Revert
            </Button>
            <Button variant="contained" color="primary">
              Confirm
            </Button>
          </div>
        </div>
      </Paper>
      <Paper>
        {treeData && (
          <div id="treeWrapper" style={{ height: "20em" }}>
            <Tree data={treeData} />
          </div>
        )}
      </Paper>
    </div>
  );
}

export default App;
