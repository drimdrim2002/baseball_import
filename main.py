import pandas as pd
import json

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    baseball_matches_original = pd.read_excel('./baseball_schedule.xlsx', engine='openpyxl', sheet_name='matches')
    baseball_match_list = []
    index = 0
    for k, v in baseball_matches_original.iterrows():
        if pd.isna(v['HOME']):
            continue
        for row_index in range(4):
            baseball_match = dict()
            baseball_match['index'] = index
            baseball_match['home'] = v['HOME']
            baseball_match['away'] = v['AWAY']

            if row_index  < 2 :
                baseball_match['matches'] = 3
            else :
                baseball_match['matches'] = 2
            baseball_match_list.append(baseball_match)
            index += 1

    initial_plan_original = pd.read_excel('./baseball_schedule.xlsx', engine='openpyxl', sheet_name='initial')
    initial_plan_list = []
    index = 0

    for k, v in initial_plan_original.iterrows():
        if pd.isna(v['HOME']):
            continue
        initial_plan = dict()
        initial_plan['index'] = index
        initial_plan['datetime'] = v['datetime']
        initial_plan['home'] = v['HOME']
        initial_plan['away'] = v['AWAY']
        initial_plan_list.append(initial_plan)
        index += 1


    distance_matrix_original = pd.read_excel('./baseball_schedule.xlsx', engine='openpyxl', sheet_name='distanceMatrix')
    distance_matrix_list = []
    index = 0

    for k, v in distance_matrix_original.iterrows():
        if pd.isna(v['from']):
            continue
        distance_matrix = dict()
        distance_matrix['index'] = index
        distance_matrix['from'] = v['from']
        distance_matrix['to'] = v['to']
        distance_matrix['distance'] = v['distance']
        distance_matrix_list.append(distance_matrix)
        index += 1

    calendar_original = pd.read_excel('./baseball_schedule.xlsx', engine='openpyxl', sheet_name='calendar')
    calendar_list = []
    index = 0

    for k, v in calendar_original.iterrows():
        if pd.isna(v['datetime']):
            continue
        calendar = dict()
        calendar['index'] = index
        calendar['datetime'] = str(v['datetime'])
        calendar['matches'] = v['matches']
        calendar['weekend'] = v['weekend']
        calendar['holiday'] = v['holiday']
        calendar_list.append(calendar)
        index += 1

    team_original_list = pd.read_excel('./baseball_schedule.xlsx', engine='openpyxl', sheet_name='teams')
    team_list = []
    index = 0

    for k, v in team_original_list.iterrows():
        if pd.isna(v['NAME']):
            continue
        team = dict()
        team['index'] = index
        team['name'] = v['NAME']
        team['stadium'] = v['STADIUM']
        team['latitude'] = v['LATITUDE']
        team['longitude'] = v['LONGITUDE']
        team_list.append(team)
        index += 1

    input = dict()
    input['teams'] = team_list
    input['matchs'] = baseball_match_list
    input['initialPlan'] = baseball_match_list
    input['distanceMatrix'] = distance_matrix_list
    input['calendar'] = calendar_list
    with open("input.json", "w", encoding='UTF8') as json_file:
        baseball_match_json = json.dump(input, json_file, ensure_ascii=False)
