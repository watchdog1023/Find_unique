import hashlib
import sys

out = sys.argv[2] #File name
inputs = sys.argv[1] #File name

completed_lines_hash = set()

output_file = open(out,"w")

for line in open(inputs,"r"):
	hashVaule = hashlib.md5(line.rstrip().encode("utf-8")).hexdigest()
	if hashVaule not in completed_lines_hash:
		output_file.write(line)
		completed_lines_hash.add(hashVaule)

output_file.close()
