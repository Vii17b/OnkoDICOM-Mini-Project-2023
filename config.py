""""
Reads the config file
"""

import os
import sqlite3
import platform


def read_config(dbf):
    """
    Reads the config file and returns an array
    """
    # Connect to the database
    conn = sqlite3.connect(dbf)

    # Create a cursor object
    cursor = conn.cursor()

    # Query the database for the single row of data
    query = "SELECT * FROM CONFIGURATION"
    cursor.execute(query)
    out = cursor.fetchone()

    # Close the database connection and return results
    conn.close()
    return out


def write_config(dbf, f_id, dflt_dir, csv):
    """
    Make + write config file
    """
    # Connect to the database
    conn = sqlite3.connect(dbf)

    # Write to the database
    conn.execute(
        """CREATE TABLE CONFIGURATION(id INTEGER PRIMARY KEY,
        default_dir TEXT, csv_dir TEXT)""")
    conn.execute(
        "INSERT INTO CONFIGURATION VALUES (?, ?, ?)",
        (f_id, dflt_dir, csv))
    conn.commit()

    # Close the database connection
    conn.close()


def config_file_exists(dbf):
    """
    Returns whether the config file exists
    """
    return bool(os.path.exists(dbf))


# Identify the OS
system = platform.system()
# Locate the database file
home_dir = os.path.expanduser("~")
hidden_dir = home_dir+"/.OnkoDICOM"
FNAME = "/OnkoDICOM.db"
dbfile = hidden_dir+FNAME

# Checks if the config file exists. if it doesnt then create it
if not os.path.exists(dbfile):

    # If the hidden direcroty does not exist then create it
    if not os.path.exists(hidden_dir):
        os.mkdir(hidden_dir)

    # Writing random values currently, replace with actual data
    write_config(dbfile, 0, home_dir, home_dir)

# Read the config file
results = read_config(dbfile)

# I'm using the variables in my own config file, if they can vary between users
# use the results array instead of these variables
file_id = results[0]
default_dir = results[1]
csv_dir = results[2]
