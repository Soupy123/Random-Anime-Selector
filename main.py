# imports
import random
import PySimpleGUI as sg

#array of the top 25 animes
animes = ['Fullmetal Alchemist: Brotherhood', 'One Punch Man', 'Death Note', 'Cowboy Bebop', 'Attack on Titan', 'Steins;gate', 'Monster', 'Hunter x Hunter', 'Dragon Ball Z', 'Clannad: After Story', 'Berserk', 'Code Geass', 'Fullmetal Alchemist',
          'Ghost in the Shell: Stand Alone Complex', 'Erased', 'Neon Genesis Evangelion', 'Dragon Ball', 'Naruto Shippuden', 'Anohana: The Flower We Saw That Day', 'FLCL', 'Naruto', 'Elfen Lied', 'Clannad', 'Akame ga Kill!', 'Another']

#put a random choice of those animes into a variable
results = random.choice(animes)

#set up GUI

sg.theme('DarkGrey5')

layout = [  [sg.Text('Select Choose Below to Randomly Select an Anime')],
            [sg.Button('Choose'), sg.Button('Close Window')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close Window': # if user closes window or clicks cancel
        break
    sg.popup(random.choice(animes))

window.close()
