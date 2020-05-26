import os

def create_folders():
	for i in range(1,10):
		folder_name = f'dir_{i}'
		os.mkdir(folder_name)

def del_folders():
	for i in range(1,10):
		folder_name = f'dir_{i}'
		os.rmdir(folder_name)


create_folders()
del_folders() 

