from statistics import median


def num_sessions(sites_sessions, site_url):
    """
    params: sites_sessions: Session list sorted by site_url
            site_url: The URL whose number of sessions will be calculated for
    return: Number of sessions of the given URL

    time complexity: O(n)
    space complexity: O(m)
    n is the total number of sessions
    m is the number of sessions of the given URL
    """
    session_for_url = [session for session in sites_sessions if session['site_url'] == site_url]
    if len(session_for_url) > 0:
        return len(session_for_url)
    raise ValueError("Error: No such URL in the data base")


def median_session_length(sites_sessions, site_url):
    """
    params: sites_sessions: Session list sorted by site_url
            site_url: The URL whose median session length will be calculated for
    return: The length of the median session of the given URL

    time complexity: O(n)
    space complexity: O(m)
    n is the total number of sessions
    m is the number of sessions of the given URL
    assuming median time complexity is O(m) and space complexity is O(1)
    """
    session_lengths = [session['length'] for session in sites_sessions if session['site_url'] == site_url]
    if len(session_lengths) > 0:
        return median(session_lengths)
    raise ValueError("Error: No such URL in the data base")


def num_unique_visited_sites(visitors_sessions, visitor_id):
    """
    params: visitors_sessions: Session list sorted by visitor_id
            visitor_id: The id of the visitor whose number of unique visited sites will be calculated for
    return: The number of unique visited sites of the given visitor

    time complexity: O(n)
    space complexity: O(m)
    n is the total number of sessions
    m is the number of sessions of the given visitor
    """
    visited_sites = [session['site_url'] for session in visitors_sessions if session['visitor_id'] == visitor_id]
    if len(visited_sites) > 0:
        return len(set(visited_sites))
    raise ValueError("Error: No such user in the data base")
