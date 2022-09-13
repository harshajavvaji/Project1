from zipfile import ZipFile
import os
import datetime

def find_zip_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.zip')]
# os.remove(os.getcwd())
# path1=os.path.join(os.getcwd(),results)
# print(path1)
ZIP_Files_PATH = 'C://Users/jharshav/Documents/task1/zip'
for f in find_zip_files(ZIP_Files_PATH):
    with ZipFile(f, 'r') as zip:
        zip.extractall(ZIP_Files_PATH) # zip.extractall(PATH)

RESULT_PATH = 'C://Users/jharshav/Documents/task1/results'

# check for html files in the directory after unzipping in path ZIP_Files_PATH and also child folders
RESULT_HTML_FILE = 'result' + datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S") + '.html'
for root, dirs, files in os.walk(ZIP_Files_PATH):
    for f in files:
        if f.endswith('.html') and 'report' in f:
            if os.path.isfile(os.path.join(RESULT_PATH, RESULT_HTML_FILE)):
                pass
            else:
                for cur_root, cur_dirs, cur_files in os.walk(RESULT_PATH):
                    for cf in cur_files:
                        if cf != RESULT_HTML_FILE:
                            os.remove(os.path.join(RESULT_PATH, cf))
            # Now merge all the .html files into single file and save it in RESULT_PATH
            with open(os.path.join(RESULT_PATH, RESULT_HTML_FILE), 'a', encoding='utf-8') as html:
                print("File is: ", html.name)
                # Read the content from each "f" and append that content into a new file result.html in RESULT_PATH
                with open(os.path.join(root, f), 'r', encoding='utf-8') as html_file:
                    html.write(
                    """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Document</title>
                    </head>
                    <body>
                    """
                    +
                    """<iframe src="{}" width="100%" style="height:100vh"></iframe>""".format(html_file.name) +
                    """</body>
                    </html>"""
                    )