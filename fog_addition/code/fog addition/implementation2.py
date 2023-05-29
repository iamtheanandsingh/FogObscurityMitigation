from PIL import Image
import copy

img = Image.open('newcar.png')
img2= Image.open('test7_output.jpg').convert('L')
img = img.convert("RGBA")
kopi=img.copy()

pixdata = img.load()
ddata=img2.load()
dup=kopi.load()

width, height = img.size
for y in range(height):
    for x in range(width):
            pixdata[x, y] = (pixdata[x,y][0],pixdata[x,y][1],pixdata[x,y][2],155-max(ddata[x,y]-100,0))
            dup[x,y]=(200,224,224,255)
 
# img.save("oup71.png", "PNG")
Image.alpha_composite(kopi, img).save("oup712.png")

# enhancement in place

'''import cv2

img_m=cv2.imread('/home/a-poor-vagabond/Desktop/MiniProject/fog/results/oup711.png')
#img_m = cv2.cvtColor(img_m, cv2.COLOR_RGB2BGR)
#print(img_m)
median_blur= cv2.GaussianBlur(img_m, (5,5),0)#7,cv2.medianBlur(img_m, 9)#
cv2.imshow('median_blur', median_blur)
cv2.imwrite('img7_res_blur.jpg',median_blur)'''