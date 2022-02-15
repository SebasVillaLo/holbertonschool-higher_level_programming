$(function () {
  clickMe()
});

function clickMe() {
  $('#add_item').on('click', function () {
    divadd();
  })
};
function divadd() {
  $('.my_list').append('<li>Item</li>')
}