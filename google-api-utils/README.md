# finance-google-utils

Finance repository intended to store Classes and Functions related to Google Services such as Drive, Sheets, Docs...

In order to use these functions, firstly you need to install the package in your project by running:

    pip install google-api-utils

## First Steps

In order to create a Drive or Sheets instance you will need some mandatory credentials from a valid Google API account:
* **Project ID**: The ID of your Google Cloud Plataform Project. (https://support.google.com/googleapi/answer/7014113?hl=en&ref_topic=7014522)
* **Client ID**: Your Google API client ID. (https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid)
* **Client Email**: Your registered e-mail in Google API
* **Client x509 Certificate URL**: The URL of the public x509 certificate, used to verify JWTs signed by the client. (https://stackoverflow.com/questions/28638830/purpose-of-client-x509-cert-url-field-in-json-file-generated-by-google-oauth-2)
* **Private Key ID**: The key ID of the Service Account. (https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
* **Private Key**: The key of the Service Account. (https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

If you need any help finding it, access your API Credentials (https://console.cloud.google.com/apis/credentials).

## Example of Usage

In the next example, the google-api-utils lib is used to read and print a PDF file from a Drive folder.

    from google_api_utils import Google
    import fitz

    private_key = "YOUR-PRIVATE-KEY"
    private_key_id = "YOUR-PRIVATE-KEY-ID"
    client_email = "YOUR-CLIENT-EMAIL"
    client_id = "YOUR-CLIENT-ID"
    client_x509_cert_url =  "YOUR-CLIENT-X509-CERT-URL"
    project_id = "YOUR-PROJECT-ID"

    # Initialize an instance of a drive object
    drive = Google.Drive(project_id, client_id, client_email, client_x509_cert_url, private_key_id, private_key)

    # Listing all files inside this ID's folder
    files = drive.list_files('17fjlUxF_VskHUCKaAt5QZLtqdds4psy5')

    # Reading in memory the first PDF file found
    fileIO = drive.read_file(files[0]['id'])

    # Using PyMuPDF to read and print PDF's content
    doc = fitz.open("pdf", fileIO)

    text= ""
    for page in doc:
        text += page.getText()

    print(text)


## Class Drive

This python class was created to deal with Drive functionalities such as listing files from a folder, reading and downloading it.

### Listing Files
List all metadata from files inside the Drive's folder.

[Arguments] :
* *folder_id*: ID from the folder where the files are. (str)

[Return] : List containing Dictionaries with the metadata (List)
### Create Folder
Creates a Drive Folder, in case it does not exists.

[Arguments] :
* *parent_id*: ID from the parent folder. (str)
* *folder_name*: Name of the new folder. (str)

[Return] : ID of the new folder (str)

### Download File
Downloads locally a file from your Drive. It is important that the file is shared with your email account.

[Arguments] :
* *file_id*: ID from the file you. (str)
* *file_path*: Local path where the file will be downloaded. (str)

[Return] : Path where the file can be found (str)
### Read File
Reads the file's content in memory, returning its Bytes. Since every type of file has its own way to deal with bytes, it is recommended to search for it.

[Arguments] :
* *file_id*: ID from the file you. (str)

[Return] : Bytes from the file (io.BytesIO)

### Move File

Allows user to move files between folders in there Drive. Notice that it moves only files from a specific MimeType. For more information about Google's mimetypes access https://developers.google.com/drive/api/v3/mime-types

[Arguments] :
* *source_id*: ID from the source folder.(str)
* *target_id*: ID from the destination folder. (str)
* *mimeType*: MimeType of the files to move. (str)

[Return] : None


### Delete File

This function is intended to delete a file from your Drive. Notice, however, that the API cannot delete a file that it is not owner. So, the function actually removes its own access to the file.

[Arguments] :  
* *file_id*: ID from the file you want to delete. (str)

[Return] : None

## Class Sheets

Python class created to deal with Sheets functionalities.

### Reading a Spreadsheet
Allows the user to read a spreadsheet from Google and turn it into a Dataframe.

[Arguments] :  
* *spreadsheet_id*: ID from the Google Spreadsheet. (str)
* *spreadsheet_range*: Google Sheets Range such as "Page1:A1:Z". (str)

[Return] : Dataframe containing the desired data. (pandas Dataframe)


### Writing a Spreadsheet
Allows the user to overwrite any data inside a Google spreadsheet. The values need to be organized in a way where lines are Lists and the value cells are items from this List.

For example,
    *values* = [["Hello, World!", "1"], ["Testing!"]] 

will be written in the specified range as:

![Example from Spreadsheet overwrite](https://imgur.com/TLXjPWc.jpg)

[Arguments] :  
* *spreadsheet_id*: ID from the Google Spreadsheet. (str)
* *spreadsheet_range*: Google Sheets Range such as "Page1:A1:Z". (str)
* *values*: List with the new values separated in lines and cells. (List)

[Return] : Request answer from the write (Dict)

