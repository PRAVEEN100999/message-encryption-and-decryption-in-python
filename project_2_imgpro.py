from PIL import Image
image = Image.open("F:/om/a.jpg")
print(image)
image.show()

#image resize
width , height = image.size
area=  (int(width/4),int(height/4))
img = image.resize(area)
img.save("F:/om/resizeimg.jpg")
print(img)
img.show()



# # cropped image
# width,height = image.size
# area = (0,0,width/2,height/2)
# img= image.crop(area)
# img.save("F:/om/croppedimg.jpg")
# img.show()

#image transpose
# transpose_img  = image.transpose(Image.FLIP_LEFT_RIGHT)
# transpose_img.save("F:/om/b.jpg")
# transpose_img.show()
