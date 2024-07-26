from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import timedelta, datetime
from plotnine import ggplot, aes, geom_point, geom_line, geom_vline, labs, theme_bw, theme, element_text, scale_x_continuous, scale_y_continuous, scale_color_manual, annotate, geom_ribbon, labs, element_blank, scale_size_identity

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression


import numpy as np
import re
import time

import pandas as pd
import networkx as nx
from datetime import datetime


import matplotlib.pyplot as plt



from collections import defaultdict
import math


def scrape(i, driver):

    if i==5:
        element_css_selector = "a[href='#'][data-key='X1,X2,X3,X4,X5'"
        element = driver.find_element(By.CSS_SELECTOR, element_css_selector)
    else:
        element_css_selector = "a[href='#'][data-key='Q" + str(i) + "']"
        element = driver.find_element(By.CSS_SELECTOR, element_css_selector)

    # Click on the element using JavaScript
    driver.execute_script("arguments[0].click();", element)
    # Wait for 1 seconds
    time.sleep(1)
    # Get HTML content
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.con-box + .con-box td')))
    # Get the page source
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    message_elements = soup.select('.con-box + .con-box td')

    # Extract text from message elements
    message = [element.get_text() for element in message_elements]
    # Reverse the message list and create a dataframe
    message_df = pd.DataFrame({'Message': message[::-1]})

    return(message_df)

def cumulative_timedelta_sum(timedeltas):
    cumulative_sum = timedelta(0)
    cumulative_sums = []
    for td in timedeltas:
        cumulative_sum +=td
        cumulative_sums.append(cumulative_sum)
    return cumulative_sums


def calculate_time_difference(times):
    time_differences = []
    for i in range(1, len(times)):
        difference = timedelta(hours=times[i-1].hour, minutes=times[i-1].minute, seconds=times[i-1].second) - \
                     timedelta(hours=times[i].hour, minutes=times[i].minute, seconds=times[i].second)
        if difference.total_seconds() < 0:
            difference = timedelta(seconds=0)
        time_differences.append(difference)
    return time_differences

def web_scrape_kbl(driver):
    column_names = ["team", "player_home_away", "time_remaining", "description"]

    # Create an empty DataFrame with column names
    empty_df = pd.DataFrame(columns=column_names)

    button = driver.find_element(By.CSS_SELECTOR, "li[data-key='onAirSms']")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(4)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    overtime = soup.select('.summary-table :nth-child(6)')
    overtime = [elem.get_text(strip=True) for elem in overtime]

    teams = soup.select('.info > h6')
    teams = [elem.get_text(strip=True) for elem in teams]

    date = soup.select('.bd-date')
    date = [elem.get_text(strip=True) for elem in date][0]
    date_string = date[:10]

    # Split the date string into components
    year, month, day = map(int, date_string.split('.'))
    date_object = datetime(year, month, day)
    formatted_date = date_object.strftime('%Y-%m-%d')

    total = soup.select('td:nth-child(7)')
    total = [elem.get_text(strip=True) for elem in total]

    time.sleep(1)

    if overtime[2] == "0" and overtime[3] == "0":
        for i in range(1, 5):
            message2 = scrape(i, driver)
            df = data_cleansing(message2)

            empty_df = pd.concat([empty_df, df], ignore_index=True)
    else:
        for i in range(1, 6):
            message2 = scrape(i, driver)
            df = data_cleansing(message2)

            empty_df = pd.concat([empty_df, df], ignore_index=True)

    empty_df['date'] = [formatted_date for _ in range(len(empty_df))]
    empty_df['team'] = np.where(empty_df['player_home_away'] == 'Home', teams[0], teams[1])

    if int(total[0]) - int(total[1]) > 0:
        empty_df['win_loss'] = [1 for _ in range(len(empty_df))]
    else:
        empty_df['win_loss'] = [0 for _ in range(len(empty_df))]
    return empty_df


def substr_right(x, n):
    return x[-n:]


