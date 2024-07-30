import os
import pandas as pd


def manage_csv(
    function_name: str,
    data: dict,
    file_path: str = "benchmark_results.csv",
    new_row: bool = True,
) -> None:
    """
    Handles logging of new data to a CSV file or updating an existing row.

    :param file_path: Path to the CSV file.
    :param function_name: Name of the function being logged.
    :param data: Dictionary containing metrics such as execution time and
        memory usage.
    """
    # Ensure the CSV file exists, creating it if necessary
    if not os.path.exists(file_path):
        print(f"Creating new CSV file at {file_path}")
        initial_columns = ["function_name"] + list(data.keys())
        df = pd.DataFrame(columns=initial_columns)
        df.to_csv(file_path, index=False)

    # Load the existing CSV into a DataFrame
    df = pd.read_csv(file_path)

    # Check for an existing row with the same function name
    existing_rows = df[df["function_name"] == function_name]

    if existing_rows.empty or new_row:
        # Append new data as a new row
        row = {"function_name": function_name, **data}
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        # Check if last row corresponding to the function is fully populated
        last_index = existing_rows.index[-1]
        last_row = df.loc[last_index]

        if all(pd.notna(last_row[col]) for col in data.keys()):
            # If fully populated, append a new row
            row = {"function_name": function_name, **data}
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        else:
            # Otherwise, update the existing row
            for metric, value in data.items():
                if metric not in df.columns:
                    df[metric] = None  # Ensure the column exists
                df.loc[last_index, metric] = value

    # Write the modified DataFrame back to the CSV
    df.to_csv(file_path, index=False)
