################################################################################
## Author: Selegean Marius Florin                                              #
## Email: marius.selegean@yahoo.com                                            #
## Description: Move files in named folders grouped by their extensions types  #
################################################################################
"""
Documantation:
--------------------------------------------------------------------------------
This code will find the defined extensions from the folder where it is placed
and will move the files into newly automated created sub-folders. If the folders
already exists then the creation of folders is skipped.
When scanning the folder, if files are found for the specific extension this
will be skipped and program will scan to find the next extension.

Instructions:
1. Copy the script into the desired folder.
2. Run the script using in a command line.
3. Follow instructions and allow program to move the files found into the folders
4. You can check the log files if needed.
"""
# Import packages
import os
import glob
import sys
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt


# Path
os.chdir

# Variables used in this script
HAR = '*.har'
TEXT = '*.txt'
MP3 = '*.mp3'
MP4 = '*.mp4'
PDF = '*.pdf'
EXCEL = '*.xlsx'
WORD = '*.docx'
PICTURES1 = '*.jp*'
PICTURES2 = '*.png'
# Template
# variable = ''

# Opening the log file. If the log file does not exist then it will be created automatically.
log = open("../logs.log", "a", encoding="utf-8")

'''
Function that creates new folders for each configured extensions.
'''
def create_folder(folder_name):
    """
    This function creates check if folders exists. If they don't then the folders will be created.
    """
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f'New folder {folder_name} created.')
        log.write(f"[{datetime.datetime.now()}]\tNew folder {folder_name} created.\n")
    else:
        print(f'Folder {folder_name} already exists.')
        log.write(f"[{datetime.datetime.now()}]\tFolder {folder_name} already exists.\n")

def main():
    """
    Creating folders
    """
    log = open("../logs.log", "a")
    confirm = input('Do you want to create new folders for HAR, MP3, MP4, TEXT, PDF, EXCEL, WORD and Pictures filetypes? (y/n)')

    if confirm in ['Y', 'y']:
        create_folder('HAR')
        create_folder('MP3')
        create_folder('MP4')
        create_folder('TEXT')
        create_folder('PDF')
        create_folder('EXCEL')
        create_folder('WORD')
        create_folder('Pictures')
        # Template
        # create_folder('_name of variable_')
    else:
        print('\n''Operation Aborted!''\n''No files will be moved.''\n')
        log.write(f"[{datetime.datetime.now()}]\tOperation Aborted!''\n''No files will be moved.\n")
        sys.exit()

if __name__ == "__main__":
    main()

# 1 second break
time.sleep(1)
print("\n")

"""
Functions used in this script:
"""
# Create Dictionary
count_data = {}
def move_files_to_har_folder(HAR, log):
    """
    Moving HAR files to folder
    """
    count = 0
    for file in glob.glob(HAR, recursive=False):
        count += 1
        try:
            os.rename(file, os.path.join('HAR', os.path.basename(file)))
            print(f'{file} moved to HAR folder')
            log.write(f"[{datetime.datetime.now()}]\t{file} moved to HAR folder\n")
        except Exception as e:
            print(f'Error moving {file}: {e}')
            log.write(f"[{datetime.datetime.now()}]\tError moving {file}: {e}\n")

    print(f'Moved {count} files to HAR folder.')
    log.write(f"[{datetime.datetime.now()}]\tMoved {count} files to HAR folder.\n")
    count_data['HAR'] = count


def move_files_to_TEXT_folder(TEXT, log):
    """
    Moving TEXT files to folder
    """
    count = 0
    for file in glob.glob(TEXT, recursive=False):
        count += 1
        try:
            os.rename(file, os.path.join('TEXT', os.path.basename(file)))
            print(f'{file} moved to TEXT folder')
            log.write(f"[{datetime.datetime.now()}]\t{file} moved to TEXT folder\n")
        except Exception as e:
            print(f'Error moving {file}: {e}')
            log.write(f"[{datetime.datetime.now()}]\tError moving {file}: {e}\n")

    print(f'Moved {count} files to TEXT folder.')
    log.write(f"[{datetime.datetime.now()}]\tMoved {count} files to TEXT folder.\n")
    count_data['TEXT'] = count

