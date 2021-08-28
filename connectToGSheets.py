import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class connectToGoogleSheets:
    """ This class was created to connect with Google Sheets API and retrieve data from some Google Spreadsheets
    Sheet as a DataFrame. """

    def __init__(self, credsFilePath):
        """ The __init__ method deals with the Google Sheets Api Authentication.
        :parameter credsFilePath: The file path of service account credentials download from google console
        :type: str
        :return: authenticated self.client attribute
      """

        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(f"{credsFilePath}", self.scope)
        self.client = gspread.authorize(self.creds)
        return

    def getDataAndSaveItIntoDataFrame(self, spreadsheet_key, worksheet_name, headers_position, data_first_row,
                                      value_render_option="FORMATTED_VALUE"):
        """"This method get data from a Google Sheets Spreadsheet and transform it into a pandas dataframe.

         :param spreadsheet_key: The Google Sheets SpreadSheets Key. It could be retrieved from Google Sheets URL.
         :type spreadsheet_key: str

         :param worksheet_name: The name of worksheet that contains the data that will be retrieved.
         :type worksheet_name: str

         :param headers_position: The row that represents the spreadsheet headers. Count starts from 0.
         :type headers_position: int

         :param data_first_row: The row that represents the data first row (excluding headers). Count starts from 0.
         :type data_first_row: int

         :param str value_render_option: (optional) Determines how values should
            be rendered in the the output. See `ValueRenderOption`_ in
            the Sheets API.
            Possible values are:
            ``FORMATTED_VALUE``
                (default) Values will be calculated and formatted according
                to the cell's formatting. Formatting is based on the
                spreadsheet's locale, not the requesting user's locale.
            ``UNFORMATTED_VALUE``
                Values will be calculated, but not formatted in the reply.
                For example, if A1 is 1.23 and A2 is =A1 and formatted as
                currency, then A2 would return the number 1.23.
            ``FORMULA``
                Values will not be calculated. The reply will include
                the formulas. For example, if A1 is 1.23 and A2 is =A1 and
                formatted as currency, then A2 would return "=A1".
        .. _ValueRenderOption: https://developers.google.com/sheets/api/reference/rest/v4/ValueRenderOption

         :return: Pandas dataframe object.
        """
        if value_render_option not in ("FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"):
            raise ValueError("value_render_option must be: 'FORMATTED_VALUE' or"
                             " 'UNFORMATTED_VALUE' or 'FORMULA'")

        sheet = self.client.open_by_key(spreadsheet_key).worksheet(worksheet_name)
        table = sheet.get_all_values(value_render_option=value_render_option)
        headers = sheet.get_all_values()[headers_position]
        df = pd.DataFrame(table[data_first_row:], columns=headers)
        return df
