import os

flags_dir = os.path.join(os.path.dirname(__file__), 'flags')
output_file_path = os.path.join(os.path.dirname(__file__), 'flag_map.py')

def walk_dir(dir_path):
    flag_map = {}
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.svg'):
                relative_path = os.path.relpath(os.path.join(root, file), flags_dir)
                key = relative_path.replace(os.sep, '/').replace('.svg', '')
                flag_map[key] = relative_path.replace(os.sep, '/')
    return flag_map

flag_map = walk_dir(flags_dir)

with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(f"FLAG_MAP = {repr(flag_map)}\n")
