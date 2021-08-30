'use strict'

console.log(1);

setTimeout(function () {
  console.log(-1);
}, 1000);
console.log(2);
console.log(3);

// 콜백지옥 구현해보기

class UserStorage{
    loginUser(id, password, onSuccess, onError){
        setTimeout(()=>{ },2)
    }

    getRoles(user, onSueccess, onError)


}