def move_files_to_MP3_folder(MP3, log):
    """
    Moving MP3 files to folder
    """
    count = 0
    for file in glob.glob(MP3, recursive=False):
        count += 1
        try:
            os.rename(file, os.path.join('MP3', os.path.basename(file)))
            print(f'{file} moved to MP3 folder')
            log.write(f"[{datetime.datetime.now()}]\t{file} moved to MP3 folder\n")
        except Exception as e:
            print(f'Error moving {file}: {e}')
            log.write(f"[{datetime.datetime.now()}]\tError moving {file}: {e}\n")

    print(f'Moved {count} files to MP3 folder.')
    log.write(f"[{datetime.datetime.now()}]\tMoved {count} files to MP3 folder.\n")
    count_data['MP3'] = count

def move_files_to_MP4_folder(MP4, log):
    """
    Moving MP4 files to folder
    """
    count = 0
    for file in glob.glob(MP4, recursive=False):
        count += 1
        try:
            os.rename(file, os.path.join('MP4', os.path.basename(file)))
            print(f'{file} moved to MP4 folder')
            log.write(f"[{datetime.datetime.now()}]\t{file} moved to MP4 folder\n")
        except Exception as e:
            print(f'Error moving {file}: {e}')
            log.write(f"[{datetime.datetime.now()}]\tError moving {file}: {e}\n")

    print(f'Moved {count} files to MP4 folder.')
    log.write(f"[{datetime.datetime.now()}]\tMoved {count} files to MP4 folder.\n")
    count_data['MP4'] = count

def move_files_to_PDF_folder(PDF, log):
    """
    Moving PDF files to folder
    """
    count = 0
    for file in glob.glob(PDF, recursive=False):
        count += 1
        try:
            os.rename(file, os.path.join('PDF', os.path.basename(file)))
            print(f'{file} moved to PDF folder')
            log.write(f"[{datetime.datetime.now()}]\t{file} moved to PDF folder\n")
        except Exception as e:
            print(f'Error moving {file}: {e}')
            log.write(f"[{datetime.datetime.now()}]\tError moving {file}: {e}\n")

    print(f'Moved {count} files to PDF folder.')
    log.write(f"[{datetime.datetime.now()}]\tMoved {count} files to PDF folder.\n")
    count_data['PDF'] = count

def move_files_to_EXCEL_folder(EXCEL, log):
    """
    Moving EXCEL files to folder
    """
    count = 0
    for file in glob.glob(EXCEL, recursive=False):
        count += 1
        try:
            os.rename(file, os.path.join('EXCEL', os.path.basename(file)))
            print(f'{file} moved to EXCEL folder')
            log.write(f"[{datetime.datetime.now()}]\t{file} moved to EXCEL folder\n")
        except Exception as e:
            print(f'Error moving {file}: {e}')
            log.write(f"[{datetime.datetime.now()}]\tError moving {file}: {e}\n")

    print(f'Moved {count} files to EXCEL folder.')
    log.write(f"[{datetime.datetime.now()}]\tMoved {count} files to EXCEL folder.\n")
    count_data['EXCEL'] = count

def move_files_to_WORD_folder(WORD, log):
    """
    Moving WORD files to folder
    """
    count = 0
    for file in glob.glob(WORD, recursive=False):
        count += 1
        try:
            os.rename(file, os.path.join('WORD', os.path.basename(file)))
            print(f'{file} moved to WORD folder')
            log.write(f"[{datetime.datetime.now()}]\t{file} moved to WORD folder\n")
        except Exception as e:
            print(f'Error moving {file}: {e}')
            log.write(f"[{datetime.datetime.now()}]\tError moving {file}: {e}\n")

    print(f'Moved {count} files to WORD folder.')
    log.write(f"[{datetime.datetime.now()}]\tMoved {count} files to WORD folder.\n")
    count_data['WORD'] = count

