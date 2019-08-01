
#!/usr/bin/env python
#!/usr/bin/python

from pytesseract import image_to_string
from PIL import Image
import pytesseract
import requests
import base64
import json
import cv2
import csv
import numpy as np
from pprint import pprint
from io import StringIO
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import os
from PIL import Image, ImageTk
import io

#------------------------------------------------------------------------------
# use PIL to read data of one image
#------------------------------------------------------------------------------
def get_img_data(f, maxsize = (1200, 850), first = False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format = "PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)
#------------------------------------------------------------------------------

def get_img_data2(f, maxsize = (1200, 850), first = False):

    img = cv2.imread(f)

    # Open output.csv
    with open('output.csv') as csvfile:
        # Read output.csv
        rows = csv.reader(csvfile)
        headers = next(rows)
        for row in rows:
            #print(row)
            split = row[0].split()
            print(split[0]
                 +"("
                 +split[1]#begin(x)
                 +","
                 +split[2]#begin(y)
                 +"), ("
                 +split[3]#end(x)
                 +","
                 +split[4]#end(y)
                 +")"
                 )

            #-------------------------------------------------------------------------------------
            #draw the rectangles on the text
            #-------------------------------------------------------------------------------------
            cv2.rectangle(img, (int(split[1]), int(split[2]) ),(int(split[3]), int(split[4])), (55,255,155),1)
            #put the text on the image
            #cv2.putText(img, split[0], (int(split[1]), int(split[2]) ),(int(split[3]), int(split[4])), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1, cv2.LINE_AA)

    # 顯示圖片
    ##cv2.imshow('My Car Image', img)

    # 按下任意鍵則關閉所有視窗
    ##cv2.waitKey(0)
    ##cv2.destroyAllWindows()

    cv2.imwrite('output.png', img)

    """
    Generate image data using PIL
    """
    output_img = Image.open('output.png')
    output_img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        output_img.save(bio, format = "PNG")
        del output_img
        return bio.getvalue()
    return ImageTk.PhotoImage(output_img)




def main():

    img = sg.PopupGetFile('Image file to select', default_path = '')

    if not img:
        sg.PopupCancel('Canceling')
        raise SystemExit()

    #path of img
    #print(img)

    #------------------------------------------------------------------------------
    #Arabic text image to string
    #print(pytesseract.image_to_string(img, lang='ara'))
    print("==============================================================")
    print("image_to_string")
    print("==============================================================")
    print(pytesseract.image_to_string(img, lang = 'eng'))

    print("==============================================================")
    print("image_to_boxes")
    print("==============================================================")
    print(pytesseract.image_to_boxes(img, lang = 'eng'))

    #print("==============================================================")
    #print("image_to_osd")
    #print("==============================================================")
    #print(pytesseract.image_to_osd(img, lang='osd', config='', nice=0))
    #------------------------------------------------------------------------------

    #Set output.csv can write and read
    output = open(r"output.csv","w")
    #write image_to_boxes data to CSV
    output.write(pytesseract.image_to_boxes(img, lang = 'eng'))
    #Using CSV writer :
    output.close()


    # create the form that also returns keyboard events
    window = sg.Window('Image Browser', return_keyboard_events=True, location=(0, 0), use_default_focus=False)

    # make these 2 elements outside the layout as we want to "update" them later
    # initialize to the first file in the list
    filename = os.path.join(img)
    #print("# name of first file in list")
    #print("filename")
    #print(filename)

    image_elem = sg.Image(data = get_img_data2(filename, first = True))
    #print("image_elem")
    #print(image_elem)

    filename_display_elem = sg.Text(filename, size=(80, 3))
    #print("filename_display_elem")
    #print(filename_display_elem)

    #Define layout, show and read the form
    # +----------+-----------+
    # | +--+ +--+| +--------+|
    # | |  | |  || |        ||
    # | |  | |  || +--------+|
    # | +--+ +--+| +--------+|
    # |          | |        ||
    # |          | +--------+|
    # +----------+-----------+
    col = [[filename_display_elem], [image_elem]]

    col_files = [[sg.ReadButton('Next', size=(8,2)), sg.ReadButton('Prev', size=(8,2)),]]

    layout = [[sg.Column(col_files), sg.Column(col)]]

    window.Layout(layout)          # Shows form on screen

    # loop reading the user input and displaying image, filename
    ##i=0
    while True:
        # read the form
        event, values = window.Read()
        ##print(event, values)

if __name__ == '__main__':
    main()