def data_cleansing(data):
    kbl_pbp = pd.DataFrame(
        columns=['date', 'team', 'player_home_away', 'time_remaining', 'secs_remaining', 'play_length', 'description'])
    for i in range(len(data)):
        if bool(re.match("^-?\\d*\\.?\\d+$", data.iloc[i, 0][0])):
            kbl_pbp.loc[i, 'player_home_away'] = "Away"
            if bool(re.match("^10:00", data.iloc[i, 0][0:5])):
                kbl_pbp.loc[i, 'time_remaining'] = data.iloc[i, 0][0:5]
            else:
                kbl_pbp.loc[i, 'time_remaining'] = data.iloc[i, 0][0:4]

            time_pattern = r"^\d{1,2}:\d{2}"

            extracted_substring = re.sub(time_pattern + r'\s*', '', data.iloc[i, 0])

            extracted_substrings = re.sub(r'^\s+', '', extracted_substring)
            kbl_pbp.loc[i, 'description'] = extracted_substrings

        elif isinstance(data.iloc[i, 0][0:1], str):
            kbl_pbp.loc[i, 'player_home_away'] = "Home"
            trimmed_column = re.sub(r'^\s+', '', data.iloc[i, 0][-5:])
            kbl_pbp.loc[i, 'time_remaining'] = trimmed_column

            last_space_position = max(m.start() for m in re.finditer(' ', data.iloc[i, 0]))

            extracted_substring = data.iloc[i, 0][:last_space_position]

            extracted_substring = extracted_substring.lstrip()
            kbl_pbp.loc[i, 'description'] = extracted_substring

        # Cleaning the character values in the time_remaining column

    for i in range(1, len(kbl_pbp['time_remaining'])):
        if kbl_pbp.loc[i, 'time_remaining'].startswith('임시작 '):
            kbl_pbp.loc[i, 'time_remaining'] = kbl_pbp['time_remaining'][i - 1]
        elif kbl_pbp.loc[i, 'time_remaining'].startswith('임종료 '):
            kbl_pbp.loc[i, 'time_remaining'] = kbl_pbp['time_remaining'][i + 1]

    kbl_pbp['time_remaining'] = kbl_pbp['time_remaining'].str.replace('^칙', '', regex=True)

    return kbl_pbp


def data_cleansing2(pbp):
    quarter = 1
    pbp = pbp.reset_index(drop=True)
    for i in range(len(pbp) - 1):
        if pbp.loc[i, 'time_remaining'] == "0:00" and pbp.loc[i + 1, 'time_remaining'] != "0:00":
            pbp.loc[i, "quarter"] = quarter
            quarter = quarter + 1
        else:
            pbp.loc[i, "quarter"] = quarter

    # Finding the maximum quarter and assigning it to the last row
    pbp.loc[len(pbp) - 1, 'quarter'] = pbp['quarter'].max()
    pbp['quarter'] = pbp['quarter'].astype(int)
    pbp = pbp[pbp['time_remaining'].apply(starts_with_integer)]
    pbp = pbp.reset_index(drop=True)
    pbp["time_remaining"] = "00:" + pbp['time_remaining'].astype(str)
    pbp["time_remaining"] = (
        pd.to_datetime(pbp['time_remaining'], format='%H:%M:%S').dt.time)
    # Seconds Remaining
    if pbp['quarter'].max() > 4:
        total = 60 * (5 * (pbp['quarter'].max() - 4) + 40)
        time_diffs = calculate_time_difference(pbp['time_remaining'])

        for i in range(len(time_diffs)):
            if time_diffs[i] == timedelta(days=-1, seconds=85800):
                time_diffs[i] = timedelta(0)

        timedeltas = [int(td.total_seconds()) for td in cumulative_timedelta_sum(time_diffs)]
        my_list = [total - td for td in timedeltas]
        time_diff = [int(td.total_seconds()) for td in time_diffs]
        my_list.insert(0, total)
        pbp["secs_remaining"] = my_list
        time_diff.insert(len(time_diff), 0)
        pbp["play_length"] = time_diff
    else:
        time_diffs = calculate_time_difference(pbp['time_remaining'])
        for i in range(len(time_diffs)):
            if time_diffs[i] == timedelta(days=-1, seconds=85800):
                time_diffs[i] = timedelta(0)

        timedeltas = [int(td.total_seconds()) for td in cumulative_timedelta_sum(time_diffs)]
        my_list = [2400 - td for td in timedeltas]
        time_diff = [int(td.total_seconds()) for td in time_diffs]
        my_list.insert(0, 2400)
        pbp["secs_remaining"] = my_list
        time_diff.insert(len(time_diff), 0)
        pbp["play_length"] = time_diff

    return pbp


