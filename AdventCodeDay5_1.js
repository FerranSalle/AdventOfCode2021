const { default: async } = require("async");

const fs = require("fs"),
  filename = "values1.txt";

fs.readFile(filename, "utf8", function (err, data) {
  if (err) throw err;
  console.log("OK: " + filename);
  const dades = data.split("\r\n");
  let points = dades.map(p => p.split("->").map(n=> n.split(',').map(n=> parseInt(n))))
  let matrix = Array(maxValue(points, points.length-1,0))
  for(let i=0; i< matrix.length; i++){
      matrix[i] = new Array(matrix.length).fill(0)
  }
  //Start Program

  for(row of points){
    let vector = {x: row[1][0]-row[0][0], y: row[1][1]-row[0][1]}
    for
  }
});

function maxValue(arr, n, max){
if(n>0){    
    if(arr[n][0][0] > max) {
        return maxValue(arr, n-1, arr[n][0][0])
    }else{
        return maxValue(arr, n-1, max)
    }
}else {
    return max
}
}