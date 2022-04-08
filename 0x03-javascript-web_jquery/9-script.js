$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
// fetches from https://fourtonfish.com/hellosalut/?lang=fr displays value of hello from fetch in tag DIV#hello
