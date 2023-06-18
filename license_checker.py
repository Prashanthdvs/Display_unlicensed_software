import tkinter as tk
import subprocess
import webbrowser

def scan_installed_software():
# Use system APIs or command-line tools to scan for installed software
    data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    result=str(data).strip()
    software_lists=[]
    try:
        for i in range(len(result)):
            software_lists.append((result.split('\\r\\r\\n')[6:][i-1]).strip()) # Exclude header and empty lines
    except IndexError:
        pass

    software_list=[x for x in software_lists if x!="'" and x!='']
    print(software_list)
    return software_list

def verify_license(software_list):
    # list of licensed software for reference
    licensed_software = ['Python 3.10.10 Test Suite (64-bit symbols)', 'Microsoft DCF MUI (English) 2016', 'Microsoft Office Professional Plus 2016', 'Microsoft OneNote MUI (English) 2016', 'Microsoft Office 32-bit Components 2016', 'Microsoft Office Shared 32-bit MUI (English) 2016', 'Microsoft Office OSM MUI (English) 2016', 'Microsoft Office OSM UX MUI (English) 2016', 'Microsoft InfoPath MUI (English) 2016', 'Microsoft Access MUI (English) 2016', 'Microsoft Office Shared Setup Metadata MUI (English) 2016', 'Microsoft Excel MUI (English) 2016', 'Microsoft Access Setup Metadata MUI (English) 2016', 'Microsoft PowerPoint MUI (English) 2016', 'Microsoft Publisher MUI (English) 2016', 'Microsoft Outlook MUI (English) 2016', 'Microsoft Groove MUI (English) 2016', 'Microsoft Word MUI (English) 2016', 'Microsoft Skype for Business MUI (English) 2016', 'Microsoft Office Proofing (English) 2016', 'Microsoft Office Shared MUI (English) 2016', 'Microsoft Office Proofing Tools 2016 - English', 'Herramientas de correcci\\xa2n de Microsoft Office 2016: espa\\xa4ol', 'Outils de v\\x82rification linguistique 2016 de Microsoft Office\\xff- Fran\\x87ais', 'Microsoft Visual C++ 2022 X64 Minimum Runtime - 14.32.31332'] # Example list of licensed software

    # Compare the list of installed software with the licensed software database
    unlicensed_software = [software for software in software_list if software not in licensed_software]

    return unlicensed_software

def start_button_clicked():
    # Scan for installed software
    installed_software = scan_installed_software()

    # Verify the license for installed software
    unlicensed_software = verify_license(installed_software)

    # Display the list of unlicensed software
    display_unlicensed_software(unlicensed_software)
   

def display_unlicensed_software(unlicensed_software):
    # Clear previous results
    display_area.delete(1.0, tk.END)
    # Display the list of unlicensed software in the display area
    if unlicensed_software:
        for software in unlicensed_software:
            display_area.insert("end", software +'\t\n')
            button = tk.Button(display_area, text="Apply License", padx=4, pady=4,command =lambda:webbrowser.open("https://tools.hcl.com/tool/user/home.aspx"))
            display_area.window_create("end-2c", window=button)
    else:
        display_area.insert(tk.END, 'No unlicensed software found.\n')

# Create the main window
window = tk.Tk()

# Create UI elements
start_button = tk.Button(window, text='Start', command=start_button_clicked)
display_area = tk.Text(window, height=40, width=70)

# Place UI elements in the window
start_button.pack()
display_area.pack()

# Start the main event loop
window.mainloop()