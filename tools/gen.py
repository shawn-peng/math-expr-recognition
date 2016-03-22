import os

i = 0
t = []
for folder in os.listdir(os.getcwd() + "/data/222"):
	if folder[0] != '.':
		t.append('"%s": %s'%(folder, str(i)))
		
print "{" + ",".join(t) + "}"
