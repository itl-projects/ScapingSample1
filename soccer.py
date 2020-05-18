import requests
from bs4 import BeautifulSoup
import os
import csv


def check_csv(name, id):
    full_name = name+"_"+str(id)+".csv"
    if not os.path.exists('data'):
        os.mkdir('data')
    path = "data/"+full_name
    if os.path.exists(path):
        return [True, path, 0]
    else:
        try:
            with open(path, 'w') as f:
                return [True, path, 1]
        except Exception as e:
            return [False, e, -1]


def setHeaders(writer, data):
    list = []
    for col in data:
        if col == "Winner":
            continue
        list.append(col)
    writer.writerow(list)


def makeMirror(data_list):
    for data in data_list:
        temp_name = data['Team Name']
        temp_id = data['Team ID']
        data['Team Name'] = data['Opponent Team']
        data['Team ID'] = data['Opponent Team ID']
        data['Opponent Team'] = temp_name
        data['Opponent Team ID'] = temp_id
        temp_1s_goal = data['Self Goals in First Half']
        temp_1o_goal = data['Total Self Goals']
        data['Self Goals in First Half'] = data['Opponent Goals in First Half']
        data['Total Self Goals'] = data['Total Opponent Goals']
        data['Opponent Goals in First Half'] = temp_1s_goal
        data['Total Opponent Goals'] = temp_1o_goal
        if not data['Winner'].lower() == "draw":
            if data['Winner'] == ['Opponent Team']:
                data.update({'Result': 'Loss'})
            else:
                data.update({'Result': 'Win'})
    return data_list

def season():
    urls = []
    x = 1811468
    for i in range(0, 21):
        x -= 2
        string = "https://vgls.betradar.com/vfl/feeds/?/srvgdemonstrator/en/Europe:Berlin/gismo/stats_season_fixtures2/" + str(x)
        urls.append(string)
    return urls


def append_to_csv(data_list):
    # Making of Simple Sheet
    for data in data_list:
        print("Season: ", data['Season Name'].strip(), ", ", data['Team Name'], " vs. ", data['Opponent Team'])
        if data['Winner'] == data['Opponent Team']:
            data.update({'Result': 'Loss'})
        elif data['Winner'].lower() == 'draw':
            data.update({'Result': 'Draw'})
        else:
            data.update({'Result': 'Win'})
        check = check_csv(data['Team Name'], data['Team ID'])  # Returns a list [True or False, File Name or Exception, Num]
        if check[0] is False:
            raise check[1]
        with open(check[1], 'a+', newline='') as file:
            writer = csv.writer(file)
            if check[2] == 1:
                setHeaders(writer, data)
            list = []
            for i in data:
                if i == "Winner":
                    continue
                list.append(data[i])
            writer.writerow(list)


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 '
                  'Safari/537.36',}
# url = "https://vgls.betradar.com/vfl/feeds/?/srvgdemonstrator/en/Europe:Berlin/gismo/stats_season_fixtures2/1811466"
for url in season():
    r = requests.get(url, headers=headers)
    data = r.json()
    season = data['doc'][0]
    season_name = season['data']['name']
    season_id = season['data']['_id']

    matches = season['data']['matches']
    csv_list = []
    count = 0
    for match in matches:
        csv_data = {}
        match_dis = match['disqualified']
        match_id = match['_id']
        # print("Match ID: ", match_id)
        match_date = match['time']['date']
        match_time = match['time']['time']
        result = match['result']['winner']
        if result.lower() == "draw":
            winner_name = "draw"
        else:
            winner_name = match['teams'][result]['name']
        home_id = match['teams']['home']['uid']
        home_name = match['teams']['home']['name']
        away_id = match['teams']['away']['uid']
        away_name = match['teams']['away']['name']
        self_first_half_goals = match['periods']['p1']['home']
        self_second_half_goals = match['periods']['ft']['home']
        opp_first_half_goals = match['periods']['p1']['away']
        opp_second_half_goals = match['periods']['ft']['away']
        csv_data.update({'Date': match_date, 'Time': match_time, 'Match ID': match_id, 'Season ID': season_id,
                         'Season Name': season_name, 'Team Name': home_name, 'Team ID': home_id,
                         'Opponent Team': away_name,
                         'Opponent Team ID': away_id, 'Winner': winner_name,
                         'Self Goals in First Half': self_first_half_goals,
                         'Opponent Goals in First Half': opp_first_half_goals,
                         'Total Self Goals': self_second_half_goals,
                         'Total Opponent Goals': opp_second_half_goals})
        csv_list.append(csv_data)
        count += 1
# soup = BeautifulSoup(r.text, features="html.parser")


    # if count > 9:
    #     break


append_to_csv(csv_list)
# Making Mirrored Data
mirror_list = makeMirror(csv_list)
append_to_csv(mirror_list)










