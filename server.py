from flask import Flask
from flask import Response, request
import queries
import json
from data_base import SingletonDataBase

app = Flask(__name__, static_url_path='')

# TODO: remove code duplications


@app.route('/')
def index():
    return app.send_static_file(filename='index.html')

@app.route('/number_of_sessions_get/', methods=['POST'])
def number_of_sessions():
    """
    This function will be called every time the user will send "number_of_sessions" query.
    The function will extract the information needed for the calculation
    and will pass it to the appropriate function in the queries handling module.
    Finally, will send a response which will include the query result to the user.

    time complexity: O(n)
    space complexity: O(n)
    n is the total number of sessions
    """
    session_site_url = json.loads(request.data)['session_site_url']
    try:
        sites_sessions = SingletonDataBase.get_instance().get_sites_sessions_data()
        query_result = queries.num_sessions(sites_sessions, session_site_url)
        result = 'The number of sessions is ' + str(query_result)
    except ValueError as e:
        result = str(e)
    response = Response(status=200)
    response.data = str(result)
    return response


@app.route('/median_length_get/', methods=['POST'])
def median_session_length():
    """
    This function will be called every time the user will send "median_session_length" query.
    The function will extract the information needed for the calculation
    and will pass it to the appropriate function in the queries handling module.
    Finally, will send a response which will include the query result to the user.

    time complexity: O(n)
    space complexity: O(n)
    n is the total number of sessions
    """
    median_site_url = json.loads(request.data)['site_url']
    try:
        sites_sessions = SingletonDataBase.get_instance().get_sites_sessions_data()
        query_result = queries.median_session_length(sites_sessions, median_site_url)
        result = 'The median  session length is ' + str(query_result)
    except ValueError as e:
        result = str(e)
    response = Response(status=200)
    response.data = str(result)
    return response


@app.route('/number_of_visited_sites_get/', methods=['POST'])
def number_of_unique_visited_sites():
    """
    This function will be called every time the user will send "number_of_unique_visited_sites" query.
    The function will extract the information needed for the calculation
    and will pass it to the appropriate function in the queries handling module.
    Finally, will send a response which will include the query result to the user.

    time complexity: O(n)
    space complexity: O(n)
    n is the total number of sessions
    """
    visitor_id = json.loads(request.data)['visitor_id']
    try:
        visitors_sessions = SingletonDataBase.get_instance().get_visitors_sessions_data()
        query_result = queries.num_unique_visited_sites(visitors_sessions, visitor_id)
        result = 'The number of unique visited sites is ' + str(query_result)
    except ValueError as e:
        result = str(e)
    response = Response(status=200)
    response.data = str(result)
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False, threaded=True)
