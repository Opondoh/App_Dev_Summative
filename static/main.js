$(document).ready(function () {
    $('.table').Tabledit({
      editButton: false,
      deleteButton: false,
      hideIdentifier: true,
      columns: {
        identifier: [1, 'Date Of Month'],
        editable: [[0], [1], [2], [3], [4], [5], [6], [6], [7],[8],[9], [10], [11]]
      }
    });
  });