# Template
"""
def move_files_to__name of variable__folder(_name of variable_, log):
    Moving _name of variable_ files to folder
    count = 0
    for file in glob.glob(_name of variable_, recursive=False):
        count += 1
        try:
            os.rename(file, os.path.join('_name of variable_', os.path.basename(file)))
            print(f'{file} moved to _name of variable_ folder')
            log.write(f"[{datetime.datetime.now()}]\t{file} moved to _name of variable_ folder\n")
        except Exception as e:
            print(f'Error moving {file}: {e}')
            log.write(f"[{datetime.datetime.now()}]\tError moving {file}: {e}\n")

    print(f'Moved {count} files to _name of variable_ folder.')
    log.write(f"[{datetime.datetime.now()}]\tMoved {count} files to _name of variable_ folder.\n")
"""


# 1 second break
time.sleep(1)

# Start scan and move

# Find and count HAR files
count = 0
for file in glob.glob(HAR, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} HAR files.\n")
log.write(f"[{datetime.datetime.now()}]\tFound {count} HAR files..\n")

# Input from user - Move files if found. If not, skip and move to next extnesion.
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    confirm = input('Do you want to move files to HAR Folder? (y/n)')
    if confirm in ["Y", "y"]:
        # Calling function
        move_files_to_har_folder(HAR, log)
print("\nScanning...")

# 1 second break
time.sleep(1)

# Find and count TEXT files

count = 0
for file in glob.glob(TEXT, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} TEXT files.\n")
log.write(f"[{datetime.datetime.now()}]\tFound {count} TEXT files..\n")

# Input from user - Move files if found. If not, skip and move to next extnesion.
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    confirm = input('Do you want to move files to TEXT Folder? (y/n)')
    if confirm in ["Y", "y"]:
        # Calling function
        move_files_to_TEXT_folder(TEXT, log)
print("\nScanning...")

# 1 second break
time.sleep(1)

# Find and count MP3 files

count = 0
for file in glob.glob(MP3, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} MP3 files.\n")
log.write(f"[{datetime.datetime.now()}]\tFound {count} MP3 files..\n")

# Input from user - Move files if found. If not, skip and move to next extnesion.
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    confirm = input('Do you want to move files to MP3 Folder? (y/n)')
    if confirm in ["Y", "y"]:
        # Calling function
        move_files_to_MP3_folder(MP3, log)
print("\nScanning...")

# 1 second break
time.sleep(1)

# Find and count MP4 files

count = 0
for file in glob.glob(MP4, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} MP4 files.\n")
log.write(f"[{datetime.datetime.now()}]\tFound {count} MP4 files..\n")

# Input from user - Move files if found. If not, skip and move to next extnesion.
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    confirm = input('Do you want to move files to MP4 Folder? (y/n)')
    if confirm in ["Y", "y"]:
        # Calling function
        move_files_to_MP4_folder(MP4, log)
print("\nScanning...")

# 1 second break
time.sleep(1)

# Find and count PDF files

count = 0
for file in glob.glob(PDF, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} PDF files.\n")
log.write(f"[{datetime.datetime.now()}]\tFound {count} PDF files..\n")

# Input from user - Move files if found. If not, skip and move to next extnesion.
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    confirm = input('Do you want to move files to PDF Folder? (y/n)')
    if confirm in ["Y", "y"]:
        # Calling function
        move_files_to_PDF_folder(PDF, log)
print("\nScanning...")

# 1 second break
time.sleep(1)

# Find and count EXCEL files

count = 0
for file in glob.glob(EXCEL, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} EXCEL files.\n")
log.write(f"[{datetime.datetime.now()}]\tFound {count} EXCEL files..\n")

# Input from user - Move files if found. If not, skip and move to next extnesion.
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    confirm = input('Do you want to move files to EXCEL Folder? (y/n)')
    if confirm in ["Y", "y"]:
        # Calling function
        move_files_to_EXCEL_folder(EXCEL, log)
print("\nScanning...")

# 1 second break
time.sleep(1)

# Find and count WORD files

