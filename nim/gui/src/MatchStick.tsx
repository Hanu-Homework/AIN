import { Fab, Typography } from "@material-ui/core";
import React from "react";

interface Props {
  rowIndex: number;
  selfIndex: number;
  isInActiveRow: boolean;
  onSelfClick: (rowIndex: number, selfIndex: number) => void;
  isSelected: boolean;
}

const MatchStick: React.FC<Props> = ({
  isSelected,
  rowIndex,
  selfIndex,
  onSelfClick,
}) => {
  return (
    <Fab
      disabled={isSelected}
      onClick={() => {
        onSelfClick(rowIndex, selfIndex);
      }}
      color="primary"
    >
      {isSelected ? "" : <Typography>{selfIndex + 1}</Typography>}
    </Fab>
  );
};

export default MatchStick;
