$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  const charName = data.name;
  $('DIV#character').text(charName);
});
// fetches the char name from URL: https://swapi-api.hbtn.io/api/people/5/?format=json
