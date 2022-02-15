$(function () {
  addName()
});
url = 'https://swapi-api.hbtn.io/api/films/?format=json'
async function addName() {
  await $.getJSON(url, function (res) {
    for (let i of res.results) {
      $('#list_movies').append(`<li>${i.title}</li>`)
    }
  });
};
