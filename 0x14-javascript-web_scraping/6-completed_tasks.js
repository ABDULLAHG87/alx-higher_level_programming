#!usr/bin/node

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const completed = {};

  body.forEach((todo) => {
    if (todo.completed && !completed[todo.userId]) {
      completed[todo.userId] = 1;
    } else {
      completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});
