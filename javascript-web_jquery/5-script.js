$(document).ready(function() {
    $('#add_item').on('click', function() {
        const newelement = $('<li>Item<li/>')
        $('my_list').append(newelement)
    });
})