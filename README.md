# h1b_statistics
Insight_Data Challenge_Data Engineerer: A python program to count top 10 occupations and top 10 states for certified h1b applications 
with built-in data structures and packages only

- Author: Xinyu Xu
- Version: 1.0.0
- Language: Python 3

# Table of Contents
1. [Problem Description](README.md#problem-description)
2. [Input Dataset](README.md#input-dataset)
3. [Output](README.md#output)
4. [Approach](README.md#approach)
5. [Instructions to run](README.md#instructions-to-run)

# Problem
The orginal problem description is provided as follows：

    A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, 
    trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor
    and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). 
    But while there are ready-made reports for[2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and 
    [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

    As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: 
    **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

# Input Dataset
Raw data could be found [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension). 
For convenience, a semicolon separated (";") format file is placed in Google drive [folder](https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf?usp=sharing).   

# Output
2 output files are generated under output folder:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications

# Approach 
- Step 1 : To get top 10 occupations and top 10 states, I read the occupation ('SOC_NAME' or 'LCA_CASE_SOC_NAME') column and the state ('LCA_CASE_WORKLOC1_STATE' or 'WORKSITE_STATE') column of certified cases only, and stored them as dictionaries.
- Step 2 : Then maintained a dictionary with all occupation classes as key and their count as values. And a similar dictionary for states is maintained as well.
- Step 3 : After looping over the certified h1b cases data getting from Step 1, sort the two dictionaries with values in descending order. Only top 10 records are required.
- Step 4 : Formatted the sort result and wrote them as required txt files.

# Instructions to run

Clone this repository and place the input file that need processing under the input folder (the one under root folder).

Execute the run.sh file under root folder to run this program.
