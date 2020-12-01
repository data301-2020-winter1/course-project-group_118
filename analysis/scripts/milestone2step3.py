# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:40:03 2020

@author: Tyler-Rogers
"""

import pandas as pd

def load_and_process(url):
    data = pd.read_csv(url)
    df = pd.DataFrame(data)
    df2 = df.dropna().drop(['goals_away', 'goals_home', 'game_id'], axis = 1).rename(columns={'dateTime':'date'}).sort_values('play_num').reset_index()
    return df2
url = 'https://raw.githubusercontent.com/data301-2020-winter1/course-project-group_118/main/data/raw/plays.csv?token=AMF4C2DNCUWGSSNSYO2WBLS7Y2N6K'
df = load_and_process(url)
