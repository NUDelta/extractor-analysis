from datetime import datetime
from .scrapers import gsheet
from .soap import SoapNote


class Project:
    def __init__(self, name, sig, students, soap_url, soap_sheet_num=0):
        self.name = name
        self.sig = sig
        self.students = students

        self.soap_url = soap_url
        self.soap_sheet_num = soap_sheet_num
        self.soap_notes = []

    def scrape_soap_notes(self):
        # fetch soap note from google sheets
        soap_cols = ['date', 'subjective', 'objective', 'assessment', 'plan']
        soap_notes = gsheet.load_google_sheet_data(self.soap_url, sheet_num=self.soap_sheet_num,
                                                   new_col_names=soap_cols)

        # format soap notes using SoapNote class
        for index, soap_note in soap_notes.iterrows():
            curr_date = datetime.strptime(soap_note['date'], '%m/%d/%y')

            curr_soap_note = SoapNote(curr_date)
            curr_soap_note.set_soap_content(soap_note['subjective'],
                                            soap_note['objective'],
                                            soap_note['assessment'],
                                            soap_note['plan'])

            # add soap note to array
            self.soap_notes.append(curr_soap_note)
