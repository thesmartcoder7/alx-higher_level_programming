(function () {
  document.addEventListener('DOMContentLoaded', function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
      if (textStatus === 'success') {
        $('DIV#hello').text(data.hello);
      } else {
        $('DIV#hello').text('Error');
      }
    });
  }, false);
})();