count = 0
for file in glob.glob(WORD, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} WORD files.\n")
log.write(f"[{datetime.datetime.now()}]\tFound {count} WORD files..\n")

# Input from user - Move files if found. If not, skip and move to next extnesion.
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    confirm = input('Do you want to move files to WORD Folder? (y/n)')
    if confirm in ["Y", "y"]:
        # Calling function
        move_files_to_WORD_folder(WORD, log)
print("\nScanning...")

# Template
"""
count = 0
for file in glob.glob(_name of variable_, recursive=False):
    count += 1
    print(file)
    log.write(f"[{datetime.datetime.now()}]\t{file}\n")

print(f"Found {count} _name of variable_ files.\n")
log.write(f"[{datetime.datetime.now()}]\tFound {count} _name of variable_ files..\n")

# Input from user - Move files if found. If not, skip and move to next extnesion.
if count == 0:
    print("Skipping... moving to next folder.")
    log.write(f"[{datetime.datetime.now()}]\tSkipping... moving to next folder.\n")
else:
    confirm = input('Do you want to move files to _name of variable_ Folder? (y/n)')
    if confirm in ["Y", "y"]:
        # Calling function
        move_files_to__name of variable__folder(_name of variable_, log)
"""

# 1 second break
time.sleep(1)


# Find and count Pictures files
def move_picture_files_to_folder(PICTURES1, PICTURES2, log):
    """Move picture files to folder"""
    count = 0
    for file in glob.glob(PICTURES1, recursive=False):
        count += 1
        print(file)
        log.write(f"[{datetime.datetime.now()}]\t{file}\n")
    for file in glob.glob(PICTURES2, recursive=False):
        count += 1
        print(file)
        log.write(f"[{datetime.datetime.now()}]\t{file}\n")

    print(f"Found {count} Picture files.\n")
    log.write(f"[{datetime.datetime.now()}]\tFound {count} Picture files..\n")

    if count == 0:
        print("")
    else:
        confirm = input('Do you want to move files to Pictures Folder? (y/n)')
        if confirm in ["Y", "y"]:
            for file in glob.glob(PICTURES1, recursive=False):
                os.rename(file, os.path.join('Pictures', os.path.basename(file)))
                print(f'{file} moved to Pictures folder')
                log.write(f"[{datetime.datetime.now()}]\t{file} moved to Pictures folder\n")
            for file in glob.glob(PICTURES2, recursive=False):
                os.rename(file, os.path.join('Pictures', os.path.basename(file)))
                print(f'{file} moved to Pictures folder')
                log.write(f"[{datetime.datetime.now()}]\t{file} moved to Pictures folder\n")
            print(f'{count} files moved to Pictures folder')
            log.write(f"[{datetime.datetime.now()}]\t{count} moved to Pictures folder\n")
            count_data['PICTURES'] = count
        else:
            print('\n''Operation Aborted''\n')
            log.write(f"[{datetime.datetime.now()}]\tOperation Aborted\n")
            sys.exit()
# Calling function
move_picture_files_to_folder(PICTURES1, PICTURES2, log)
data7 = {'PICTURES': [count]}


"""
Building a data frame from the dictionary.
The data frame will be presented as a chart
This will also automatically save as a .png file.
"""
df = pd.DataFrame({'folder': list(count_data.keys()), 'count': list(count_data.values())})
log.write(f"[{datetime.datetime.now()}]\tData Frame successfully created!\n")

# Create a bar chart
plt.bar(df['folder'], df['count'])
log.write(f"[{datetime.datetime.now()}]\tChart bar created!\n")

# Add labels and title
plt.xlabel('Folder')
plt.ylabel('Count')
plt.title('Number of files moved to each folder')
log.write(f"[{datetime.datetime.now()}]\tChart labels and title created!\n")

# Show/save the chart
plt.savefig('chart.png')
log.write(f"[{datetime.datetime.now()}]\tChart picture saved!\n")
plt.show()
log.write(f"[{datetime.datetime.now()}]\tChart successfully created!\n")

# Closing the log file.
log.close()
# End of script.
# End of script.
