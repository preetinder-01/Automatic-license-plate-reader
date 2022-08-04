import cv2


from PlateExtraction import extraction
from OpticalCharacterRecognition import ocr
from OpticalCharacterRecognition import check_if_string_in_file

image = cv2.imread('./pictures/001.jpg')
plate = extraction(image)
cv2.imshow('frame',plate)
cv2.waitKey(0)
text = ocr(plate)
text = ''.join(e for e in text if e.isalnum())
print(text, end=" ")
# if check_if_string_in_file('Database.txt', text) and text != "":
#     print('Registered')
# else:
#     print("Not Registered")