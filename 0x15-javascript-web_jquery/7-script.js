$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data) {
      $('#DIV#character').text(data.name);
    });
});
