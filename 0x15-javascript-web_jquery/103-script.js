$(function () {
  function translate () {
    $.get('https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), function (dat, status) {
      if (status === 'success') {
        $('DIV#hello').text(dat.hello);
      } else {
        $('DIV#hello').text('Error');
      }
    });
  }

  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      translate();
    }
  });
});