def data_cleansing3(pbp):
    home = 0
    away = 0
    pbp['home_score'] = 0
    pbp['away_score'] = 0
    for i in range(len(pbp)):
        if pbp.loc[i, 'player_home_away'] == "Home" and "2점슛성공" in pbp.loc[i, 'description']:
            home += 2
            pbp.loc[i, 'home_score'] = home
            pbp.loc[i, 'away_score'] = away
        elif pbp.loc[i, 'player_home_away'] == "Away" and "2점슛성공" in pbp.loc[i, 'description']:
            away += 2
            pbp.loc[i, 'home_score'] = home
            pbp.loc[i, 'away_score'] = away
        elif pbp.loc[i, 'player_home_away'] == "Home" and "3점슛성공" in pbp.loc[i, 'description']:
            home += 3
            pbp.loc[i, 'home_score'] = home
            pbp.loc[i, 'away_score'] = away
        elif pbp.loc[i, 'player_home_away'] == "Away" and "3점슛성공" in pbp.loc[i, 'description']:
            away += 3
            pbp.loc[i, 'home_score'] = home
            pbp.loc[i, 'away_score'] = away
        elif pbp.loc[i, 'player_home_away'] == "Home" and "자유투성공" in pbp.loc[i, 'description']:
            home += 1
            pbp.loc[i, 'home_score'] = home
            pbp.loc[i, 'away_score'] = away
        elif pbp.loc[i, 'player_home_away'] == "Away" and "자유투성공" in pbp.loc[i, 'description']:
            away += 1
            pbp.loc[i, 'home_score'] = home
            pbp.loc[i, 'away_score'] = away
        elif pbp.loc[i, 'player_home_away'] == "Home" and "덩크슛성공" in pbp.loc[i, 'description']:
            home += 2
            pbp.loc[i, 'home_score'] = home
            pbp.loc[i, 'away_score'] = away
        elif pbp.loc[i, 'player_home_away'] == "Away" and "덩크슛성공" in pbp.loc[i, 'description']:
            away += 2
            pbp.loc[i, 'home_score'] = home
            pbp.loc[i, 'away_score'] = away
        else:
            pbp.loc[i, 'home_score'] = home
            pbp.loc[i, 'away_score'] = away
    pbp['score_diff'] = pbp['home_score'] - pbp['away_score']

    pbp = pbp.reindex(
        columns=['date', 'team', 'player_home_away', 'quarter', 'time_remaining', 'description', 'secs_remaining',
                 'play_length', 'win_loss', 'home_score', 'away_score', 'score_diff'])

    return pbp


def starts_with_integer(s):
    try:
        return len(str(s)) > 0 and str(s)[0].isdigit()
    except Exception as e:
        print(f"Error processing value: {s}, Error: {e}")
        return False


def scrape_pbp_kbl(driver, starting_page, ending_date):
    driver.get(starting_page)
    driver.refresh()
    time.sleep(2)

    KBL_PBP = pd.DataFrame()
    keep_clicking = True

    while keep_clicking:
        time.sleep(4)  # Originally 4
        dropdown_menu = driver.find_element(By.CSS_SELECTOR, "#container select")
        options = dropdown_menu.find_elements(By.CSS_SELECTOR, 'option')
        option_values = [option.get_attribute("value") for option in options]

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        date = soup.select('.bd-date')
        date = [elem.get_text(strip=True) for elem in date][0]

        for i in option_values:
            time.sleep(3)
            option = driver.find_element(By.CSS_SELECTOR, "#container select option[value='{}']".format(i))
            option.click()
            current_url = driver.current_url

            match = re.search(r"/record/(.*)$", current_url)

            game_id = match.group(1)  # Extract the first capturing group (the game ID)
            print(f"Retrieving Game ID: {game_id}")
            pbp = web_scrape_kbl(driver)
            pbp = pbp[pbp['time_remaining'].apply(starts_with_integer)]
            pbp = data_cleansing2(pbp)
            pbp = data_cleansing3(pbp)
            pbp['game_id'] = game_id
            KBL_PBP = pd.concat([KBL_PBP, pbp])

        if date != ending_date:
            element = driver.find_element(By.CSS_SELECTOR, "i.ic-arrow-right-40")
            element.click()
        else:
            break

    #    driver.quit()
    return KBL_PBP


