from flask import Flask, session, render_template, redirect, request, make_response 
from flask_session import Session
from collections import defaultdict

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def get_result(query, category, acts, judge, start_date, end_date):
    '''
    returns query output as list
    '''
    return 1
def make_recent(query, category, acts, judge, store=""):
    '''
    returns string which is stored in a cookie for showing recent queries
    '''
    if len(query) > 1:
        store += query
    if len(category) > 1:
        store += " " + category
    if len(acts) > 1:
        store += " " + category
    if len(judge) > 1:
        store += " " + judge
    return store

@app.route("/", methods = ['GET'])
def index():
    if 'search' in request.form:
        #extracting information from form
        query = request.form['query']
        category = request.form['category']
        acts = request.form['acts']
        judge = request.form['judge']
        start_date = request.form['from']
        end_date = request.form['to']
        print(f"query is {query}, category is {category}, acts is {acts}, judge is {judge}, start date is {start_date}")
        #Add this search in recents
        recent = session["recent"]
        store = ""
        store = make_recent(query=query, category=category, acts=acts, judge=judge, store=store)
        recents = session["recent"]
        recents.append(store)
        # get results
        output = get_result(query=query, category=category, acts=acts, judge=judge, start_date=start_date, end_date=end_date)
        # pass the list to be displayed to index.html and render index.html
        return render_template('search.html', output=output)
    else :
        if 'recent' not in session:
            session["recent"] = []
        recents = session["recent"]
        for x in recents:
            print(f"x is {x}")
        return render_template('index.html', recents=recents)

@app.route("/cases/<string:case_id>", methods = ['GET'])
def cases(case_id):
    return render_template('case.html', case_id=case_id)

@app.route("/search", methods=['GET'])
def search():
    return render_template('search.html')

