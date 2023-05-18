"""
Reads the config file
"""

import os
import sqlite3


class Config:
    """
    Reads the config file
    """

    def __init__(self, controller):
        self.controller = controller

        # Locate the database file
        home_dir = os.path.expanduser("~")
        hidden_dir = home_dir + "/.OnkoDICOM"
        fname = "/OnkoDICOM.db"
        dbfile = hidden_dir + fname

        # Checks if the config file exists. if it doesnt then create it
        if not os.path.exists(dbfile):
            # If the hidden direcroty does not exist then create it
            if not os.path.exists(hidden_dir):
                os.mkdir(hidden_dir)

            # Prompt the user for default directory, then save it to the config
            self.controller.default_directory_prompt(self, dbfile)
        else:
            # If we don't have to wait for the user,
            # respond to the controller immediately
            self.send_results(dbfile)

    def send_results(self, dbfile):
        """
        Tells the controller that the config file has been resolved
        """
        # Read the config file and return
        results = self.read_config(dbfile)
        self.db_id = results[0]
        self.default_dir = results[1]
        self.csv_dir = results[2]
        self.controller.config_resolved(self)

    def read_config(self, dbf):
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

    def write_config(self, dbf, f_id, dflt_dir, csv):
        """
        Make + write config file
        """
        # Connect to the database
        conn = sqlite3.connect(dbf)

        # Write to the database
        conn.execute(
            """CREATE TABLE CONFIGURATION(id INTEGER PRIMARY KEY,
            default_dir TEXT, csv_dir TEXT)"""
        )
        conn.execute(
            "INSERT INTO CONFIGURATION VALUES (?, ?, ?)", (f_id, dflt_dir, csv)
        )
        conn.commit()

        # Close the database connection
        conn.close()

    def supply_default_directory(self, dbfile, home_dir):
        """
        Allows the directory window to write to the config
        then lets the main controller continue
        """
        self.write_config(dbfile, 0, home_dir, home_dir)
        self.send_results(dbfile)


if __name__ == "__main__":
    con = Config()
