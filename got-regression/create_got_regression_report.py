#! /usr/bin/python
#
# Python script for parsing the regression results and creating the GoT regression_report.csv
#
# Author: Aly Metwaly (aly.metwaly@nokia.com)
#
# Usage: python create_regression_report_mrm.py
#

import re
import csv

# Parse test results
with open("report.txt", 'r') as f:
    dashboard_lines = f.readlines()
for line in range(0, len(dashboard_lines)):
    current_line = dashboard_lines[line]
    # Extract test results coverage
    phase_info_line = re.search("Phase Info:", current_line)
    if phase_info_line:
        test_results_line = dashboard_lines[line+5]
        test_scores_list = test_results_line.split()
f.close()
passed_tests = int(test_scores_list[2])
completed_tests = int(test_scores_list[3])
total_tests = int(test_scores_list[4])
failed_tests = completed_tests - passed_tests
incomplete_tests = total_tests - completed_tests
print("Total TC:", total_tests, "\nPassed TC: ", passed_tests, "\nCompleted TC: ",
      total_tests, "\nFailed TC:", failed_tests, "\nIncomplete TC:", incomplete_tests)

# Parse coverage results
with open("dashboard.txt", 'r') as f:
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
    # Extract code coverage scores
    code_coverage_line = re.search("Total Coverage Summary", current_line)
    if code_coverage_line:
        code_coverage_score_line = dashboard_lines[line+2]
        coverage_scores = code_coverage_score_line.split()
f.close()
code_coverage = float(coverage_scores[0])
line_coverage = float(coverage_scores[1])
cond_coverage = float(coverage_scores[2])
toggle_coverage = float(coverage_scores[3])
fsm_coverage = float(coverage_scores[4])
branch_coverage = float(coverage_scores[5])
print("Code coverage:", code_coverage, "\nFunctional coverage:", feature_coverage_score, "\nLine coverage:", line_coverage, "\nConditional coverage:", cond_coverage,
      "\nToggle coverage:", toggle_coverage, "\nFSM coverage:", fsm_coverage, "\nBranch coverage:", branch_coverage)

# Create the regression_report.csv
with open('regression_report.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Total targeted TC",
                         "Passed TC",
                         "Failed TC",
                         "Not Completed TC",
                         "Line Coverage",
                         "Functional Coverage",
                         "Code Coverage (ASIC only)",
                         "Toggle Coverage (ASIC only)",
                         "Branch Coverage (ASIC only)",
                         "Expression/Condition Coverage (ASIC only)",
                         "FSM Coverage (ASIC only)"])
    filewriter.writerow([total_tests, passed_tests, failed_tests, incomplete_tests, line_coverage, feature_coverage_score, code_coverage,
                         toggle_coverage, branch_coverage, cond_coverage, fsm_coverage])
csvfile.close()