def scrape_pbp_kbl_single(driver, starting_page):
    driver.get(starting_page)
    driver.refresh()
    time.sleep(2)

    KBL_PBP = pd.DataFrame()
    keep_clicking = True

    current_url = driver.current_url

    match = re.search(r"/record/(.*)$", current_url)

    game_id = match.group(1)  # Extract the first capturing group (the game ID)
    print(f"Retrieving Game ID: {game_id}")
    pbp = web_scrape_kbl(driver)
    pbp = data_cleansing2(pbp)
    pbp = data_cleansing3(pbp)
    pbp['game_id'] = game_id
    KBL_PBP = pd.concat([KBL_PBP, pbp])

    return KBL_PBP


def kbl_wp_chart(data, training_data, algorithm, show_labels=True):
    features = training_data[["player_home_away", "secs_remaining", "score_diff"]]
    target = training_data["win_loss"].astype('category')

    new_features = data[["player_home_away", "secs_remaining", "score_diff"]]
    categorical_cols = ["player_home_away"]

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), categorical_cols)
        ],
        remainder='passthrough'  # Pass through remaining columns as they are
    )
    features_encoded = preprocessor.fit_transform(features)
    new_features_encoded = preprocessor.transform(new_features)

    if algorithm == "Logistic Regression":
        logreg_model = LogisticRegression(random_state=42)
        logreg_model.fit(features_encoded, target)

        predictions = logreg_model.predict_proba(new_features_encoded)[:, 1]
        data['win_prob'] = predictions

    if data['win_loss'][0] == 1:
        data['win_prob'] = data.apply(lambda row: 1 if row['secs_remaining'] == 0 else row['win_prob'], axis=1)
    else:
        data['win_prob'] = data.apply(lambda row: 0 if row['secs_remaining'] == 0 else row['win_prob'], axis=1)

    if data['team'][0] == "원주 DB":
        home_col = "#0d7128"
    elif data['team'][0] == "서울 삼성":
        home_col = "#0032a0"
    elif data['team'][0] == "고양 소노":
        home_col = "#78a2cb"
    elif data['team'][0] == "서울 SK":
        home_col = "#dc0029"
    elif data['team'][0] == "창원 LG":
        home_col = "#fbcf2f"
    elif data['team'][0] == "부산 KCC":
        home_col = "#153a6f"
    elif data['team'][0] == "안양 정관장":
        home_col = "#7a2827"
    elif data['team'][0] == "수원 KT":
        home_col = "#161213"
    elif data['team'][0] == "대구 한국가스공사":
        home_col = "#201451"
    elif data['team'][0] == "울산 현대모비스":
        home_col = "#Ff4114"

    if data['team'][5] == "원주 DB":
        away_col = "#0d7128"
    elif data['team'][5] == "서울 삼성":
        away_col = "#0032a0"
    elif data['team'][5] == "고양 소노":
        away_col = "#78a2cb"
    elif data['team'][5] == "서울 SK":
        away_col = "#dc0029"
    elif data['team'][5] == "창원 LG":
        away_col = "#fbcf2f"
    elif data['team'][5] == "부산 KCC":
        away_col = "#153a6f"
    elif data['team'][5] == "안양 정관장":
        away_col = "#7a2827"
    elif data['team'][5] == "수원 KT":
        away_col = "#161213"
    elif data['team'][5] == "대구 한국가스공사":
        away_col = "#201451"
    elif data['team'][5] == "울산 현대모비스":
        away_col = "#Ff4114"

    plot_lines = [1200]
    msec = data['secs_remaining'].max()
    sec = msec - 2400
    ot_counter = 0

    while sec > 0:
        sec = sec - 300
        plot_lines.append(2400 + ot_counter * 300)
        ot_counter += 1

    x = pd.concat([
        data[['secs_remaining', 'win_prob']].assign(team='home'),
        data[['secs_remaining', 'win_prob']].assign(win_prob=lambda x: 1 - x['win_prob'], team='away')],
        ignore_index=True)

    x['secs_elapsed'] = msec - x['secs_remaining']

    if x['secs_elapsed'].min() != 0:
        new_row = pd.DataFrame({
            'secs_remaining_absolute': msec,
            'secs_elapsed': [0, 0],
            'win_prob': [0.5, 0.5],
            'team': ['home', 'away']
        })
        x = pd.concat([x, new_rows], ignore_index=True)

        # Arrange x by secs_elapsed
        x = x.sort_values(by='secs_elapsed')

        # Reset index if needed
        x = x.reset_index(drop=True)

    data['wp_delta'] = data['win_prob'].diff().abs()
    data['wp_delta'] = data['wp_delta'].fillna(0)

    gei = data['wp_delta'].sum(skipna=True)
    gei_str = f"Game Excitement Index: {round(gei, 2)}"

    Home_team = data['team'].iloc[0]
    Away_team = data['team'].iloc[5]

    if data['score_diff'].iloc[-1] > 0:
        # Calculate minimum win probability for home team
        min_prob = min(data['win_prob'])
        min_prob_str = f"Minimum Win Probability for {Home_team}: "
        if 100 * min_prob < 1:
            min_prob_str += "< 1%"
        else:
            min_prob_str += f"{round(100 * min_prob)}%"

    else:
        # Calculate minimum win probability for away team
        min_prob = min(1 - data['win_prob'])
        min_prob_str = f"Minimum Win Probability for {Away_team}: "
        if 100 * min_prob < 1:
            min_prob_str += "< 1%"
        else:
            min_prob_str += f"{round(100 * min_prob)}%"

    # Get scores and create summary string
    home_score = data['home_score'].iloc[-1]
    away_score = data['away_score'].iloc[-1]
    data['date'] = pd.to_datetime(data['date']).dt.date
    date_str = data['date'][0].strftime('%Y-%m-%d')

    # Construct the string with centered date
    st = f"{Home_team}: {home_score}  {Away_team}: {away_score}\n\n"

    # Calculate center alignment
    total_width = len(st.strip())  # Calculate the width of the preceding line
    padding_width = (total_width - len(date_str)) // 2  # Calculate padding for centering

    st += '  ' * padding_width + date_str + '  ' * padding_width

    x['Minutes Elapsed'] = x['secs_elapsed'] / 60
    plot = ggplot(x, aes(x='Minutes Elapsed', y='win_prob', group='team', color='team')) + geom_line(
        size=1) + theme_bw() + geom_vline(xintercept=[line / 60 for line in plot_lines], linetype='dashed', alpha=0.5,
                                          size=0.8) + labs(x='Minutes Elapsed',
                                                           y='Win Probability',
                                                           color='',
                                                           title=f'Win Probability Chart for {Home_team} vs. {Away_team} by {algorithm}',
                                                           subtitle=st) + theme(
        plot_title=element_text(size=10, hjust=0.5, face='bold'),
        text=element_text(family='Arial Unicode MS', size=10),
        plot_subtitle=element_text(size=8, hjust=0.5),
        axis_title=element_text(size=10, face='bold'),
        plot_caption=element_text(size=8, hjust=0),
        legend_text=element_text(size=7),
        legend_position='bottom') + scale_color_manual(values=[away_col, home_col],
                                                       labels=[Away_team, Home_team]) + scale_x_continuous(
        breaks=list(range(int(x['Minutes Elapsed'].min()), int(x['Minutes Elapsed'].max()) + 1, 5))) + \
           scale_y_continuous(labels=lambda x: [f"{100 * val} %" for val in x])

    if show_labels:
        plot = (plot + annotate("text", x=0, y=0.1, label=gei_str, size=7, ha='left') +
                annotate("text", x=0, y=0.025, label=str(min_prob_str), size=7, ha='left')
                )

    return plot


