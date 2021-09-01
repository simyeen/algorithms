// 전역에서의 this
console.log(this); // Window {...}

// 전역 스코프 함수에서의 this
function foo() {
  console.log(1, this);

  foo2();
  function foo2() {
    console.log(2, this);
  }
} // Window {...}

foo();
