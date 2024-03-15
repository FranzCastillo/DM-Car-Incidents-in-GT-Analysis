import os
import csv

def main():
    import csv

    def get_header(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            # Assuming the first row contains the headers
            headers = next(reader)
        return set(headers)

    def check_same_headers(csv_files):
        headers_set = None
        for csv_file in csv_files:
            headers = get_header(csv_file)
            if headers_set is None:
                headers_set = headers
            elif headers_set != headers:
                return False
        return True

    # Get all CSV files in the data directory
    data_dir = 'data'
    csv_files = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.csv')]

    if check_same_headers(csv_files):
        print("All CSV files have the same headers.")
    else:
        print("CSV files have different headers.")


if __name__ == '__main__':
    main()