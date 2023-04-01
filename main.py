import PySimpleGUI as sg
import csv
import os
import sys
import pandas
import subprocess

# 1. Create a showstats window


# csv files
EX_file = 'expensedata.csv'
IN_file = 'incomedata.csv'

# theme
sg.theme('Light blue')

# menu toolbar

menu_def = [['File', ['Open', 'Exit']],
            ['Help', 'About...'], ]

main_layout = [[sg.Menu(menu_def, tearoff=True)],
               [sg.Text('Hello, what you want to do?', size=(50, 1), font=30)],
               [sg.Button('Add expense', border_width=3, pad=((0, 0), (20, 0))),
                sg.Button('Add income', border_width=3, pad=((75, 0), (20, 0)))],
               [sg.Button('Quit', border_width=3, pad=((240, 0), (60, 0)))],
               [sg.Button('Visualization')]
               ]

# windows
main_window = sg.Window("Expense tracker", main_layout, grab_anywhere=False, size=(300, 200))
browse_wn_active = False
win2_active = False
win3_active = False
graph_active = False
i = 0

# loop

while True:
    event, values = main_window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    elif event == 'Exit':
        break
    elif event == 'Open' and not browse_wn_active:
        browse_wn_active = True

        browse_layout = [[sg.Text('What file you want open?')],
                         [sg.InputText(key='-PATH-'), sg.FileBrowse()],
                        [sg.OK(), sg.Cancel()]]

        browse_window = sg.Window('Find files', browse_layout)
        if browse_wn_active:
            event, values = browse_window.read()
            if event != sg.TIMEOUT_KEY:
                print('win2', event)
            if event == 'Cancel' or sg.WIN_CLOSED:
                browse_wn_active = False
                browse_window.close()
            if event == 'OK':
                source = values['-PATH-']
                subprocess.call(["xdg-open", source])
                browse_wn_active = False
                browse_window.close()

    elif event == 'Add expense' and not win2_active:
        win2_active = True

        layout_2 = [[sg.Text('How much money you spend that time?', justification='center'), sg.Text(size=(15, 1))],
                    [sg.Text("Expense"), sg.Input(key='-EXPENSE-', background_color='white',
                                                  text_color='black', pad=(16, 0))],
                    [sg.CalendarButton("Data", format='%d.%m.%y'),
                     sg.Input(key='-DATA-', background_color='white', text_color='black', pad=(16, 0))],
                    [sg.Text("Description"), sg.Input(key='-DESCRIPTION-', background_color='white', text_color='black',
                                                      pad=(0, 0))],
                    [sg.Button('Add expense'), sg.Button('Back', pad=(10, 0))]]

        window2 = sg.Window('Add expense', layout_2, size=(450, 150))
        if win2_active:
            event, values = window2.read()
            if event != sg.TIMEOUT_KEY:
                print('win2', event)
            if event == 'Add expense':
                with open(EX_file, 'a', newline='') as f:
                    fieldnames = ['Expense', 'Data', 'Description']
                    writer_1 = csv.DictWriter(f, fieldnames=fieldnames)
                    writer_1.writerow({'Expense': values['-EXPENSE-'],
                                          'Data': values['-DATA-'],
                                          'Description': values['-DESCRIPTION-']})
                sg.popup('Your expense successfully added')
                win2_active = False
                window2.close()
            if event == 'Back' or sg.WIN_CLOSED:
                win2_active = False
                window2.close()

    elif event == 'Add income' and not win3_active:
        win3_active = True

        layout_3 = [[sg.Text('How much money you earned that time?', justification='center'), sg.Text(size=(15, 1))],
                    [sg.Text("Earned"), sg.Input(key='-EARN-', background_color='white',
                                                 text_color='black', pad=(25, 0))],
                    [sg.CalendarButton("Data", format='%d.%m.%y'),
                     sg.Input(key='-DATA-', background_color='white', text_color='black', pad=(16, 0))],
                    [sg.Text("Description"), sg.Input(key='-DESCRIPTION-', background_color='white', text_color='black',
                                                      pad=(0, 0))],
                    [sg.Button('Add income'), sg.Button('Back', pad=(10, 0))]]

        window3 = sg.Window('Add income', layout_3, size=(450, 150))
        if win3_active:
            event, values = window3.read()
            if event != sg.TIMEOUT_KEY:
                print('win3', event)
            if event == 'Add income':
                with open(IN_file, 'a', newline='') as fi:
                    fieldnames = ['Earned', 'Data', 'Description']
                    writer_2 = csv.DictWriter(fi, fieldnames=fieldnames)
                    writer_2.writerow({'Earned': values['-EARN-'], 'Data': values['-DATA-'],
                                                    'Description': values['-DESCRIPTION-']})
                sg.popup('Your earned money successfully added')
                win3_active = False
                window3.close()
            if event == 'Back' or sg.WIN_CLOSED:
                win3_active = False
                window3.close()

    elif event == 'Visualization':
        graph_active = True
        


main_window.close()

