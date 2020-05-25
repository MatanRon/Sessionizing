import config


def create_new_session(record):
    """
    creates new session with length 0 from a given site visit
    time complexity: O(1)
    space complexity: O(1)
    """
    return {'visitor_id': record['visitor_id'],
            'site_url': record['site_url'],
            'first_timestamp': record['timestamp'],
            'length': 0}


def create_sessions(data):
    """
    This method receives unprocessed data (separate site visits) and produces sessions from it.
    A session is defined as a group of page views of a single visitor to a single site such that the time between
    every two successive page views is not longer than 30 minutes.

    param: list of separate sites visits
    output: A list of all site visits grouped together into sessions

    time complexity: O(n)
    space complexity: O(n)
    n is the total number of page views
    assuming the time complexity of append() is O(1)
    """
    sessions = []
    current_session = create_new_session(data[0])
    for record in data[1:]:
        if(record['site_url'] == current_session['site_url'] and
            record['visitor_id'] == current_session['visitor_id'] and
            int(record['timestamp']) - int(current_session['first_timestamp']) - int(current_session['length']) <= config.TIME_BETWEEN_PAGES):
            current_session['length'] = int(record['timestamp']) - int(current_session['first_timestamp'])
        else:
            sessions.append(current_session)
            current_session = create_new_session(record)

    sessions.append(current_session)
    return sessions


def create_site_url_sessions(data):
    """
    input: list of all site visits (page views)
    output: session list sort by site_url then by visitor_id and then by timestamp

    time complexity: O(n)
    space complexity: O(n)
    n is the total number of page views
    """
    data.sort(key=lambda entry: (entry['site_url'], entry['visitor_id'], entry['timestamp']))
    sites_sessions = create_sessions(data)
    return sites_sessions


def create_visitor_id_sessions(data):
    """
    input: list of all site visits
    output: session list sort by visitor_id then by site_url and then by timestamp

    time complexity: O(n)
    space complexity: O(n)
    n is the total number of page views
    """
    data.sort(key=lambda entry: (entry['visitor_id'], entry['site_url'], entry['timestamp']))
    visitors_sessions = create_sessions(data)
    return visitors_sessions
