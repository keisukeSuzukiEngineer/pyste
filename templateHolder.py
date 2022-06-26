import os, glob
from sqlBaker import SqlBaker

__sql_lark_path = "./lark/sqlTemplate.lark"

__template_holder = {}

def get_templates(base_folder_path):
    
    base_folder_path = os.path.abspath(base_folder_path)
    
    if base_folder_path in __template_holder.keys():
        return __template_holder[base_folder_path]
    
    templateHolder = TemplateHolder()
    
    __set_templates(templateHolder, __sql_lark_path, base_folder_path)
    
    # setattr(c, "key", "value")
    
    
    __template_holder[base_folder_path] = templateHolder
    
    return templateHolder
    
def __set_templates(templateHolder, __sql_lark_path, base_path):
    
    for path in [path for path in glob.glob(f"{base_path}/*") if os.path.isdir(path)]:
        folder_name = path.split("\\")[-1]
        
        templateFolder = TemplateFolder()
        __set_templates(templateFolder, __sql_lark_path, path)
        
        setattr(templateHolder, folder_name, templateFolder)
        
    for path in [path for path in glob.glob(f"{base_path}/*") if os.path.isfile(path)]:
        file_name = path.split("\\")[-1].split(".")[0]
        
        setattr(templateHolder, file_name, SqlBaker(__sql_lark_path, path))
    
    
    
class TemplateHolder:
    pass
    
class TemplateFolder:
    pass