from random import shuffle

with open('iris.data') as f:
	content=f.readlines()

shuffle(content)

train=open('train.data','wt')
test=open('test.data','wt')

for i in range(0,int(0.9*len(content))):
	content[i]=content[i].rstrip('\n')
	train.write(content[i]+'\n')
train.close()

for i in range(int(0.9*len(content)+1),len(content)):
	content[i]=content[i].rstrip('\n')
	test.write(content[i]+'\n')
test.close()