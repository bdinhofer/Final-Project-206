import sqlite3
import json
import os



def set_up_db(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def read_Data_From_File(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    file_data = file_data.replace("\'", "\"")
    json_data = json.loads(file_data)
    return json_data



def create_team_table(data, cur, conn, i):
    cur.execute("CREATE TABLE IF NOT EXISTS nba_teams (id INTEGER PRIMARY KEY, team TEXT, city TEXT, winpct INTEGER)")
    while True:
        try:
            cur.execute("INSERT INTO nba_teams (id,team,city,winpct) VALUES (?,?,?,?)", (data[i]['TEAM_ID'], data[i]['TEAM_NAME'], data[i]['TEAM_CITY'], data[i]['WIN_PCT'],))
        except:
            break
        i += 1
        if i % 25 == 0 or i > len(data):
            break
    conn.commit()
    return None 

def create_player_table(data, cur, conn, i):
    cur.execute("CREATE TABLE IF NOT EXISTS nba_players (team_id INTEGER, name TEXT, gp INTEGER, reb INTEGER, ast INTEGER, pts INTEGER)")
    cur.execute("SELECT id FROM nba_teams")
    lst = []
    for j in cur:
        lst.append(j)
    while True:
        try:
            for id_ in lst:
                if id_ == data[i][1]['TEAM_ID']:
                    team_id = id_ 
            cur.execute("INSERT INTO nba_players (team_id,name,gp,reb,ast,pts) VALUES (?,?,?,?,?,?)", (team_id, data[i][0], data[i][1]['GP'], data[i][1]['REB'], data[i][1]['AST'], data[i][1]['PTS']))
        except:
            break
        i += 1
        if i % 25 == 0 or i > len(data):
            break
    conn.commit()
    return None
            
def main1():
    cur, conn = set_up_db('Final-Data.db')
    d = read_Data_From_File('PLAYER_STATS.txt')
    create_player_table(d, cur, conn, 25) #Each time this code runs increase i by 25

main1()



    