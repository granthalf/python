import pefile
from pathlib import Path

def list_icons(exe_path):
    pe = pefile.PE(exe_path)
    icons = []

    if hasattr(pe, 'DIRECTORY_ENTRY_RESOURCE'):
        for resource_type in pe.DIRECTORY_ENTRY_RESOURCE.entries:
            if resource_type.name is not None:
                name = str(resource_type.name)
            else:
                name = str(resource_type.struct.Id)

            if name == "RT_ICON" or name == "3":  # 3 = RT_ICON
                for entry in resource_type.directory.entries:
                    for lang in entry.directory.entries:
                        data_rva = lang.data.struct.OffsetToData
                        size = lang.data.struct.Size
                        icons.append(size)

    return icons
    
fileshere = False
my_file_local_name="./archive.exe"
my_file_dist_name="./dist/archive.exe"

my_file_local = Path(my_file_local_name)
if my_file_local.is_file():
    fileshere = True
    
my_file_dist = Path(my_file_dist_name)
if my_file_dist.is_file():
    fileshere = True

if not fileshere:
       print("No EXE found.")
    
if fileshere:
    try:
        icons = list_icons(my_file_dist_name)
        print("ICON Sizes found in dist exe :", icons)
        
        
    except Exception as e:
        icons = list_icons(my_file_local_name)
        print("ICON Sizes found in local exe :", icons)
