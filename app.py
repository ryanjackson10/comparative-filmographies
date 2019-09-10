import flask
from flask import Flask
from flask import request
from flask import render_template
from bokeh.layouts import row
from bokeh.plotting import figure
import os
from bokeh.models import ColumnDataSource
import json
from bokeh.plotting import output_file, ColumnDataSource
from bokeh.io import output_file, output_notebook, push_notebook, show, save
from bokeh.resources import CDN
from bokeh.embed import file_html


output_notebook()

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    try:
        text = request.form['FirstName'].lower()
        text2 = request.form['LastName'].lower()
        if text != '' and text2 == '':

            with open('data.json','r') as j:
                json_data = json.load(j)
                ans = json_data[text]
                movies = ans[0]
                moviescores = ans[1]
                index = [] #since this uses TMDB instead of Rotten Tomatoes, I put in thin lines across the graph at 6.0,
                average = []#TMDB's average rating, and 7.6, a score that puts a film around the 90th percentile. These are
                nintieth = []#for scale, since a "good score" on TMDB is a lot different than a "good score" on RT.
                for i in range(len(movies)):
                    nintieth.append(7.5)
                for i in range(len(movies)):
                    index.append(i)
                for i in range(len(movies)):
                    average.append(6)


            source = ColumnDataSource(data=dict(
            x = index,
            y = moviescores,
            movies = movies,
            scores = moviescores

            ))

            TOOLTIPS = [
            ('Film','@movies'), #for the hover tools
            ('TMDB score','@scores')
            ]

            p = figure(plot_width=1200, plot_height=575, y_range=(0,10), tooltips=TOOLTIPS,
            title="")
            p.line(x=index,y=average,color='red',line_width=1,legend='Average TMDB Score')
            p.line(x=index,y=nintieth,color='green',line_width=1,legend='90th Percentile TMDB Score')
            p.line(x=index,y=moviescores,color='black',line_width=2,legend=text.upper())


            p.circle('x', 'y', size=20,source=source,alpha=0,hover_alpha=0.5)
            graph = save(p)
            html = file_html(p,CDN,"plot") #the show(p) technically returns none, which is invalid. We have to return the
            return str(html)               #html file it generates instead




        if text != '' and text2 != '':

            with open('data.json','r') as j:
                json_data = json.load(j)
                ans = json_data[text]
                ans2 = json_data[text2]
                movies_ = ans2[0]
                moviescores_ = ans2[1]
                movies = ans[0]
                moviescores = ans[1]
                index = []
                index_ = []
                average = []
                nintieth = []
                for i in range(len(movies)):
                    nintieth.append(7.5)
                for i in range(len(movies)):
                    index.append(i)
                for i in range(len(movies_)):
                    average.append(6)
                for i in range(len(movies_)):
                    index_.append(i)

            maxindex = []
            maxrange = max(len(index),len(index_))
            for i in range(maxrange):
                maxindex.append(i)
            average = []
            nintieth = []
            for i in range(maxrange):
                average.append(6)
                nintieth.append(7.5)


            source = ColumnDataSource(data=dict(
            x = index+index_,
            y = moviescores+moviescores_,
            movies = movies+movies_,
            scores = moviescores+moviescores_

            ))

            TOOLTIPS = [
            ('Film','@movies'),
            ('TMDB score','@scores')
            ]

            p = figure(plot_width=1200, plot_height=575, y_range=(0,10), tooltips=TOOLTIPS,
            title="")

            p.line(x=maxindex,y=average,color='red',line_width=1,legend='Average TMDB Score')
            p.line(x=maxindex,y=nintieth,color='green',line_width=1,legend='90th Percentile TMDB Score')
            p.line(x=index,y=moviescores,color='black',line_width=2,legend=text.upper())
            p.line(x=index_,y=moviescores_,color='blue',line_width=2,legend=text2.upper())


            p.circle('x', 'y', size=20,source=source,alpha=0,hover_alpha=0.5)

            graph = save(p)
            html = file_html(p,CDN,"plot")
            #file1.close()
            return str(html)


        elif text == '' and text2 != '':
            with open('data.json','r') as j:
                json_data = json.load(j)
                ans = json_data[text2]
                movies = ans[0]
                moviescores = ans[1]
                index = []
                average = []
                nintieth = []
                for i in range(len(movies)):
                    nintieth.append(7.5)
                for i in range(len(movies)):
                    index.append(i)
                for i in range(len(movies)):
                    average.append(6)


            source = ColumnDataSource(data=dict(
            x = index,
            y = moviescores,
            movies = movies,
            scores = moviescores
            #scores = moviescores_,
            #filmtitles = movies_titles,

            ))

            TOOLTIPS = [
            ('Film','@movies'),
            ('TMDB score','@scores')
            ]

            p = figure(plot_width=1200, plot_height=575, y_range=(0,10), tooltips=TOOLTIPS,
            title="")
            p.line(x=index,y=average,color='red',line_width=1,legend='Average TMDB Score')
            p.line(x=index,y=nintieth,color='green',line_width=1,legend='90th Percentile TMDB Score')
            p.line(x=index,y=moviescores,color='black',line_width=2,legend=text2.upper())


            p.circle('x', 'y', size=20,source=source,alpha=0,hover_alpha=0.5)
            return str(html)

    except KeyError: #in case the name is misspelled and/or isn't in the data.json file
        return 'One of both of your inputs are either misspelled or not in the database!'


if __name__ == "__main__":
    app.run(debug=True)
