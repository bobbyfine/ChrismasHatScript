from PIL import Image
import face_recognition

img_path = input("image path:")

image = face_recognition.load_image_file(img_path)

face_locations = face_recognition.face_locations(image)

print("Found {} face(s) in this photograph.".format(len(face_locations)))
print(face_locations)

human_img = Image.open(img_path)

human_img = human_img.convert("RGBA")

hat_img = Image.open("./Hat/Hat.png")
hat_img = hat_img.convert("RGBA")

for face_location in face_locations:
	top, right, bottom, left = face_location
	top -= 10
	print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
	head_h = bottom-top
	head_l = right-left
	hat_img = hat_img.resize( (head_l,head_h) )
	hat_region = hat_img
	human_region = ( left, top-head_h, right, top )
	human_img.paste(hat_region, human_region,mask=hat_img)
human_img.show()
