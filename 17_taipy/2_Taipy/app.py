#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro


Link de estudo -->  https://github.com/Avaiga/taipy?tab=readme-ov-file

Executar o Script
=================
$ python main.py
"""
import taipy as tp
import pandas as pd
from taipy import Config, Scope, Gui

# Taipy Scenario & Data Management

# Filtering function - task
def filter_genre(initial_dataset: pd.DataFrame, selected_genre):
    filtered_dataset = initial_dataset[initial_dataset["genres"].str.contains(selected_genre)]
    filtered_data = filtered_dataset.nlargest(7, "Popularity %")
    return filtered_data

# Load the configuration made with Taipy Studio
Config.load("config.toml")
scenario_cfg = Config.scenarios["scenario"]

# Start Taipy Core service
tp.Core().run()

# Create a scenario
scenario = tp.create_scenario(scenario_cfg)


# Taipy User Interface
# Let's add a GUI to our Scenario Management for a full application

# Callback definition - submits scenario with genre selection
def on_genre_selected(state):
    scenario.selected_genre_node.write(state.selected_genre)
    tp.submit(scenario)
    state.df = scenario.filtered_data.read()

# Get list of genres
genres = [
    "Action", "Adventure", "Animation", "Children", "Comedy", "Fantasy", "IMAX"
    "Romance","Sci-FI", "Western", "Crime", "Mystery", "Drama", "Horror", "Thriller", "Film-Noir","War", "Musical", "Documentary"
    ]

# Initialization of variables
df = pd.DataFrame(columns=["Title", "Popularity %"])
selected_genre = "Action"

## Set initial value to Action
def on_init(state):
    on_genre_selected(state)

# User interface definition
my_page = """
# Film recommendation

## Choose your favorite genre
<|{selected_genre}|selector|lov={genres}|on_change=on_genre_selected|dropdown|>

## Here are the top seven picks by popularity
<|{df}|chart|x=Title|y=Popularity %|type=bar|title=Film Popularity|>
"""

Gui(page=my_page).run()
