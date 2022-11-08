import urllib
import requests, zipfile, io


class GetDataByUrl:
    def __init__(self):
        self.url = ""

    def get_Data_By_File(self, url_file_input, filename):
        self.url = url_file_input
        return urllib.request.urlretrieve(self.url, filename)

    def get_Data_By_Zip(self, url_file_zip):
        read_ = requests.get(url_file_zip)
        zip_data = zipfile.ZipFile(io.BytesIO(read_.content))
        return zip_data.extractall("H:/Coursera_ML_models/")
