// 1. 버블 정렬

const arr = [9, 8, 7, 6, 5, 4, 3, 2, 1];
var n = arr.length;
function selectSort(arr) {
  console.log("in");
  let min_index = 0;
  for (let i = 0; i < n - 1; i++) {
    min_index = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[min_index] > arr[j]) min_index = j;
    }

    let tmp;
    tmp = arr[i];
    arr[i] = arr[min_index];
    arr[min_index] = tmp;
  }
  console.log("out");
}

selectSort(arr);
console.log("after", arr);

// function bubbleSort(arr) {
//   for (let i = arr.length; i > 0; i--) {
//     for (let j = 0; j < i - 1; j++) {
//       if (arr[j] > arr[j + 1]) {
//         let temp = arr[j];
//         arr[j] = arr[j + 1];
//         arr[j + 1] = temp;
//         noSwaps = false;
//       }
//     else{ break}
//   }
//   console.log(arr);
//   return arr;
// }

//bubbleSort(arr);

// 2. 선택 정렬

// 3. 삽입 정렬

// function insertSort(arr) {
//   for (let i = 0; i < n; i++) {
//     for (let j = i; j > 0; j--) {
//       if (arr[j - 1] > arr[j]) {
//         let tmp;
//         tmp = arr[j - 1];
//         arr[j - 1] = arr[j];
//         arr[j] = tmp;
//       } else {
//         break;
//       }
//     }
//   }
// }

//insertSort(arr);
//console.log("after", arr);
