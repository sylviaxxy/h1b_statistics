#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculate top 10 occupations and states of H1B visa.

@author: Sylvia Xinyu Xu
@Date: Oct 28th 2018
@Version: 1.0.0

"""
import os
import sys
import csv


def load_data(input_path):
    """load data as a dict
    input: path of input h1b data files from USCIS
    output: dict of certified h1b cases
    """

    lines = []
    certified_h1b_data = {'SOC_NAME': [],
                          'STATE': []
                          }
    useful_cols_name = ['SOC_NAME', 'STATE', 'CASE_STATUS']
    useful_cols_index = [0, 0, 0]

    with open(input_path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            lines.append(row)

        col_names = lines[0]
        if 'LCA_CASE_SOC_NAME' in col_names:
            useful_cols_index[0] = col_names.index('LCA_CASE_SOC_NAME')
            useful_cols_index[1] = col_names.index('LCA_CASE_WORKLOC1_STATE')
            useful_cols_index[2] = col_names.index('STATUS')
        else:
            useful_cols_index[0] = col_names.index('SOC_NAME')
            useful_cols_index[1] = col_names.index('WORKSITE_STATE')
            useful_cols_index[2] = col_names.index('CASE_STATUS')

        for line in lines[1:]:
            if line[useful_cols_index[2]] == 'CERTIFIED':
                for i in range(0, 2):
                    certified_h1b_data[useful_cols_name[i]].append(line[useful_cols_index[i]])

    return certified_h1b_data


def count_and_dict(h1b_data):
    """count the certified cases for each occupation and state
    input: certified h1b data dict
    output:  count result dic containing occupation count dict and state count dict
    """
    unique_occu = set(h1b_data['SOC_NAME'])
    unique_state = set(h1b_data['STATE'])
    occu_count_dict = {}
    state_count_dict = {}

    for i in unique_occu:
        occu_count_dict[i] = 0
    for i in unique_state:
        state_count_dict[i] = 0

    for i in h1b_data['SOC_NAME']:
        occu_count_dict[i] += 1

    for i in h1b_data['STATE']:
        state_count_dict[i] += 1

    count_result = {'OCCU_COUNT': occu_count_dict, 'STATE_COUNT': state_count_dict}
    return count_result

def sort_dict(dict_to_sort):
    """
    sort the dict according to values in descending order, and pict the top 10
    input: a dictionary containing unique classes and its count
    output: top 10 class
    """
    sort_result = sorted(dict_to_sort.items(),
                          key=lambda e:e[1],
                          reverse=True)[:10]
    return sort_result

def total_count(certified_h1b_data):
    """
      count all certified cases regardless of class
      input:  certified h1b data dic
      output: certified case count
    """
    certified_case_count = len(certified_h1b_data[list(certified_h1b_data.keys())[0]])
    return certified_case_count

def generate_output(field_sort_result, header, certified_case_count, file_path):
    """
      write the top 10 rank result as txt file in required format
      input: field_sort_result : list returned by sort_dict() funtion
            header: Head line in txt file
            certified_case_count: certified case count
            file_path: output file path

      output: a txt file
    """
    output_txt = open(file_path,"w")
    output_txt.write(header)
    for row in field_sort_result:
        output_txt.write(str(row[0])+";"+str(row[1])+";"+str(round((row[1]*100/certified_case_count)+0.0,1))+"%\n")
    output_txt.close()


if __name__ == '__main__':

    # set input and output path
    input_path = sys.argv[1]
    occupation_output_path = sys.argv[2]
    state_output_path = sys.argv[3]

    # load input data
    certified_h1b_data = load_data(input_path)
    # get the total case number
    count_result = count_and_dict(certified_h1b_data)
    # get top 10 occupations and top 10 states
    certified_case_count = total_count(certified_h1b_data)
    occu_sort_result = sort_dict(count_result['OCCU_COUNT'])
    state_sort_result = sort_dict(count_result['STATE_COUNT'])

    # write the txt file in required format
    generate_output(occu_sort_result,
                    "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n",
                    certified_case_count,
                    occupation_output_path)

    generate_output(state_sort_result,
                    "TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n",
                    certified_case_count,
                    state_output_path)