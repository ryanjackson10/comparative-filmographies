#not actually in the directory that's running the site, just how I generated the data for the data.json file

count = 1
goal = 20250

actors = ['Acting']
dir_terms = ['Writer','Screenplay','Director','Directing','Writing','Producer']
prod_terms = ['Writer','Screenplay','Director','Producer','Executive Producer']

while goal>count:
    try:
        person = tmdb.People(count)
        name = tmdb.People(count).info()['name']
        movies = person.movie_credits()
        film = []
        ratings = []
        voters = []
        r = len(ratings)
        if 'Act' in tmdb.People(count).info()['known_for_department']:
            for i in range(0,len((movies)['cast'])):
                film.append(movies['cast'][i]['original_title'])
            for i in range(0,len((movies)['cast'])):
                ratings.append(movies['cast'][i]['vote_average'])
            for i in range(0,len((movies)['cast'])):
                low_votes = movies['cast'][i]['vote_count']
                if low_votes < 20:
                    voters.append(low_votes)

            index = []
            f = []
            s = []

            for i in range(len(ratings)):
                if movies['cast'][i]['vote_count'] in voters:
                    pass
                else:
                    f.append(ratings[i])
                    s.append(film[i])
            data[name.lower()] = [s,f]
            count+=1
            if count%10 == 0:
                time.sleep(5)
        elif tmdb.People(count).info()['known_for_department'] in dir_terms:
            for i in range(0,len((movies)['crew'])):
                if movies['crew'][i]['job'] in dir_terms:
                    film.append(movies['crew'][i]['original_title'])
            for i in range(0,len((movies)['crew'])):
                if movies['crew'][i]['job'] in dir_terms:
                    ratings.append(movies['crew'][i]['vote_average'])
            for i in range(0,len((movies)['crew'])):
                if movies['crew'][i]['job'] in dir_terms:
                    voters.append(movies['crew'][i]['vote_count'])

            index = []
            c = []
            e = []

            for i in range(len(ratings)):
                if voters[i] < 10: #weed out films with less than 10 ratings
                    continue
                else:
                    c.append(ratings[i])
                    e.append(film[i])
            s = []
            f = []
            for j in range(len(e)-1): #a lot of times directors are credited as producers, directors, and screenwriters (or
                if e[j] in s:         #some combination) for films, causing them to appear multiple times.
                    pass          
                else:
                    s.append(e[j])
                    f.append(c[j])
            data[name.lower()] = [s,f]
            count+=1
            if count%10 == 0:
                time.sleep(5)
        else:
            for i in range(0,len((movies)['crew'])):
                if movies['crew'][i]['job'] in prod_terms:
                    film.append(movies['crew'][i]['original_title'])
            for i in range(0,len((movies)['crew'])):
                if movies['crew'][i]['job'] in prod_terms:
                    ratings.append(movies['crew'][i]['vote_average'])
            for i in range(0,len((movies)['crew'])):
                if movies['crew'][i]['job'] in prod_terms:
                    voters.append(movies['crew'][i]['vote_count'])

            index = []
            c = []
            e = []

            for i in range(len(ratings)):
            #if movies['crew'][i]['job'] in prod_terms:
                if voters[i] < 10:
                    pass
                else:
                    c.append(ratings[i])
                    e.append(film[i])
            s = []
            f = []
            for j in range(len(e)-1):
                if e[j] == e[j+1]:
                    pass
                else:
                    s.append(e[j])
                    f.append(c[j])
            data[name.lower()] = [s,f]
            count+=1
            if count%10 == 0: #the maximum amount of requests during the loop is 10
                time.sleep(3)

    except requests.exceptions.HTTPError: #TMDB doesn't have a person assigned to every number. If a number doesn't match to
        count+=1                          #a person it throws this error
        if count%10 == 0:
            time.sleep(3)


with open('the_data.json','w') as outfile:
    json.dump(data,outfile)
