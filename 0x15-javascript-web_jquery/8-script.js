$(function () {
  addName()
});
url = 'https://swapi-api.hbtn.io/api/films/?format=json'
let count = 0;
function addName() {
  $.getJSON(url, function (json) {
    for (let i of json.results) {
      $('#list_movies').append(`<li>${count++} ${i.title}</li>`)
    }
  });
};
