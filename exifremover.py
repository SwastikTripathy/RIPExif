# Disclaimer: This tool is only made for educational purpose. Do not use against any photos that you don't own or have authorization to test. 
# It supports only JPEG extenstion

print("""

  ________   _______ ______   _____  ______ __  __  ______      ________ _____  
 |  ____\ \ / /_   _|  ____| |  __ \|  ____|  \/  |/ __ \ \    / /  ____|  __ \ 
 | |__   \ V /  | | | |__    | |__) | |__  | \  / | |  | \ \  / /| |__  | |__) |
 |  __|   > <   | | |  __|   |  _  /|  __| | |\/| | |  | |\ \/ / |  __| |  _  / 
 | |____ / . \ _| |_| |      | | \ \| |____| |  | | |__| | \  /  | |____| | \ \ 
 |______/_/ \_\_____|_|      |_|  \_\______|_|  |_|\____/   \/   |______|_|  \_\
                                                                                
                                                   MADE WITH ❤️ BY LIGHTNINGSTAR
                                                    
""")


import os
from PIL import Image

cwd = os.getcwd()
os.chdir(os.path.join(cwd, "Data"))
files = os.listdir()

if len(files) == 0:
    print("You dont have files in ./Data folder add some to remove exif data.")
    exit()
for file in files:
    try:
        img = Image.open(file)
        img_data = list(img.getdata())
        img_no_exif = Image.new(img.mode, img.size) 
        img_no_exif.putdata(img_data)
        img_no_exif.save(file)
    except IOError:
        print("File format not supported! Use .JPEG files")
