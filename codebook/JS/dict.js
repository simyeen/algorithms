function solution(clothes) {
  const n = clothes.length;
  var dict = {};

  for (let i = 0; i < n; i++) {
    key = clothes[i][1];
    value = clothes[i][0];

    if (key in dict) dict[key]++;
    else dict[key] = 1;
  }

  var sum_value = 0;
  var mul_value = 1;
  for (var key in dict) {
    sum_value += dict[key];
    mul_value *= dict[key];
  }

  return sum_value + mul_value;
}

console.log(
  solution([
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
  ])
);

// 사전에 clothes[1]를 key로 카운트한다.
//
