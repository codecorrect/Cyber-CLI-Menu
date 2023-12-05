from cyber_menu_template import *
from file_functions import *

working_file = ""

def createfile():
    global working_file
    clear_screen()
    formatted_header("Create New File")
    filename = formatted_prompt("Enter new file name")

    if not filename.strip() or " " in filename: #tests for spaces
        formatted_msg(f"Filename can't have spaces. Try again!", True)
    else:
        file_type = "csv"

        status = new_file(filename, file_type) #creates a csv file

        if status == 1:
            working_file = filename + "." + file_type
            formatted_msg(f"{filename}.csv created successfully!", False)
        elif status == 0:
            formatted_msg(f"{filename}.csv already exists!", True)
        else:
            formatted_msg(f"An error occurred.", True)

    formatted_prompt("Press Enter to continue")

def openfile():
    global working_file
    clear_screen()
    formatted_header("Open File")
    formatted_msg("Select a file:", False)
    files = list_files()
    formatted_list(files)

    filenum = formatted_prompt("Enter file number")

    try:
        selected_item = int(filenum) - 1
        if 0 <= selected_item < len(files):
            working_file = files[selected_item]
            formatted_msg("Using file: " + working_file, False)
        else:
            formatted_msg(f"Invalid file number. Try again!", True)
    except ValueError:
        formatted_msg(f"Enter a valid number. Try again!", True)

    if create_backup(working_file):
        formatted_msg(f"Backup created: {working_file}.bak", False)
    else:
        formatted_msg(f"Backup failed", True)

    formatted_prompt("Press Enter to continue")

def wifiscan():
    global working_file
    clear_screen()
    formatted_header("Wifi Scan")

    if file_exists(working_file):
        formatted_msg(f"Current working file: {working_file}", False)
        formatted_msg(f"**This page runs wifi scanner on everything", False)
        formatted_msg(f"**and then saves BSSID & ESSID to the global data variable, or maybe saves it to the file with just the local data variable", False)
    else:
        formatted_msg(f"File error. Go back to create or open file.", True)

    formatted_prompt("Press Enter to continue")

def savefile():
    formatted_msg(f"Changes to {working_file} saved.", False)

    if del_file(working_file + ".bak"):
        formatted_msg(f"Removed backup file {working_file + ".bak"}.", False)
    else:
        formatted_msg(f"Removing backup failed.", True)

    formatted_prompt("Press Enter to continue")

def viewfile():
    pass

def fileoptions():
    main_menu_options = {
        "New File": createfile,
        "Open File": openfile,
        "View File": viewfile
    }

    create_menu("File Options", main_menu_options, False)

def deauth():
    global working_file
    clear_screen()
    formatted_header("Deauth")

    if file_exists(working_file):
        formatted_msg(f"Current working file: {working_file}", False)
        formatted_msg(f"**This page runs deauth on each BSSID in file and saves handshake to file", False)
    else:
        formatted_msg(f"File error. Go back to create or open file.", True)

    formatted_prompt("Press Enter to continue")

def crack():
    pass

def test_func():
    def pass_func():
        pass
    main_menu_options = {
        "Option 1": pass_func,
        "Option 2": pass_func,
        "Option 3": pass_func,
        "Option 4": pass_func
    }

    create_menu("Main Menu", main_menu_options, False)

#MAIN
main_menu_options = {
    #"Create New File": createfile,
    #"Open File": openfile,
    "File Options": fileoptions,
    "Wifi Scan": wifiscan,
    "Deauth": deauth,
    "Crack": crack,
    #"Save & Exit": savefile
    #"Test": test_func
}

create_menu("Main Menu", main_menu_options, True)


