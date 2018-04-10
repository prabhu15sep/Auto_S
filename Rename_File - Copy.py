import os
path = "D:\\ppadayac\\PraChin\\db\\db"
files = os.listdir(path)
i = 1

for file in files:
    #os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    new_file = file[24:]
    #print(new_file)
    os.rename(os.path.join(path, file), os.path.join(path, new_file))
    i = i+1