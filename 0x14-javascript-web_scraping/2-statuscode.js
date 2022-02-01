#!/usr/bin/node
const axios = require('axios');
const argv = process.argv.slice(2);

axios.get(argv[0]).then(res => {
  console.log(`statusCode: ${res.status}`)
  console.log(res);
}).catch(error => {
  console.error(error);
});
