import csv
import config
import os
import pre_process


class UnprocessedDataBase(object):
    """
    This class is responsible for fetching merging and holding all the site visits information before it is
    processed into sessions
    """
    def __init__(self, csvs_folder_path):

        """
        time complexity: O(n)
        space complexity: O(n)
        n is the total number of page views
        (Under the assumption that there are of course, more views than csv files)
        """
        csv_paths = [os.path.join(csvs_folder_path, file_name) for file_name in os.listdir(csvs_folder_path)
                         if file_name.endswith('.csv')]
        if len(csv_paths) < 1:
            raise FileNotFoundError("No csv files in folder '" + csvs_folder_path + "'")
        self._data = self._read_csvs(csv_paths)

    @staticmethod
    def _read_csvs(csv_paths):
        """
        This function receives an array of csv file paths and creates a list of dictionaries
        where each dict represents one csv row, (i.e. a page view).

        time complexity: O(n)
        space complexity: O(n)
        n is the total number of page views
        """
        site_visits = []
        for path in csv_paths:
            # TODO: Handle error here, in case the file is corrupted or unreadable
            with open(path, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    # the original dict keys have no meaning, because there are no headlines in the CSV files
                    row = dict(zip(config.DATA_BASE_FIELDS_ORDER, row.values()))
                    site_visits.append(row)
        return site_visits

    def get_data(self):
        return self._data


class SingletonDataBase(object):
    """
    This class represents the main database of the program, it receives unprocessed data (site visits information),
    processes it into sessions by calling pre_process module's relevant functions and holds it for
    different uses of the program
    """
    __instance = None

    @staticmethod
    def get_instance():
        if SingletonDataBase.__instance is None:
            SingletonDataBase.__instance = SingletonDataBase()
        return SingletonDataBase.__instance

    def __init__(self):
        if SingletonDataBase.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SingletonDataBase.__instance = self
        self._visitors_sessions_db = None
        self._sites_sessions_db = None

    def set_database(self, unprocessed_data):
        """
        time complexity: O(n)
        space complexity: O(n)
        n is the total number of page views
        """
        self._visitors_sessions_db = pre_process.create_visitor_id_sessions(unprocessed_data)
        self._sites_sessions_db = pre_process.create_site_url_sessions(unprocessed_data)

    def get_visitors_sessions_data(self):
        return self._visitors_sessions_db

    def get_sites_sessions_data(self):
        return self._sites_sessions_db
