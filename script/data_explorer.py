import csv
import argparse

def find_tournament(file_path):
    tournament_names = set()

    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tournament_name = row['tournament'].strip()
                tournament_names.add(tournament_name)

    except FileNotFoundError:
        print("File not found: {file_path}")
    except Exception as e:
        print("An error occurred: {str(e)}")

    return list(tournament_names)

def find_country(file_path):
    countries = set()

    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                country = row['country'].strip()
                countries.add(country)

    except FileNotFoundError:
        print("File not found: {file_path}")
    except Exception as e:
        print("An error occurred: {str(e)}")

    return list(countries)

def main():
    parser = argparse.ArgumentParser(description="Extract unique tournament names from a CSV file.")
    parser.add_argument("csv_file", help="Path to the CSV file")

    args = parser.parse_args()
    csv_file_path = args.csv_file

    tournament_names = find_tournament(csv_file_path)
    countries = find_country(csv_file_path)

    if tournament_names:
        print("Tournament in the list:")
        for name in tournament_names:
            print(name)
    else:
        print("No tournament found in the CSV file.")

    if countries:
        print("\n\nCountry in the list:")
        for country in countries:
            print(country)
    else:
        print("No country found in the CSV file.")

        

if __name__ == "__main__":
    main()
