from flask import Flask, render_template, request
from recs import get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/recommend', methods=['post'])
def recommmend():
	anime_title = request.form['title']
	recommendations = get_recommendations(anime_title)
	return render_template('recommend.html', title=anime_title,recommendations=recommendations)
if __name__ == '__main__':
	app.run(debug=True)
