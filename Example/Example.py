from google_api_utils import Google
import fitz

private_key = ""
private_key_id = ""
client_email = ""
client_id = ""
client_x509_cert_url =  ""
project_id = ""

drive = Google.Drive(project_id, client_id, client_email, client_x509_cert_url, private_key_id, private_key)

files = drive.list_files('17fjlUxF_VskHUCKaAt5QZLtqdds4psy5')

fileIO = drive.read_file(files[0]['id'])

doc = fitz.open("pdf", fileIO)

text= ""
for page in doc:
    text += page.getText()

print(text)