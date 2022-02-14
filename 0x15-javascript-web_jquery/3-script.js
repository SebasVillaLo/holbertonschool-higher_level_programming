$(function () {
  clickMe()
});

function addclass() {
  $('header').addClass('red');
};
function clickMe() {
  $('#red_header').on('click', function () {
    addclass();
  })
};
