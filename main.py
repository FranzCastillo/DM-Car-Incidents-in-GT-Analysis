import os
import csv

def main():
    # Define the directory where the CSV files are located
    data_dir = 'data'

    # Get a list of all CSV files in the directory
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

    # Initialize an empty list to store headers
    headers = []

    # For each CSV file in the directory
    for file in csv_files:
        # Open the file and read the first line (header)
        with open(os.path.join(data_dir, file), 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            # Add the header to the list of headers
            headers.append(header)

    # Get the first header as the standard
    standard_header = headers[0]

    # For each header in the list of headers
    for i, header in enumerate(headers):
        # If the header is not the same as the standard
        if set(header) != set(standard_header):
            # Print the file name and the missing headers
            missing_headers = set(standard_header) - set(header)
            print(f"The file {csv_files[i]} is missing the following headers: {missing_headers}")

if __name__ == '__main__':
    main()