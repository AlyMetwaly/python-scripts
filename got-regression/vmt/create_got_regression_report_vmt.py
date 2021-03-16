#! /usr/bin/python
#
# Python script for parsing the regression results and creating the GoT regression_report.csv
#
# Author: Aly Metwaly (aly.metwaly@nokia.com)
#
# Usage: python create_regression_report_vmt.py
#

import re
import csv

# Parse test results
with open("regression_report.txt", 'r') as f:
    dashboard_lines = f.readlines()
for line in range(0, len(dashboard_lines)):
    current_line = dashboard_lines[line]
    # Extract total testcases
    find_total_line = re.search("Total:\s*(\d+)", current_line)
    if find_total_line:
        total_line = dashboard_lines[line]
        total_tc_list = re.findall("\d+", total_line)
        total_tc = int(total_tc_list[0])
    # Extract passed testcases
    find_passed_line = re.search("Passed:\s*(\d+)", current_line)
    if find_passed_line:
        passed_line = dashboard_lines[line]
        passed_tc_list = re.findall("\d+", passed_line)
        passed_tc = int(passed_tc_list[0])
    # Extract failed testcases
    find_failed_line = re.search("Failed:\s*(\d+)", current_line)
    if find_failed_line:
        failed_line = dashboard_lines[line]
        failed_tc_list = re.findall("\d+", failed_line)
        failed_tc = int(failed_tc_list[0])
    # Extract fatal testcases
    find_fatal_line = re.search("Fatal:\s*(\d+)", current_line)
    if find_fatal_line:
        fatal_line = dashboard_lines[line]
        fatal_tc_list = re.findall("\d+", fatal_line)
        fatal_tc = int(fatal_tc_list[0])
    # Extract incomplete testcases
    find_incomplete_line = re.search("Incomplete:\s*(\d+)", current_line)
    if find_incomplete_line:
        incomplete_line = dashboard_lines[line]
        incomplete_tc_list = re.findall("\d+", incomplete_line)
        incomplete_tc = int(incomplete_tc_list[0])
f.close()
# Sum the fatal and failed to find the total failed testcases
total_failed_tc = failed_tc + fatal_tc
print("Total TC:", total_tc, "\nPassed TC: ", passed_tc, "\nFailed TC:",
      total_failed_tc, "\nIncomplete TC:", incomplete_tc)

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
    filewriter.writerow([total_tc, passed_tc, total_failed_tc, incomplete_tc, line_coverage, feature_coverage_score, code_coverage,
                         toggle_coverage, branch_coverage, cond_coverage, fsm_coverage])
csvfile.close()