def kbl_wp_chart_new(data, training_data, algorithm, show_labels=True):
    features = training_data[["player_home_away", "secs_remaining", "score_diff"]]
    target = training_data["win_loss"].astype('category')

    new_features = data[["player_home_away", "secs_remaining", "score_diff"]]
    categorical_cols = ["player_home_away"]

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), categorical_cols)
        ],
        remainder='passthrough'  # Pass through remaining columns as they are
    )
    features_encoded = preprocessor.fit_transform(features)
    new_features_encoded = preprocessor.transform(new_features)

    if algorithm == "Logistic Regression":
        logreg_model = LogisticRegression(random_state=42)
        logreg_model.fit(features_encoded, target)

        predictions = logreg_model.predict_proba(new_features_encoded)[:, 1]
        data['win_prob'] = predictions

    if data['win_loss'][0] == 1:
        data['win_prob'] = data.apply(lambda row: 1 if row['secs_remaining'] == 0 else row['win_prob'], axis=1)
    else:
        data['win_prob'] = data.apply(lambda row: 0 if row['secs_remaining'] == 0 else row['win_prob'], axis=1)

    if data['team'][0] == "원주 DB":
        home_col = "#0d7128"
    elif data['team'][0] == "서울 삼성":
        home_col = "#0032a0"
    elif data['team'][0] == "고양 소노":
        home_col = "#78a2cb"
    elif data['team'][0] == "서울 SK":
        home_col = "#dc0029"
    elif data['team'][0] == "창원 LG":
        home_col = "#fbcf2f"
    elif data['team'][0] == "부산 KCC":
        home_col = "#153a6f"
    elif data['team'][0] == "안양 정관장":
        home_col = "#7a2827"
    elif data['team'][0] == "수원 KT":
        home_col = "#161213"
    elif data['team'][0] == "대구 한국가스공사":
        home_col = "#201451"
    elif data['team'][0] == "울산 현대모비스":
        home_col = "#Ff4114"

    if data['team'][5] == "원주 DB":
        away_col = "#0d7128"
    elif data['team'][5] == "서울 삼성":
        away_col = "#0032a0"
    elif data['team'][5] == "고양 소노":
        away_col = "#78a2cb"
    elif data['team'][5] == "서울 SK":
        away_col = "#dc0029"
    elif data['team'][5] == "창원 LG":
        away_col = "#fbcf2f"
    elif data['team'][5] == "부산 KCC":
        away_col = "#153a6f"
    elif data['team'][5] == "안양 정관장":
        away_col = "#7a2827"
    elif data['team'][5] == "수원 KT":
        away_col = "#161213"
    elif data['team'][5] == "대구 한국가스공사":
        away_col = "#201451"
    elif data['team'][5] == "울산 현대모비스":
        away_col = "#Ff4114"

    plot_lines = [1200]
    msec = data['secs_remaining'].max()
    sec = msec - 2400
    ot_counter = 0

    while sec > 0:
        sec = sec - 300
        plot_lines.append(2400 + ot_counter * 300)
        ot_counter += 1

    x = pd.concat([
        data[['secs_remaining', 'win_prob']].assign(team='home'),
        data[['secs_remaining', 'win_prob']].assign(win_prob=lambda x: 1 - x['win_prob'], team='away')],
        ignore_index=True)

    x['secs_elapsed'] = msec - x['secs_remaining']

    if x['secs_elapsed'].min() != 0:
        new_row = pd.DataFrame({
            'secs_remaining_absolute': msec,
            'secs_elapsed': [0, 0],
            'win_prob': [0.5, 0.5],
            'team': ['home', 'away']
        })
        x = pd.concat([x, new_rows], ignore_index=True)

        # Arrange x by secs_elapsed
        x = x.sort_values(by='secs_elapsed')
        # Reset index if needed
        x = x.reset_index(drop=True)

    data['wp_delta'] = data['win_prob'].diff().abs()
    data['wp_delta'] = data['wp_delta'].fillna(0)
    Home_team = data['team'].iloc[0]
    Away_team = data['team'].iloc[5]

    gei = data['wp_delta'].sum(skipna=True)
    gei_str = f"Game Excitement Index: {round(gei, 2)}"

    if data['score_diff'].iloc[-1] > 0:
        # Calculate minimum win probability for home team
        min_prob = data['win_prob'].min()
        min_prob_str = f"Minimum Win Probability for {Home_team}: "
        if 100 * min_prob < 1:
            min_prob_str += "< 1%"
        else:
            min_prob_str += f"{round(100 * min_prob)}%"

    else:
        # Calculate minimum win probability for away team
        min_prob = min(1 - data['win_prob'])
        min_prob_str = f"Minimum Win Probability for {Away_team}: "
        if 100 * min_prob < 1:
            min_prob_str += "< 1%"
        else:
            min_prob_str += f"{round(100 * min_prob)}%"

    # Get scores and create summary string
    home_score = data['home_score'].iloc[-1]
    away_score = data['away_score'].iloc[-1]
    data['date'] = pd.to_datetime(data['date']).dt.date
    date_str = data['date'][0].strftime('%Y-%m-%d')

    # Construct the string with centered date
    st = f"{Home_team}: {home_score}  {Away_team}: {away_score}\n\n"

    # Calculate center alignment
    total_width = len(st.strip())  # Calculate the width of the preceding line
    padding_width = (total_width - len(date_str)) // 2  # Calculate padding for centering

    st += '  ' * padding_width + date_str + '  ' * padding_width
    font = {'family': 'Malgun Gothic'}
    x['Minutes Elapsed'] = x['secs_elapsed'] / 60
    if home_score > away_score:
        winning_col = home_col
        # winning_url = home_url
        losing_col = away_col
        # losing_url = away_url
        x = x[x['team'] == 'home']
    else:
        winning_col = away_col
        # winning_url = away_url
        losing_col = home_col
        # losing_url = home_url
        x = x[x['team'] == 'away']

    x['favored'] = x['win_prob'] >= 0.5
    x['favored_prev'] = x['favored'].shift(1)

    # Find the indices where there is a switch in 'favored' status
    ix_switch = x.index[x['favored'] != x['favored_prev']].tolist()

    # Drop the 'favored_prev' column if not needed
    x.drop(columns=['favored_prev'], inplace=True)
    add = pd.DataFrame()

    # Perform operations if there are switches in 'favored' status
    lagged_favored = np.roll(x['favored'], 1)
    ix_switch = np.where(x['favored'] != lagged_favored)[0]

    if len(ix_switch) > 0:
        # Create 'add' DataFrame similar to the R code
        add_top = x.iloc[ix_switch].assign(id=np.arange(1, len(ix_switch) + 1))
        add_bottom = x.iloc[ix_switch - 1].assign(id=np.arange(1, len(ix_switch) + 1))

        add = pd.concat([add_top, add_bottom]).groupby('id').agg({
            'secs_elapsed': lambda s: s.iloc[0] + (s.iloc[1] - s.iloc[0]) * abs(
                x.loc[s.index[0], 'win_prob'] - 0.5) / abs(
                x.loc[s.index[0], 'win_prob'] - x.loc[s.index[1], 'win_prob']),
            'win_prob': lambda s: 0.5,
            'favored': lambda s: s.iloc[0]
        }).reset_index()

        # Append 'add' DataFrame to 'x'
    x = pd.concat([x, add], ignore_index=True)
    # Calculate 'winning_upper' and 'losing_lower' columns
    x['winning_upper'] = x['win_prob'].apply(lambda wp: max(wp, 0.5))
    x['losing_lower'] = x['win_prob'].apply(lambda wp: min(wp, 0.5))

    # Define 'cols' based on 'favored' condition
    cols = [losing_col, winning_col]

    # Assuming x is a DataFrame and favored is a boolean column
    if all(x['favored']):
        cols = cols[1]

    x['Minutes Elapsed'] = x['secs_elapsed'] / 60

    plot = ggplot(x, aes(x='Minutes Elapsed', y='win_prob')) + \
           geom_line(aes(color="favored", group=1), size=1, lineend='round') + \
           geom_vline(xintercept=[line / 60 for line in plot_lines], linetype='dashed', alpha=0.5, size=0.8) + \
           labs(x="Minutes Elapsed",
                y="Win Probability",
                title=f"Win Probability Chart for {Home_team} vs. {Away_team} by {algorithm}",
                subtitle=st,
                color="") + \
           theme_bw() + \
           theme(plot_title=element_text(size=10, hjust=0.5, weight="bold"),
                 plot_subtitle=element_text(size=8, hjust=0.5),
                 axis_title=element_text(size=10, weight="bold"),
                 plot_caption=element_text(size=8, hjust=0),
                 legend_position="bottom",
                 text=element_text(size=10, family="Arial Unicode MS")) + \
           scale_x_continuous(
               breaks=list(range(int(x['Minutes Elapsed'].min()), int(x['Minutes Elapsed'].max()) + 1, 5))) + \
           scale_y_continuous(limits=(0, 1), labels=lambda x: [f"{100 * max(val, 1 - val)} %" for val in x]) + \
           geom_ribbon(aes(ymin='winning_upper', ymax=0.5), fill=winning_col, alpha=0.2) + \
           geom_ribbon(aes(ymin=0.5, ymax='losing_lower'), fill=losing_col, alpha=0.2) + \
           scale_size_identity()

    # Conditional logic for color scales
    if data['win_loss'].iloc[0] == 1:
        plot = plot + scale_color_manual(values=[away_col, home_col], labels=[Away_team, Home_team])
    else:
        plot = plot + scale_color_manual(values=[home_col, away_col], labels=[Home_team, Away_team])

    if show_labels:
        plot = (plot + annotate("text", x=0, y=0.1, label=gei_str, size=7, ha='left') +
                annotate("text", x=0, y=0.025, label=str(min_prob_str), size=7, ha='left')
                )

    return plot


