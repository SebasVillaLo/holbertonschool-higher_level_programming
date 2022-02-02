#!/usr/bin/node
const request = require('request');
const argv = process.argv.slice(2);
request(argv[0], function (err, r, body) {
  if (err) { console.log(err); }
  const Res = {};
  const string = JSON.parse(body);
  for (const i of string) {
    if (i.completed) {
      if (Res[i.userId] === undefined) {
        Res[i.userId] = 1;
      } else {
        Res[i.userId] += 1;
      }
    }
  }
  console.log(Res);
});
