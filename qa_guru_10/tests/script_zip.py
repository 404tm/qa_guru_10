from zipfile import ZipFile

def test_zip_file():

    extract_dir = 'extract_dir'

    with ZipFile("resources/Archive.zip") as reader:
        print(reader.namelist())
        reader.extractall(extract_dir)



