# Disclaimer: This tool is only made for educational purpose. Do not use against any photos that you don't own or have authorization to test. 
# It supports only JPEG extenstion

import os
import sys
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS


def convert_decimal_degrees(degree, minutes, seconds, direction):
    decimal_degrees = degree + minutes / 60 + seconds / 3600
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees

def create_google_maps_url(gps_coords):            
    dec_deg_lat = convert_decimal_degrees(float(gps_coords["lat"][0]),  float(gps_coords["lat"][1]), float(gps_coords["lat"][2]), gps_coords["lat_ref"])
    dec_deg_lon = convert_decimal_degrees(float(gps_coords["lon"][0]),  float(gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
    return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"
        

print("""

  ________   _______ ______   ________   _________ _____            _____ _______ ____  _____  
 |  ____\ \ / /_   _|  ____| |  ____\ \ / /__   __|  __ \     /\   / ____|__   __/ __ \|  __ \ 
 | |__   \ V /  | | | |__    | |__   \ V /   | |  | |__) |   /  \ | |       | | | |  | | |__) |
 |  __|   > <   | | |  __|   |  __|   > <    | |  |  _  /   / /\ \| |       | | | |  | |  _  / 
 | |____ / . \ _| |_| |      | |____ / . \   | |  | | \ \  / ____ \ |____   | | | |__| | | \ \ 
 |______/_/ \_\_____|_|      |______/_/ \_\  |_|  |_|  \_\/_/    \_\_____|  |_|  \____/|_|  \_\

                                                                  MADE WITH ❤️ BY LIGHTNINGSTAR                                    
""")

while True:
    output_choice = input("Add some files in ./Data folder to get Exif data:\nPress 1 to continue :  ")
    try:
        conv_val = int(output_choice)
        if conv_val == 1:
            sys.stdout = open("extracted_data.txt", "w")
            break
        else:
            print("You entered an incorrect option, please try again.")
    except:
        print("You entered an invalid option, please try again.")

 
cwd = os.getcwd()
os.chdir(os.path.join(cwd, "Data"))
files = os.listdir()

if len(files) == 0:
    print("You don't have have files in the Data folder add some files to see the output.")
    exit()

for file in files:
    
    try:
        image = Image.open(file)
        print(f"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _{file}_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        gps_coords = {} 
        if image._getexif() == None:
            print(f"{file} No exif data found.")
        else:
            for tag, value in image._getexif().items():
                tag_name = TAGS.get(tag)
                if tag_name == "GPSInfo":
                    for key, val in value.items():
                        
                        print(f"{GPSTAGS.get(key)} - {val}")
                        
                        if GPSTAGS.get(key) == "GPSLatitude":
                            gps_coords["lat"] = val
                        elif GPSTAGS.get(key) == "GPSLongitude":
                            gps_coords["lon"] = val
                        elif GPSTAGS.get(key) == "GPSLatitudeRef":
                            gps_coords["lat_ref"] = val
                        elif GPSTAGS.get(key) == "GPSLongitudeRef":
                            gps_coords["lon_ref"] = val   
                else:
                    
                    print(f"{tag_name} - {value}")
             
            if gps_coords:
                print(create_google_maps_url(gps_coords))
           
    except IOError:
        print("File format not supported!")

if output_choice == "1":
    sys.stdout.close()
os.chdir(cwd)
