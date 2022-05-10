import sys
import PySimpleGUI as sg
from PIL import Image
import pygame
import pygame.camera
import io
import time

pygame.init()
pygame.camera.init()
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0],(720,480))

engrenagem = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAADsAAAA7AF5KHG9AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAA9tJREFUWIW113vM1mMYB/BPpd6ISiTN20pvrJpSijHLHw1RGLZMlsbmbP0VMrWVkeY0mUOMsLGZ01ZYOogctuaUKBE15/MhK5Ux8sf3fvY+Pb1vJ0/f7dnz/K77cF2/+/5e3+t6+H8Yj9+wDr+jYXc3aLsHTi/ES+iMAbgbTdiIXhiJBThoD/beKcZhNaZhExZjcBmbiC+wFtfj3b0RxGpcUn53a2F8H3Qp38twZb0D6Ic/0KE8D8GjWIip2LfYL8YitKmX47Y4S47+xWI7Qcg3FsfgVrxW5h6Gr8rY0fUIoAk/4UEMLbYFQrhqPIvTy++r8QyW1COAfninxrYGB9bYphTHFRyFV3a08a6m4V8YWIIYXWzvYUzNXqOF/TAHT5W1dUEjzsbL5bmPpNxNmCDa8EAZGyQZ01f0olXsjhB9g/VyrA2S88cJNwbgHlxR5jZJtvyIDbvhY6dYi8skvU7VnHYV9NJM0qWYVE/nMBxfY67c9fc4t4zNkdT7XLJhnma9qCuGYbqcwiTMkmz4tjg8QjShAy7A0+VzZEub7QoHHhPBWYdP8EsJYKtcyZmaT+Nv4cohIlTnl3U9cJrUiGt35rArzqh6Xi5K17c4Gl7sTTixZm07Eah5UqzelmwZVwL8EJ/ZATe6Sq7/jBtEetfjgDK+qGx+ngjRlxhVtb4jVoge7C9FaQh6o72Q9mHMaMl5l+J8CnriDdxS3ryCBqkJC8rbD5R0PLmMD8C9ckUH432R4tW4r8xZictxeG0Ag4XhvVuKrhV0LA5mCJ+2SGVsxB2YXOa1Ky80QgrUWyJc2+EckdhqDMNdUojG25a4U6XgtClOfhUVJKl4UtXcO6Wb2k+UcyHbZ0Fv6XIqmIiH8EFZMEp4UMnvueguGfGv8OM5qZLz5TobcbzI+Ku4TZqaF6odPyLN5WZhN7nflSXiatwu5Kzgdc0p2lk0YFY5leuElEvl+Alxa8u4JaLrnapsU7Scs434qAX7CinbG+XaLkL/MtZWKudIzJSTQtKkgg2SuxU0aLmQbNF6+71Zjnq+6MeNwpuxooQ95GROqV34PFZJI9mz2EbI8dbyZKIQsoIn5Qr+1NwF9ynrZksqfif86VI+26G96PlMXFNlny1sPlY0frIoWfcqR6tEKw5tYd9uch1DbXvarWK0KFw1LpZmc7n8Calux6eVIOuC/vhBisuuoqvo/YQ9dVp9v5uEwf+IqEyXClbb2w/C/SK7neROt+5pALVokjteLER7Ap9KYYHHhVQ3S/OxBpfWy3l1EFdVPX+smWBvam4sxkjDsdexTP56V5SysZ6b/wev2NhqMojr9gAAAABJRU5ErkJggg=='

options = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAE6SURBVFiF7ZZRTsJAFEUPaoxLIqAuRhpYECGuQMFl6Bos6DfwBRvoR8GPdmKZvLF90ychgZu8j07evXOnmTe5cCLoAENgAeTAXqgcmANJ2W+qMQoQQpUIBlppfCnJqWAgSsP9hhy4EkRD2AHX3lqUhjOwVxAd/HsQpaFx/C+4GDgZAzslT+qP0nAGvpXkhbDWSiNB94g8CYKtNDqlQMrf73gKDAInstC44IxhEUiqeABmwBrIgBUwBe5DBItAAnADPNdwJ2XfASwCCQ02r5o4QOi3hyoXNn9UavSrZA3RlY83Jf/V2sBayV/B722WBOvgT0IG3Cr4GXBnmQe2yv4N2AaSD2X/e/XDYgq6FCEjagrmSgOfgVNNGvLHPtEikEDxwtWZGCO8hNZhok8x50uK274EXoBeA+5x8QPoh1aG0X2+XgAAAABJRU5ErkJggg=='

