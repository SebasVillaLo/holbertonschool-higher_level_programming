$(function () {
  addlist();
  removelist();
  cleanlist();
});
let count = 1;
function addlist() {
  $('#add_item').on('click', function () {
    $('.my_list').append('<li>Item</li>')
    count++;
  })
};
function removelist() {
  $('#remove_item').on('click', function () {
    $('.my_list li').slice(count - 1).remove()
    count--;
  })
};
function cleanlist() {
  $('#clear_list').on('click', function () {
    $('.my_list').empty();
    count = 1;
  })
};