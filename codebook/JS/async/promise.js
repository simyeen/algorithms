"use strict";

// 1. 프로듀서
const promise = new Promise((resolve, reject) => {
  console.log("doing something...");
  setTimeout(() => {
    resolve("namil");
  }, 2000);
});

// 2. 컨슈머 then, catch, finally

const getHen = () =>
  new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("닭");
    }, 1000);
  });