def add_assist(data):
    # Initialize new columns with NaN
    data.loc[:, 'shooter'] = np.nan
    data.loc[:, 'assisted'] = np.nan
    data['assisted'] = data['assisted'].astype(object)
    data['shooter'] = data['shooter'].astype(object)
    for index, row in data.iterrows():
        text = row['description']
        text = str(text)
        cleaned_text = text.rstrip()
        result = cleaned_text[-2:]

        if result == "성공":
            shot_taker = text[:-7].rstrip()
            data.at[index, 'shooter'] = shot_taker

            if index in data.index:
                offset = 1
                next_row = data.loc[index + offset]
                while row['time_remaining'] == next_row['time_remaining']:
                    next_row = data.loc[index + offset]
                    if "어시스트" in next_row['description']:
                        text = next_row['description']

                        # Split the string by spaces except the last one
                        split_text = re.split(' (?=[^ ]+$)', text)
                        data.at[index, 'assisted'] = split_text[0]
                    offset += 1
                    if row['time_remaining'] != next_row['time_remaining']:
                        break

    data.loc[:, 'assisted'] = data.loc[:, 'assisted'].str.replace("어시스트", "")
    data.loc[:, 'assisted'] = data.loc[:, 'assisted'].str.strip()
    data = data[~data['description'].fillna('').str.contains("자유투")]
    x = data.dropna().copy()

    # Use .loc to avoid SettingWithCopyWarning
    x.loc[:, 'weights'] = 2

    # Wherever 'description' contains "3점슛", set 'weights' to 3
    x.loc[x['description'].str.contains("3점슛"), 'weights'] = 3

    return x


