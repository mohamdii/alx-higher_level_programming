$(function () {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", async function (data) {
        if (data && data.results != null)
            data.results.forEach(item => {
                $('#list_movies').append(`<li>${item.title}</li>`)
            });
    })
});