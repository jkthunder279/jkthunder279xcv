# utils/helpers.py

"""
Utility functions for formatting and exporting data.
"""

from datetime import datetime


def format_datetime(dt):
    """
    Format a datetime object to a string in YYYY-MM-DD HH:MM:SS format.
    """
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def export_to_csv(data, filename):
    """
    Export a list of dictionaries to a CSV file.
    """
    import csv
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

