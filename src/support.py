import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

episodes_character = pd.read_csv("data/charactersepisode.csv")
lines = pd.read_csv("data/lines.csv") 

def get_character_info(personaje):
    df_group = episodes_character.groupby(['first_name']).size().reset_index(name='counter')
    df_group["percentage"] = (df_group["counter"] / len(episodes_character["episode_id"].unique())) * 100
    df_group = df_group.set_index('first_name')
    episode_percentage = int(df_group.loc[[f"{personaje}"], ["percentage"]].values[0][0])
    
    df_distinct = lines.drop_duplicates(subset=['season', 'episode', 'scene','first_name'])
    num_distinct = len(lines.drop_duplicates(subset=['season', 'episode', 'scene']))
    df_group2 = df_distinct.groupby(['first_name']).size().reset_index(name='counter')
    df_group2["ai"] = (df_group2["counter"] / num_distinct) * 100
    df_group2 = df_group2.set_index('first_name')
    scene_percentage = int(df_group2.loc[[f"{personaje}"], ["ai"]].values[0][0])
    
    df_lines = lines.groupby('first_name').size().reset_index(name='count')
    df_lines["percentage"] = (df_lines["count"] / len(episodes_character["episode_id"].unique()))
    df_lines = df_lines.set_index('first_name')
    average_lines = int(df_lines.loc[[f"{personaje}"], ["percentage"]].values[0][0])
    
    return f"{personaje} has appeared in {episode_percentage}% of episodes, {scene_percentage}% of scenes, and has an average of {average_lines} lines per episode 🍌"


