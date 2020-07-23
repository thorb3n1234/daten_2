import glob,os,shutil
counter =1
files = sorted(glob.iglob(os.path.join("../data/data/train/","*.txt")))

for file in files:
	if os.path.isfile(file):
		if os.stat(file).st_size != 0 and str(file) != "test/classes.txt":
			counter = counter + 1 
			f = open(file,"r")
			content = f.readline()
			if content[-1] == " "
				content[-1] =="\n"
			f = open(file,"w")
			f.write(content)
print(str(counter))
