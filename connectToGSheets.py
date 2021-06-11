import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
sys.path.insert(0, 'C:/Users/BI/PycharmProjects/connect-to-gsheets')

class connectToGoogleSheets:
    def __init__(self, credsFilePath):
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(f"{credsFilePath}",self.scope)
        self.client = gspread.authorize(self.creds)
        return

    def get_data(self, spreadsheet_key, worksheet_name, headersPosition, dataStartRow, value_render_option):
        sheet = self.client.open_by_key(spreadsheet_key).worksheet(worksheet_name)
        table = sheet.get_all_values(value_render_option=value_render_option)
        headers = sheet.get_all_values()[headersPosition]
        df = pd.DataFrame(table[dataStartRow:], columns=headers)
        return df

if __name__ == "__main__":
    connectToGoogleSheets(credsFilePath=r"C:\Users\BI\Desktop\80 20 Marketing\API\Autenticação\Sebrae\ConectarGoogleSheets-9bbd90f82eb4.json")