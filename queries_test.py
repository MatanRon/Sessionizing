import unittest
import queries
import utils
import tests_data

from data_base import SingletonDataBase, UnprocessedDataBase

class TestQueries(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestQueries, self).__init__(*args, **kwargs)
        args = utils.parse_args()
        csvs_folder = args.csvs_folder
        unprocessed_data = UnprocessedDataBase(csvs_folder)
        db = SingletonDataBase.get_instance()
        db.set_database(unprocessed_data.get_data())

        self.sites_session_list = SingletonDataBase.get_instance().get_sites_sessions_data()
        self.visitors_sessions = SingletonDataBase.get_instance().get_visitors_sessions_data()

    def test_num_sessions(self):
        self.assertRaises(ValueError, queries.num_sessions, self.sites_session_list, 'nonexistent_site_url')

        for site in tests_data.site_urls_expected_results:
            current_query_result = queries.num_sessions(self.sites_session_list, site['site_url'])
            self.assertEqual(current_query_result, site['number_of_sessions'])

    def test_median_session_length(self):
        self.assertRaises(ValueError, queries.median_session_length, self.sites_session_list, 'nonexistent_site_url')
        for site in tests_data.site_urls_expected_results:
            current_query_result = queries.median_session_length(self.sites_session_list, site['site_url'])
            self.assertEqual(current_query_result, site['median_session_length'])

    def test_num_unique_visited_sites(self):
        self.assertRaises(ValueError, queries.num_unique_visited_sites, self.sites_session_list, 'nonexistent_visitor_id')
        for visitor in tests_data.visitors_expected_results:
            current_query_result = queries.num_unique_visited_sites(self.visitors_sessions, visitor['visitor_id'])
            self.assertEqual(current_query_result, visitor['number_of_unique_visited_sites'])
