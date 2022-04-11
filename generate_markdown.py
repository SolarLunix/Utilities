import os
import pathlib
from typing import Dict

def generate_categories():
    category = {}
    for dir, folders, files in os.walk("."):
        for file in files:
            dir_path = pathlib.Path(dir)

            if '.lnk' in file:
                file = file.replace('.lnk', '')

            file_pathlib = pathlib.Path(file)

            file_system = category.setdefault(file_pathlib.stem, ["",[], ""])

            if not file_system[0]:
                file_path = os.path.join(dir_path.absolute(), file)
                if not os.path.islink(file_path):
                    file_system[0] = file_path
                    file_system[2] = file_pathlib.suffix.replace('.', '')
            [file_system[1].append(dir_name) for dir_name in dir.split('\\') if dir_name != '.']
    for key, value in category.items():
        category[key] = [value[0], set(value[1]), value[2]]
    del category['generate_markdown']
    return category


def generate_markdowns(category: Dict, path: str):
    def generate_title(file, title):
        file.write(f"# {title}\n---\n")
        return file
    def generate_tags(file, tags, file_type):
        tag_string = "".join([f"#{tag} " for tag in tags]).strip()
        file.write(tag_string + f" #{file_type}" + "\n")
        return file
    def generate_link(file, title, link):
        link = link.replace(' ', '%20')
        file.write(f"[{title}]({link})")
        return file
    os.makedirs(path, exist_ok=True)
    for title, book_system in category.items():
        with open(os.path.join(path, title + ".md"), 'w') as file:
            generate_title(file, title)
            generate_tags(file, book_system[1], book_system[2])
            generate_link(file, title, book_system[0])

categories = generate_categories()

path = "C:/Users/ryanm/OneDrive/Documents/eBooks/Markdown"
generate_markdowns(categories, path)