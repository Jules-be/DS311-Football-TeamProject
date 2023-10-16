import pandas as pd
import numpy as np
import argparse

file = "data/fifa_world_cup.csv"

def find_tournament():
    df = pd.read_csv(file)
    unique_tournament = df['tournament'].str.strip().unique()
    print(unique_tournament)

def find_country():
    df = pd.read_csv(file)
    unique_country = df['country'].str.strip().unique()
    print(unique_country)

if __name__ == "__main__":
    find_tournament()
    find_country()
