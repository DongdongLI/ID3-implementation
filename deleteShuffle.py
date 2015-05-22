import os
try:
	os.remove("train.data")
	os.remove("test.data")
except OSError:
	pass