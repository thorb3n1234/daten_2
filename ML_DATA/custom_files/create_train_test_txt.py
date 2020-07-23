import os
import sys

#CONNECTION
a = open("train.txt", "w")
for file in os.listdir("../combined/train/"):
	if file.endswith('.jpg'):
		a.write("../daten_2/ML_DATA/combined/train/"+ str(file) + os.linesep)

a.close()


b = open("test.txt", "w")
for file in os.listdir("../combined/test/"):
	if file.endswith('.jpg'):
		b.write("../daten_2/ML_DATA/combined/test/"+ str(file) + os.linesep)
b.close()




