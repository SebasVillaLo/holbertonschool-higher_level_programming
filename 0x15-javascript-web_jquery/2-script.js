$(function () {
  clickMe()
});

function changeColor() {
  $('header').css('color', '#FF0000');
};
function clickMe() {
  $('#red_header').on('click', function () {
    changeColor();
  })
};
