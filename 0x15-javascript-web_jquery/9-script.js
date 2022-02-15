$(function () {
  addName()
});
url = 'https://fourtonfish.com/hellosalut/?lang=fr'
let count = 0;
function addName() {
  $.getJSON(url, function (json) {
    $('#hello').append(json.hello)
  });
};
