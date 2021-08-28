# Connect-to-GSheets
This project seeks to create a simple and fast way to convert Google Sheets spreadsheets into pandas dataframe objects.

## Pre-execution steps

 - Create Google Developer Account;
 - Enable Google Sheets API;
 - Create Service Account to handle authentication;
 - Download Credential File from Google Developers;
 - Share the spreadsheet you want to extract data with service account email.
 
 These steps can be done using this guide as a reference: https://robocorp.com/docs/development-guide/google-sheets/interacting-with-google-sheets.

## Getting Started

### Dependencies
 - python 3.7
 - numpy~=1.19.5
- pandas~=1.1.5
- gspread~=3.6.0
- oauth2client~=4.1.3

See requirements.txt file in this repository,

### Installing

* Clone this repository
* Install requirements.txt

### Executing program

* Import the lib into your project
* Instantiate connectToGoogleSheets
* In Instance call the method getDataAndSaveItIntoDataFrame and set the parameters.


```python
from connectToGoogleSheets import connectToGoogleSheets

connection = connectToGoogleSheets(credsFilePath="credentials file path")

df = connection.getDataAndSaveItIntoDataFrame(spreadsheet_key= "fill with spreadsheet key", worksheet_name="fill with work sheet name", headers_position=0, data_first_row=1,  
value_render_option="value_render_option")

```
