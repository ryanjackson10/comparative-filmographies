# comparative-filmographies
running using the Flask framework on ryanjackson.pythonanywhere.com.

enter one or two names into the search bar, and if they're both in the JSON file that's stored, then it'll show an interactive line chart of their filmographies, with the y-axis values being their audience scores on TMDB. EXAMPLE: https://imgur.com/a/2EpqBhp

Notes
- I originally had it so that it made an API call for every request, but that took too much time, especially if they had a large filmography (Tom Hanks alone was around 13 seconds). So instead I put a bunch of the data in a JSON file. I have ~17,000 people and their filmographies in the that file, but some notable people are still missing (Jordan Peele for one). 
- For directors I tried to make it so that they only get credit for films they had a significant hand in making. The API I used gave Quentin Tarantino "credit" for around 27 films, which obviously isn't very indicative of his filmography.
- If you hover over a data point, it'll show the name of the film and the rating it received. If there are two points in the same area, it'll show both data points, like this: https://imgur.com/a/o2rxbLQ
- names have to be spelled correctly, but it isn't case sensitive. "DaNieL dAy-LewiS" works, but "daniel day lewis" and "Daniel Day- Lewis " don't.
Future Improvements
- the domain, for one. I'm running it on a paid PythonAnywhere account, so that should be no problem
- the ratings? I used TMDB ratings since it was the internal rating system for the API I used. Perhaps I'll make an option to see Rotten Tomatoes scores as well?
- the aesthetic of the homepage. I really don't know that much HTML and the one html file I made(the homepage) only amounted to 10 lines of code. If anybody who knows HTML were to spice that up a bit it'd be amazing.
- add more names to the JSON file?
- When you hover on the line where there's no data it shows this: https://imgur.com/a/Xq1N4bB
- possibly a Google-style dropdown search bar to prevent misspellings
