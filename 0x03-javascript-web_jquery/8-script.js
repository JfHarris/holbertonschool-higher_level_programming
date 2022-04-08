$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const results = data.results;
  $.each(results, function (key, value) {
    $('#list_movies').append('<li>' + value.title + '</li>');
  });
});
// fetches/lists title for all movies using URL: https://swapi-api.hbtn.io/api/films/?format=json