def kbl_assist_net(data, team_select, top=10, color="orange", k=1):
    basketball_data = data.loc[data['team'] == team_select].reset_index(drop=True)
    # Find the minimum and maximum values in 'date' column
    min_date = basketball_data['date'].min()
    max_date = basketball_data['date'].max()

    # Now you should define add_assist function in Python or replace it with equivalent Python code
    basketball_data = add_assist(basketball_data)

    # Group by 'assisted' and 'shooter' columns, and calculate sum and mean of 'weights'
    basketball_data = (basketball_data
                       .groupby(['assisted', 'shooter'])
                       .agg(points=('weights', 'sum'),
                            average=('weights', 'mean'))
                       .reset_index())

    # Trim trailing whitespace from 'shooter' column

    # Select a subset of columns
    basketball_data = basketball_data[['assisted', 'shooter', 'points']]

    # Sort by 'points' column and take the first 'top' rows
    basketball_data = (basketball_data
                       .sort_values(by='points', ascending=False)
                       .head(top))

    # Select a subset of columns
    basketball_data = basketball_data[['assisted', 'shooter', 'points']]

    # Sort by 'points' column and take the first 'top' rows
    basketball_data = (basketball_data
                       .sort_values(by='points', ascending=False)
                       .head(top))
    formatted_data = {}

    # Iterate through each row in the DataFrame
    for index, row in basketball_data.iterrows():
        assisted = row['assisted']
        shooter = row['shooter']
        points = row['points']

        # Create a tuple (shooter, assisted) as the key and points as the value
        key = (shooter, assisted)
        formatted_data[key] = points

    G = nx.from_pandas_edgelist(basketball_data, 'assisted', 'shooter', ['points'], create_using=nx.MultiDiGraph())

    # Define the layout with higher k value and more iterations
    pos = nx.spring_layout(G, k=5 / math.sqrt(G.order()), iterations=100)  # Adjust k for more separation between nodes

    # Draw the graph with custom nodes and multiple edges
    plt.figure(figsize=(12, 8))

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=color, node_size=600)

    # Draw edges with point labels
    edge_labels = defaultdict(list)
    for u, v, d in G.edges(data=True):
        rad = 0.1  # Radial separation between multiple edges
        num_edges = G.number_of_edges(u, v)

        if num_edges > 1:
            rad += 0.1 * (num_edges - 1)

        # Adjust the arrow to touch the node
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], connectionstyle=f'arc3, rad = {rad}', edge_color="gray",
                               arrows=True, arrowsize=15, min_source_margin=15, min_target_margin=15)

        # Store edge labels to position them later
        edge_labels[(u, v)].append(d['points'])

    # Draw labels with transparent background
    nx.draw_networkx_labels(G, pos, font_family='Arial Unicode MS', font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_data,
                                 label_pos=0.25, font_size=10, bbox=dict(facecolor='white', alpha=0, edgecolor='none'))
    np.random.seed(k)
    # Remove grid
    plt.grid(False)
    plt.title('Plot')
    # Remove axis
    plt.axis('off')

    plt.show()



