"""
Connects to the database in the hiden directory
"""

import os
import sqlite3
import platform


class Config():
    """
    Docstring
    """
    def __init__(self) -> None:
        # Locate the database file
        system = platform.system()
        home_dir = os.path.expanduser("~")
        hidden_dir = home_dir+"/.OnkoDICOM"
        fname = "/OnkoDICOM.db"
        dbfile = hidden_dir+fname

        # Checks if the config file exists. if it doesnt then create it
        if not os.path.exists(dbfile):

            # If the hidden direcroty does not exist then create it
            if not os.path.exists(hidden_dir):
                os.mkdir(hidden_dir)

            # Writing random values currently, replace with actual data
            self.write_config(dbfile, 0, home_dir, home_dir)

        # Read the config file
        results = self.read_config(dbfile)

        # I'm using the variables in my own config file
        # if they can vary between users,
        # use the results array instead of these variables
        id = results[0]
        default_dir = results[1]
        csv_dir = results[2]

    def read_config(self, dbfile):
        """
        Reads the config file and returns an array
        """
        # Connect to the database
        conn = sqlite3.connect(dbfile)

        # Create a cursor object
        cursor = conn.cursor()

        # Query the database for the single row of data
        query = "SELECT * FROM CONFIGURATION"
        cursor.execute(query)
        results = cursor.fetchone()

        # Close the database connection and return results
        conn.close()
        return results

    def write_config(self, dbfile, id, default_dir, csv_dir):
        """
        Creates and writes the config file
        """
        # Connect to the database
        conn = sqlite3.connect(dbfile)

        # Create a cursor object
        cursor = conn.cursor()

        # Write to the database
        conn.execute("""
            CREATE TABLE CONFIGURATION(
                id INTEGER PRIMARY KEY,
                default_dir TEXT,
                csv_dir TEXT
            )
        """)
        conn.execute(
            "INSERT INTO CONFIGURATION VALUES (?, ?, ?)",
            (id, default_dir, csv_dir)
        )
        conn.commit()

        # Close the database connection
        conn.close()

    def config_file_exists(self, dbfile):
        """
        Returns whether the config file exists
        """
        if os.path.exists(dbfile):
            return True
        else:
            return False

if __name__ == "__main__":
    con = Config()
