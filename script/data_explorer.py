import pandas as pd
import numpy as np
import argparse

def find_tournament(file_path):
    try:
        df = pd.read_csv(file_path)
        unique_tournament = df['tournament'].str.strip().unique()
        return unique_tournament
    except FileNotFoundError:
        print("File not found: {file_path}")
    except Exception as e:
        print("An error occurred: {str(e)}")

def find_country(file_path):
    try:
        df = pd.read_csv(file_path)
        unique_country = df['country'].str.strip().unique()
        return unique_country
    except FileNotFoundError:
        print("File not found: {file_path}")
    except Exception as e:
        print("An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Extract unique tournament names and countries from a CSV file.")
    parser.add_argument("csv_file", help="Path to the CSV file")
    args = parser.parse_args()
    csv_file_path = args.csv_file

    tournaments = find_tournament(csv_file_path)
    countries = find_country(csv_file_path)

    if tournaments.size > 0:
        print("Unique Tournament Names:")
        for name in tournaments:
            print(name)

    if countries.size > 0:
        print("Unique Countries:")
        for country in countries:
            print(country)

if __name__ == "__main__":
    main()
