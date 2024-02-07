$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }),
      function (datat) {
        $('DIV#hello').html(data.hello);
      });
  });
});
