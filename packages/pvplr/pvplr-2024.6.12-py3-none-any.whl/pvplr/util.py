""" Auto-Download Module

This function downloads RTC power data from the OSF database. 

"""

import requests
import os

def RTC_download(
    output_file, 
    output_dir
):
    """
    Helper function that downloads CSV file from OSF Database

    Args:
        output_file (string): name for CSV file
        output_dir (string): directory for which the file should be saved in
    """
    
    url = 'https://osf.io/qmvfu/download'
    
    response = requests.get(url)
    response.raise_for_status()  

    file_path = os.path.join(output_dir, output_file)
    with open(file_path, 'wb') as file:
        file.write(response.content)

    print(f"CSV file downloaded as {output_file}")
