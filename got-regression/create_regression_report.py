import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()


def parse_coverage_results(self, coverage_info_file, functional_info_file):
    """
    Parse coverage results from coverage files. 

    Args:
        coverage_info_file: Coverage text file including code coverage
        functional_info_file: functional html file including functional coverage

    Returns:

    """
    # Parse functional coverage
    with open(args.file, 'r') as f:
        dashboard_lines = f.readlines()
    for line in range(0, len(dashboard_lines)):
        current_line = dashboard_lines[line]
        # Extract functional coverage
        feature_coverage_line = re.search("Feature_coverage", current_line)
        if feature_coverage_line:
            feature_coverage_score_line = dashboard_lines[line+1]
            feature_coverage_score_list = re.findall(
                "\d+.\d+", feature_coverage_score_line)
            feature_coverage_score = float(feature_coverage_score_list[0])
