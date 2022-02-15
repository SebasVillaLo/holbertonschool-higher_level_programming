$(function () {
  addName()
});
url = 'https://fourtonfish.com/hellosalut/?lang=fr'
function addName() {
  $.getJSON(url, function (json) {
    $('#hello').append(json.hello)
  });
};
