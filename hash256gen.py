import hashlib
import glob

filenames = glob.glob("*.csv")

for filename in filenames:
	with open(filename, 'rb') as afile:
		hash = afile.read()
		gethash = hashlib.sha256(hash).hexdigest()
		f = open(filename+".sha256", "w", newline='\n')
		f.write(gethash+ "  " +filename+'\n')
