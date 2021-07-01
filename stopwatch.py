import PySimpleGUI as sg

def StopWatch():


    img_play = 'play.png'
    img_stop = 'stop.png'
    img_reset = 'reset.png'
    img_qt = 'qt.png'

    sg.theme_button_color((sg.theme_background_color(), sg.theme_background_color()))
    sg.theme_border_width(0)

    sg.theme('DarkBrown1')

    layout = [  [sg.T(' ' * 2),sg.Text('Stopwatch', size=(19, 2), justification='center')],
                [sg.T(' ' * 10),sg.Text('00:00:00', size=(7, 2), font=("Helvetica", 40) ,justification='center', key='-OUTPUT-')],
                [sg.T(' ' * 10),sg.Button(image_filename=img_reset, image_size=(40, 40), image_subsample=2, key='-RESET-'),sg.T(' ' * 2), sg.Button(image_filename=img_play, image_size=(40, 40), focus=True, image_subsample=2, key='-PLAY/STOP-'), sg.T(' ' * 2),sg.Button(image_filename=img_qt, image_size=(40, 40), image_subsample=2, key='-Quit-')]]

    window = sg.Window('Stopwatch Timer', layout, default_element_size=(20, 1), font=("Helvetica", 25))

    timer_running, counter = False, 0

    while True:                                 # Event Loop
        event, values = window.read(timeout=10) # Please try and use as high of a timeout value as you can
        if event in (sg.WIN_CLOSED,'-Quit-'):             # if user closed the window using X or clicked Quit button
            break
        elif event == '-PLAY/STOP-':
            timer_running = not timer_running
            if timer_running:
                window['-PLAY/STOP-'].update(image_filename=img_stop, image_size=(40, 40), image_subsample=2)
            if not timer_running:
                window['-PLAY/STOP-'].update(image_filename=img_play, image_size=(40, 40), image_subsample=2)
        elif event == '-RESET-':
            if not timer_running:
                window['-OUTPUT-'].update('00:00:00')
                counter *= 0
                window['-PLAY/STOP-'].update(image_filename=img_play, image_size=(40, 40), image_subsample=2)
        if timer_running:
            window['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
            counter += 1
    window.close()

StopWatch()