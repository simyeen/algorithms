// 1. async  /
// 기존
function fetchUser1() {
  return new Promise((resolve, reject) => {
    resolve("네트워크에서 받아온 데이터");
  });
}

// async 이용하면??
async function fetchUser2() {
  return "네트워크에서 받아온 데이터";
}

const user1 = fetchUser1();
const user2 = fetchUser2();

console.log(user1, user2);
