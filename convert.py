import csv
import pandas as pd

MAIN_COLUMN_NAMES = ["COUNTRY", "Country", "PRODUCT", "Product", "SECTOR", "Sector", "FLOW", "Flow"]
KEY_COLUMN_NAMES = ["Country", "Product", "Sector", "Flow"]
TIME_COLUMN_NAME = "TIME"
VALUE_COLUMN_NAME = "Value"

def get_representative_rows(csv_data):
    """
    CSV データの中で MAIN_COLUMN_NAMES の値が等しい行をまとめてグループにし、各グループから１行ずつ代表行を適当に取得する
    """
    duplicates_dropped = csv_data.drop_duplicates(KEY_COLUMN_NAMES)
    return duplicates_dropped.iterrows()

def get_time_column_names(csv_data):
    """
    CSV データの中で TIME 行の値を重複なしに全部取得する
    """
    unique_time_rows = csv_data.drop_duplicates([TIME_COLUMN_NAME])
    time_column_names = sorted([ row[TIME_COLUMN_NAME] for index, row in unique_time_rows.iterrows() ])
    return time_column_names


def get_rows_from_representative_row(csv_data, representative_row):
    """
    MAIN_COLUMN_NAMES の値が代表行と等しい行をすべて取得する
    """
    row_selector = None
    row_selectors = [ csv_data[column_name] == representative_row[column_name] for column_name in KEY_COLUMN_NAMES ]
    for selector in row_selectors:
        row_selector = selector if row_selector is None else (row_selector & selector)

    rows = csv_data[row_selector]
    return rows


if __name__ == "__main__":

    # 入出力のファイル名を変更するにはここを編集する
    input_file = "./samples/original.csv"
    output_file = "output.csv"

    csv_data = pd.read_csv(input_file)

    representative_rows = get_representative_rows(csv_data)

    time_column_names = get_time_column_names(csv_data)

    converted_csv_data = pd.DataFrame(data=None, columns=(MAIN_COLUMN_NAMES + time_column_names))
    for index, representative_row in representative_rows:
        rows = get_rows_from_representative_row(csv_data, representative_row)

        time_and_values = pd.Series(
            index=rows[TIME_COLUMN_NAME].tolist(),
            data=rows[VALUE_COLUMN_NAME].tolist())

        new_row = representative_row.loc[MAIN_COLUMN_NAMES].append(time_and_values)

        converted_csv_data = converted_csv_data.append(new_row, ignore_index=True, verify_integrity=True)

    converted_csv_data.to_csv(output_file, index=None)
