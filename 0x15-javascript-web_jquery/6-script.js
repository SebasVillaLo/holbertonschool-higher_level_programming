$(function () {
  clickMe()
});

function clickMe() {
  $('#update_header').on('click', function () {
    addtext();
  })
};
function addtext() {
  $('header').empty()
  $('header').append('New Header!!!')
}