import requests
from flask import Flask, render_template, render_template_string, request


app = Flask(__name__)


@app.route('/get_media/')
def get_media():
    return render_template("/get_media.html")

@app.route('/choice/', methods = ['POST', 'GET'])
def choice():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        selection = request.form
        if 'movies' in selection.values():
            return render_template('/movies.html')
        elif 'series' in selection.values():
            return render_template('/series.html')

@app.route('/movie/')
def movies():
    return render_template("/movies.html")

@app.route('/get_movies/', methods = ['POST', 'GET'])
def get_movies():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        movie_name = request.form.get('movie_name')
        url = "media:7878/api/v3/movies?apiKey=10fc753d66e048009a1d7fbc3a8f8053"
        params = {'title': movie_name}
        return request.args.get(url)

@app.route('/series/')
def series():
    return render_template("/movies.html")

@app.route('/get_series/', methods = ['POST', 'GET'])
def get_series():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        series_name = request.form
        return series_name.get('series_name')




if __name__ == "__main__":
    app.run()
