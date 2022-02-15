$(function () {
  clickMe()
});

function clickMe() {
  $('#update_header').on('click', function () {
    addtext();
  })
};
function addtext() {
  $('header').empty().append('New Header!!!')
}