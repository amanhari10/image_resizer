#First install cv2 in device by typing "pip install cv2" in your terminal.

import cv2

src = cv2.imread("python projects\horror.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)
#percent by which the image is resized
scale_image = int(input("Enter The Scale of image you want to resize: "))

#calculate the % of image 
new_width = int(src.shape[1] * scale_image / 100)
new_height = int(src.shape[0] * scale_image / 100)

#resize image

output = cv2.resize(src, (new_width, new_height))
cv2.imwrite('newimage.png', output)

cv2.waitKey(0)
