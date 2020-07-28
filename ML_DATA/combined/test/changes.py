import glob,os,shutil
counter =1
files = sorted(glob.iglob(os.path.join("train/","*.txt")))

for file in files:
	if os.path.isfile(file):
		if os.stat(file).st_size != 0 :
			
			
			f = open(file,"r")
			content = f.readline()
			new_content = "1" + content[1:]
			f = open(file,"w")
			f.write(new_content)
			
	
