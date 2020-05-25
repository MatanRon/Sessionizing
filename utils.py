import argparse

def parse_args():
    """
    An auxiliary function for arguments parsing
    time complexity: O(1)
    space complexity: O(1)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("csvs_folder", nargs='?', help="Folder containing CSV files with sites data", default="./data")
    args = parser.parse_args()
    return args