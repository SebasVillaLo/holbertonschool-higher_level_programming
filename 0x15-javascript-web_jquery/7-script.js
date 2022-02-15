$(function () {
  addName()
});
url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
async function addName() {
  await $.getJSON(url, function (res) {
    $('#character').append(res.name)
  });
};
