import os
import data_base
import utils
import server
from data_base import SingletonDataBase

def run_server(csvs_folder):
    """
    This function fetches all information from the given path (stored in unprocessed_data). This data is passed
    to the main database (main_database) where the information is processed and held so that
    each time a query is called, the data of this database is being "accessed" (not directly of course)
    Finally the server starts running and listens to requests from the user.

    params: csvs_folder: A path to a folder where all csv files are located


    space complexity: O(n)
    n is the total number of page views
    """
    print("Processing Data...")
    try:
        unprocessed_data = data_base.UnprocessedDataBase(csvs_folder)
    except FileNotFoundError as e:
        print(str(e))
        return
    main_database = SingletonDataBase.get_instance()
    main_database.set_database(unprocessed_data.get_data())
    server.app.run(host='127.0.0.1', port=8000, debug=False, threaded=True)

def main():
    args = utils.parse_args()
    csvs_folder = args.csvs_folder
    if not os.path.exists(csvs_folder):
        print("The path:\" " + str(csvs_folder) + "\" is not valid. Pass argument to set data location")
        return

    run_server(csvs_folder)


if __name__ == "__main__":
    main()
