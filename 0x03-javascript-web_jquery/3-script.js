$('div#red_header').click(function () {
    if (!$('header').hasClass('red')) {
      $('header').addClass('red');
    }
  });
// adds class red to <header> when user clicks on DIV#red_header