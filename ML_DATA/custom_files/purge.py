import glob,os,shutil
counter =1
files = sorted(glob.iglob(os.path.join("../data/data/train/","*.txt")))

for file in files:
	if os.path.isfile(file):
		if os.stat(file).st_size == 0 :
			
			parts = file.split("/")
			print(parts)
			txtfile = parts[4]
			newimgfile = txtfile.split(".")
			y = ""
			for x in newimgfile[:-1]:
				y=y+ x + "."
			y = y[:-1] + ".jpg"
			print(y)
			print(txtfile)
			#now remove file !
			os.remove("../data/data/train/" + y)
			os.remove("../data/data/train/" + txtfile)
			
	
