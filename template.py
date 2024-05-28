import os

file_paths = [
    "./Demo.ipynb",
    "./meta.yaml",
    "./README.md",
    "./requirements.txt",
    "./template.py",
    "./config\config.yaml",
    "./data\diabetes_dataset.csv",
    "./documentation\project_documentation.docx",
    "./models\model_description.txt",
    "./scripts\Demo.ipynb",
    "./scripts\main.py",
    "./scripts\code\__init__.py",
    "./scripts\code\config\__init__.py",
    "./scripts\code\logging\__init__.py",
    "./scripts\code\pipelines\data_gathering.py",
    "./scripts\code\pipelines\data_preparation.py",
    "./scripts\code\pipelines\model_training.py",
    "./scripts\code\pipelines\__init__.py",
    "./scripts\code\utilities\common_utils.py",
    "./scripts\code\utilities\__init__.py",
    "./scripts\logs\__init__.py"
]

for path in file_paths:
    if not os.path.isfile(path):
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, "w") as file:
            file.write("")
        print(f"File created: {path}")

print("#"*100)

import os
base_path = ""./"

def show_contents(base_path, depth):
    items = os.listdir(base_path)
    items = [x for x in items if "." not in x] + [x for x in items if "." in x]
    for i in range(len(items)):
        item = items[i]
        if "." in item:
            if item != items[-1]:
                print("   │"*depth + "   ├── " + item)
            else:
                print("   │"*depth + "   └── " + item)
        else:
            print("   │"*depth + "   ├── " + item + "/")
            depth+=1
            show_contents(os.path.join(base_path, item), depth)
            depth-=1
print(".\n└──")
show_contents(base_path, 0)