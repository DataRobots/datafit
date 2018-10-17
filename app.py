from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/about")
def about():
    """Return the homepage."""
    return render_template("about.html")

@app.route("/analysis")
def analysis():
    """Return the homepage."""
    return render_template("analysis.html")



@app.route('/data_scientist')
def get_keywords():
	
	conn = sqlite3.connect('file:./ResumeAnalyzer.sqlite?mode=ro',uri=True)
	cur = conn.cursor()
	query = 'SELECT keywords, score FROM keywords_data_scientist ORDER BY score DESC LIMIT 10'
	query_education = 'SELECT keywords, score FROM keywords_data_scientist WHERE keywords IN (\'phd\',\'masters\',\'bachelor\') ORDER BY score DESC LIMIT 10'
	query_tool = 'SELECT keywords, score FROM keywords_data_scientist WHERE keywords IN (\'hive\',\'tableu\',\'python\',\'excel\',\'spark\',\'sql\') ORDER BY score DESC LIMIT 10'
	results = cur.execute(query)
	
	keyword = []
	score = []
	for result in results:
		keyword.append(result[0])
		score.append(result[1])

	education_results = cur.execute(query_education)

	education = []
	edu_score = []
	for result in results:
		education.append(result[0])
		edu_score.append(result[1])
	tool =[]
	tool_score =[]

	tools_results = cur.execute(query_tool)
	for result in results:
		tool.append(result[0])
		tool_score.append(result[1])

	plot_trace = {'plot1':{
	 "x": keyword,
	 "y":score,
	 "type": "bar"
	}, 'plot2':{
		"x": education,
	 "y":edu_score,
	 "type": "bar"
	},

	'plot3':{
		"x": tool,
	 "y":tool_score,
	 "type": "bar"
	}}

	conn.close()
	return jsonify(plot_trace)
@app.route('/data_analyst')
def get_keywords_da():
	conn = sqlite3.connect('file:./ResumeAnalyzer.sqlite?mode=ro',uri=True)
	cur = conn.cursor()
	query = 'SELECT keywords, score FROM keywords_data_analyst ORDER BY score DESC LIMIT 10'
	query_education = 'SELECT keywords, score FROM keywords_data_analyst WHERE keywords IN (\'phd\',\'masters\',\'bachelor\') ORDER BY score DESC LIMIT 10'
	query_tool = 'SELECT keywords, score FROM keywords_data_analyst WHERE keywords IN (\'hive\',\'tableu\',\'python\',\'excel\',\'spark\',\'sql\') ORDER BY score DESC LIMIT 10'
	results = cur.execute(query)
	
	keyword = []
	score = []
	for result in results:
		keyword.append(result[0])
		score.append(result[1])

	education_results = cur.execute(query_education)

	education = []
	edu_score = []
	for result in results:
		education.append(result[0])
		edu_score.append(result[1])
	tool =[]
	tool_score =[]

	tools_results = cur.execute(query_tool)
	for result in results:
		tool.append(result[0])
		tool_score.append(result[1])

	plot_trace = {'plot1':{
	 "x": keyword,
	 "y":score,
	 "type": "bar"
	}, 'plot2':{
		"x": education,
	 "y":edu_score,
	 "type": "bar"
	},

	'plot3':{
		"x": tool,
	 "y":tool_score,
	 "type": "bar"
	}}

	conn.close()
	return jsonify(plot_trace)

@app.route('/data_engineer')
def get_keywords_de():
	
	conn = sqlite3.connect('file:./ResumeAnalyzer.sqlite?mode=ro',uri=True)
	cur = conn.cursor()
	query = 'SELECT keywords, score FROM keywords_data_engineer ORDER BY score DESC LIMIT 10'
	query_education = 'SELECT keywords, score FROM keywords_data_engineer WHERE keywords IN (\'phd\',\'masters\',\'bachelor\') ORDER BY score DESC LIMIT 10'
	query_tool = 'SELECT keywords, score FROM keywords_data_engineer WHERE keywords IN (\'hive\',\'tableu\',\'python\',\'excel\',\'spark\',\'sql\') ORDER BY score DESC LIMIT 10'
	results = cur.execute(query)
	
	keyword = []
	score = []
	for result in results:
		keyword.append(result[0])
		score.append(result[1])

	education_results = cur.execute(query_education)

	education = []
	edu_score = []
	for result in results:
		education.append(result[0])
		edu_score.append(result[1])
	tool =[]
	tool_score =[]

	tools_results = cur.execute(query_tool)
	for result in results:
		tool.append(result[0])
		tool_score.append(result[1])

	plot_trace = {'plot1':{
	 "x": keyword,
	 "y":score,
	 "type": "bar"
	}, 'plot2':{
		"x": education,
	 "y":edu_score,
	 "type": "bar"
	},

	'plot3':{
		"x": tool,
	 "y":tool_score,
	 "type": "bar"
	}}

	conn.close()
	return jsonify(plot_trace)

if __name__ == '__main__':
	app.run()