const { default: async } = require("async");

const fs = require("fs"),
  filename = "values1.txt";

fs.readFile(filename, "utf8", function (err, data) {
  if (err) throw err;
  console.log("OK: " + filename);
  const dades = data.split("\r\n");
  const numbers = dades.map((n) =>
    n.split(",").map(function (item) {
      return parseInt(item, 10);
    })
  )[0];
  let boards = [];
  let arr = [];
  for (let i = 2; i < dades.length; i++) {
    if (dades[i][0] !== undefined) {
      arr.push(dades[i]);
    }
  }
  arr = arr.map((row) =>
    row
      .split(" ")
      .map((n) => parseInt(n))
      .filter((value) => !Number.isNaN(value))
  );
  const n = 5;

  for (let i = 0; i < arr.length; i += n) {
    const matriu = arr.slice(i, i + n);
    boards.push(matriu);
  }
  start(boards, numbers);
});
function start(boards, numbers) {
  let lengthBoards = boards.length;
  let isBoardWinner = false;
  let winnerNumber = 0;
  let winnerBoard = 0;
  let x = 0;
  let isPreviousWinner = false
  for (const number of numbers) {
    if (!isBoardWinner) {
      boards = checkBoards(number, boards);
      let data = checkWinner(boards);
      let winner = data[0];
      if (winner) {
        boards = data[1];
        winnerBoard = data[1][0];
        winnerNumber = number;
        if (boards.length === 1 && !isPreviousWinner) {
          isPreviousWinner = true
        }else if(boards.length === 1 && isPreviousWinner){
            isBoardWinner = true;
        }
      }else {
          //isPreviousWinner = false
      }
    } else {
      console.log(winnerNumber);
      console.log(winnerBoard);
      break;
    }
  }
  if (isBoardWinner) {
    let sum = 0;
    for (row of winnerBoard) {
      for (num of row) {
        if (num !== "X") {
          sum += num;
        }
      }
    }
    console.log(`Total: ${sum * winnerNumber}`);
  }
}
function checkBoards(number, boards) {
  return boards.map((board) =>
    board.map((row) => row.map((n) => (n == number ? "X" : n)))
  );
}

function checkWinner(boards) {
  let column = checkColumn(boards);
  let row = checkRow(boards);
  if (row[0]) {
    return row;
  } else if (column[0]) {
    return column;
  } else {
    return [false, boards];
  }
}

function checkRow(boards) {
  let isRowCompleted = false;
  for (board of boards) {
    for (row of board) {
      let count = 0;
      for (num of row) {
        if (num === "X") count++;
      }
      if (count === 5) {
          if(boards.length !== 1){
            boards = boards.filter((b) => b !== board);
          }
        isRowCompleted = true;
      }
      //if (count === 5) return [true, board];
    }
  }
  return [isRowCompleted, boards];
}

function checkColumn(boards) {
  let isColumCompleted = false;
  for (board of boards) {
    for (let x = 0; x < board.length; x++) {
      let count = 0;
      for (let y = 0; y < board.length; y++) {
        if (board[y][x] == "X") {
          count++;
        }
      }
      if (count === 5) {
        isColumCompleted = true;
        if(boards.length !== 1){
            boards = boards.filter((b) => b !== board);
        }
        //return [true, board];
      }
    }
  }
  return [isColumCompleted, boards,];
}
