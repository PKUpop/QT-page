import cv2


#for i in range(11):
#	img_name = "0-%d.png"%(i+1)
for i in range(6):
	img_name = "intro-%d.jpg"%(i+1)
	img = cv2.imread(img_name)
	hgt, wdt, _ = img.shape
	print(hgt, wdt)
