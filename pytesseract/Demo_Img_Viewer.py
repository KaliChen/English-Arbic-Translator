#!/usr/bin/env python
#!/usr/bin/python

import requests
import base64
import json
import cv2
import numpy as np
from pprint import pprint

import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import os
from PIL import Image, ImageTk
import io





imgfile = sg.PopupGetFile('Image file to select', default_path = '')

if not imgfile:
    sg.PopupCancel('Canceling')
    raise SystemExit()

print(imgfile)

# PIL supported image types
img_types = (".png", ".jpg", "jpeg", ".tiff", ".bmp", ".ppm")
#print("# PIL supported image types")
#print(img_types)



#------------------------------------------------------------------------------
# use PIL to read data of one image
#------------------------------------------------------------------------------
def get_img_data(f, maxsize = (1200, 850), first = False):

    #------------------------------------------------------------------------------
    #Call openalpr (Cloud)
    #-------------------------------------------------------------------------------
    SECRET_KEY = 'sk_2902aacead0248cd2f0d8400'
    ###key = open('Key.txt', 'r')
    ###    SECRET_KEY = key.readlines()

    with open(f, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())
    img = cv2.imread(f)
    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
    r = requests.post(url, data = img_base64)
    #-------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------
    #output to file: output.json
    #-------------------------------------------------------------------------------
    jsonfile = "output.json"
    with open(jsonfile, 'w') as fp:
        json.dump(r.json(), fp)

    with open('output.json') as data_file:
        data = json.loads(data_file.read())
    #-------------------------------------------------------------------------------

    #-------------------------------------------------------------------------------------
    #draw the rectangle on the license plate
    #-------------------------------------------------------------------------------------
    cv2.rectangle(img,
    (data['results'][0]['coordinates'][0]['x'], data['results'][0]['coordinates'][0]['y']),
    (data['results'][0]['coordinates'][2]['x'], data['results'][0]['coordinates'][2]['y']),
    (55,255,155),5)
    #--------------------------------------------------------------------------------------

    #--------------------------------------------------------------------------------------
    #draw the rectangle on the car
    #--------------------------------------------------------------------------------------
    cv2.rectangle(img,
                  (data['results'][0]['vehicle_region']['x'],data['results'][0]['vehicle_region']['y']),
                  (data['results'][0]['vehicle_region']['x']+ data['results'][0]['vehicle_region']['width'], 
                   data['results'][0]['vehicle_region']['y']+data['results'][0]['vehicle_region']['height']),
                  (255,55,255),
                  5)
    #--------------------------------------------------------------------------------------

    # 顯示圖片
    ##cv2.imshow('My Car Image', img)

    # 按下任意鍵則關閉所有視窗
    ##cv2.waitKey(0)
    ##cv2.destroyAllWindows()

    cv2.imwrite('output.png', img)

    """Generate image data using PIL
    """
    output_img = Image.open('output.png')
    output_img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        output_img.save(bio, format = "PNG")
        del output_img
        return bio.getvalue()
    return ImageTk.PhotoImage(output_img)





# create the form that also returns keyboard events
window = sg.Window('Image Browser', return_keyboard_events=True, location=(0, 0), use_default_focus=False)

# make these 2 elements outside the layout as we want to "update" them later
# initialize to the first file in the list
filename = os.path.join(imgfile)
##print("# name of first file in list")
##print("filename")
##print(filename)

image_elem = sg.Image(data = get_img_data(filename, first = True))
##print("image_elem")
##print(image_elem)

filename_display_elem = sg.Text(filename, size=(80, 3))
##print("filename_display_elem")
##print(filename_display_elem)

other_info =  sg.Text(filename, size=(30, 30))

# define layout, show and read the form
col = [[filename_display_elem],
          [image_elem]]

col_text = [[other_info]]

layout = [[sg.Column(col_text), sg.Column(col)]]

window.Layout(layout)          # Shows form on screen

# loop reading the user input and displaying image, filename
##i=0
while True:
    # read the form
    event, values = window.Read()
    ##print(event, values)


    

