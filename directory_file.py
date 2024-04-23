import os

folder = '/Users/prapande12/Desktop'

entries = os.scandir(folder)

for entry in entries :
    if os.path.isfile(entry) :
        print("File:", entry.name)
    elif os.path.isdir(entry) :
        print("Directory:", entry.name)

destination_folder = '/Users/prapande12/Desktop/NewPython'

location = os.path.join(folder, "test.html")
destination_location = os.path.join(destination_folder, "test.html")

os.rename(location, destination_location) 