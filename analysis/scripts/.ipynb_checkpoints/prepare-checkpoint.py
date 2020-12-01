def load_and_process(url):
    data = pd.read_csv(url)
    df = pd.DataFrame(data)
    #df2 = df.dropna().drop(['goals_away', 'goals_home', 'game_id'], axis = 1).rename(columns={'dateTime':'date'}).sort_values('play_num').reset_index()
    return df2