camera = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAGFSURBVFiF7ZY9TsNAEIW/WCgNSSzRU0NHSMmPRIuICwpuE6UJgtBwCFoEXIAk16AmPxKhI/Sm2FlwLDueRY6FhJ80srXzdubtW9trKFHCDQMgzIjndTXfVTS3saMt6jkIOFkT92+gCtwAM/Q2/zamQF96fqNfQON4XEcFFLHyeMyiAlwmvgEdoAlsSuzL2NyxVqqAA+AwYfweqJOOBvCQh4Aj4DiheUX4ATACPiWGQFtynoOIVAFJttuVX8WcqgPnwAtwKRwf3XaoBXQiK487ZbEFjCNOdPMUsCe8UUJuDJxK/gJzXoB5MHMTUBPeIiX/KvkG8CH3dY2ADXSoZOS3MdsR5WXNWUKW0qbwhgqu3YKWgqs+DQO53iq4lhOsZMWQpXSO2V8wr1oaryccH3hX1FULCDEfF+tYG2P1QmIAnEnOA56UNZ0EWBH+Cid94NGhnrOAEGNtF/OQ1TCvW0vGNLYnCpg6TswjJvCzp3crbF0XlnpWMX8oRTgxwRxoS79kJf4vvgB4RbwJ1cGAUAAAAABJRU5ErkJggg=='

def login():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Token:        '), sg.Input(key='token', size=(30, 1))],
        [sg.Text('Username:  '), sg.Input(key='usuario', size=(30, 1))],
        [sg.Text('Password:  '), sg.Input(key='senha', password_char='*', size=(30, 1))],
        [sg.Checkbox('Salvar o login?', key='salva_login')],
        [sg.Button('Entrar')]
    ]

    janela = sg.Window('Login', layout, icon='imgs\\logo_ico_bls.ico')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Entrar':
            #PROCURAR  O LOGIN NO XML
            janela.close()
            return True


def interface_webcam():
    sg.ChangeLookAndFeel('DarkBlue')

    # define the window layout
    layout = [[sg.Text('Webcam', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image', p=(150,0))],
              [sg.Text('Usuário:\nNome do usuário:'),
               sg.Button('', pad=((420, 8), 3), button_color=sg.TRANSPARENT_BUTTON, image_data=engrenagem,
                         image_size=(60, 35), key='-resolucao-'),
               sg.Button('', button_color=sg.TRANSPARENT_BUTTON, image_data=options, image_size=(60, 35), key='-imagens_salvas-'),
               sg.Button('', button_color=sg.TRANSPARENT_BUTTON, image_data=camera, image_size=(60, 35), key='-camera-')]]

    # create the window and show it without the plot
    window = sg.Window('Tela de visualização da Webcam',
                       location=(800, 400))
    window.Layout(layout).Finalize()

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #

    #cap = cv.VideoCapture(0)
    
    cam.start()
    time.sleep(2)  
    while True:
        bio = io.BytesIO()
        img = cam.get_image()
        pil_image_string = pygame.image.tostring(img, "RGBA", False)
        final_img = Image.frombytes("RGBA",(720,480), pil_image_string)
        final_img.save(bio, format='PNG')
        imgbytes = bio.getvalue()
        window['image'].Update(data=imgbytes)
        window.refresh()
        
        
        #button, values = window.read()
        
        
        #if button == sg.WINDOW_CLOSED:
        #    sys.exit(0)
        #if button == '-camera-':
        #   pass #AçÂO
        #if button == '-imagens_salvas-':
        #   pass


        # img = Image.fromarray(gray)  # create PIL image from frame
        # bio = io.BytesIO()  # a binary memory resident stream
        # img.save(bio, format='PNG')  # save image as png to it
        # imgbytes = bio.getvalue()  # this can be used by OpenCV hopefully
        
    


if __name__ == '__main__':
    result = login()
    if result is True:
        interface_webcam()

