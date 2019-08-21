# google
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# setup connection
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
gc = gspread.authorize(credentials)


def load_google_sheet_data(url, sheet_num=0, new_col_names=[]):
    """
    Loads in and returns google sheet as a Pandas DataFrame with header remapped according to values above.

    Inputs:
        url (string): url of spreadsheet to load in
        new_col_names (list): list of strings for new column names

    Returns:
        (DataFrame): Pandas DataFrame with header remapped above
    """
    url_connection = gc.open_by_url(url)
    raw_data = url_connection.get_worksheet(sheet_num).get_all_values()

    output_df = pd.DataFrame(raw_data[1:], columns=raw_data[0])
    if len(new_col_names) > 0:
        output_df.columns = new_col_names

    return output_df
