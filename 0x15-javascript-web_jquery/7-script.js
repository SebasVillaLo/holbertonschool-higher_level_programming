$(function () {
  addName()
});
url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
function addName() {
  $.getJSON(url, function (json) {
    $('#character').append(json.name)
  });
};
