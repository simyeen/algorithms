const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

var x = 0;
var y = 0;

function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;
  let q = [[x, y, 1]];

  while (q.length > 0) {
    console.log(q);
    let cur = q.shift();
    x = cur[0];
    y = cur[1];
    const dist = cur[2];
    maps[x][y] = 0;

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (0 <= nx && nx < n && 0 <= ny && ny < n) {
        if (maps[nx][ny] === 0) {
          continue;
        } // 벽이거나 이미 지나온 곳 이면

        if (nx === n - 1 && ny === m - 1) {
          return dist + 1;
        }

        if (maps[nx][ny] === 1) {
          q.push([nx, ny, dist + 1]);
        }
      }
    }

    // for (let k = 0; k < n; k++) {
    //   console.log(maps[k]);
    // }
    // console.log();
  }

  return -1;
}

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ])
);
