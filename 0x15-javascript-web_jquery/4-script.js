$(function () {
  clickMe()
});
function clickMe() {
  $('#toggle_header').on('click', function () {
    nextclass();
  })
};

function nextclass() {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else {
    $('header').removeClass('red').addClass('green');
  }
};
// hacerlo con toggleclass es aburrido :D