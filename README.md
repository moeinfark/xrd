## Xrd data visualization guide

This guide is designed to allow you to use the python codes available at this page in order to use online databases and create xrd pattern documentations alongside visualization of these data sets.

#### System Requirements:

> since the code is done in python language, you should have this language installed on your operating system.

- In order to use these codes you need to install the packages mentioned in the “requirements” file. To do so you should open cmd in files directory and write the following command 
    “pip install -r requirements.txt”
  
- For running “MP xrd api” file you need to get an API key from “https://next-gen.materialsproject.org/” . you should save this key in a text file in the same directory as the python program. This file should be named “.env”. The api key inside the file should be stored in the format “MP_API_KEY={your_api_key}” with no space or anything else added to this format only replace {your_api_key} with the key you get from the website.

#### how to run the code:

- For “mp xrd api” after providing the api key in the above mentioned format, you must search for material_id in “https://next-gen.materialsproject.org/”. Then you write down the id inside the code in line 16 as the following example which is for cubic nickel with material_id (mp-1008728)

    material_id = "mp-1008728"
  
- For running “cod xrd cif file.py” you need to download a cif file in the same directory as the code has been saved to. After that you need to replace the file name inside the code in line 9 as the following example : 

    cif_file_name="file_name.cif"

