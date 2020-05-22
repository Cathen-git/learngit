import os

path = 'C:\PycharmProjects\scripts_cai\example_data\\rename'

for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path,'paml'+file[-5:]))





