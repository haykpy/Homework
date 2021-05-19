import random



def rand():
	file_ = open("filerand.txt", "w")

	for i in range(20):
		i = random.randint(1,50)
		i = str(i)
		file_.write(i + " ")


ood_list = []

	for j in file_:
		if j % 2 == 0:
			ood_list.append(j)
			print(ood_list)



	file_.close()
rand()

