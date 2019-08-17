import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image

img = np.zeros((800, 800, 3), np.uint8)

# 將背景設定為大紅色
img[:] = (0, 0, 255)

# 文字
text = 'اللغة العربية رائعة'

# 指定 TTF 字體檔
fontPath1 = "./A_Nefel_Sereke.ttf"
fontPath2 = "./DejaVuSans.ttf"

# 載入字體
font1 = ImageFont.truetype(fontPath1, 50)
font2 = ImageFont.truetype(fontPath2, 50)
# 將 NumPy 陣列轉為 PIL 影像
imgPil = Image.fromarray(img)

# 在圖片上加入文字
draw = ImageDraw.Draw(imgPil)
draw.text((100, 100),  text, font = font1, fill = (0, 0, 0))
draw.text((100, 150),  text, font = font2, fill = (0, 0, 0))
# 將 PIL 影像轉回 NumPy 陣列
img = np.array(imgPil)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
