#!/usr/bin/env python3

import json
from collections import namedtuple, OrderedDict
from flask import Flask, Response, request
from flask_caching import Cache
import pandas as pd

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE' : 'simple'})

@app.route("/get_voters_where")
def get_voters():
	args = request.args

	@cache.memoize(50)
	def get_data():
		return pd.read_csv("data.csv", sep=';', parse_dates=['Date'])
	df = get_data()
	headers = list(df)
	votersCols = [header for header in headers if '-' in header]

	if args.get('county'): df = df[df['County'] == args['county']]
	if args.get('month'): df = df[df['Date'].dt.month == int(args['month'])]
	if args.get('limit'): df = df.iloc[:int(args['limit'])]
	if args.get('party'): headers = [header for header in headers if header.split(' - ')[0] == args['party']]
	if args.get('status'): headers = [header for header in headers if header.split(' - ')[1] == args['status']]

	cols = ['Date', 'County', 'Grand Total'] + headers
	js = json.dumps(df[cols].to_dict('records'), default=str)
	resp = Response(js, status = 200, mimetype='application/json')
	return resp

@app.route("/")
def default_uri():
	data = {'first': 'word', 'second': 2}
	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='applicaiton/json')
	return resp

if __name__ == "__main__":
	app.run()
