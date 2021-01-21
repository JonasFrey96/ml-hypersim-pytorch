import os
import urls
import argparse
import pathlib
from zipfile import ZipFile

def file_path(string):
  if os.path.isfile(string):
    return string
  else:
    raise NotADirectoryError(string)
  
parser = argparse.ArgumentParser()    
parser.add_argument('--destination', type=file_path, default='cfg/exp/exp.yml',
                    help='Location where the dataset should be stored')

args = parser.parse_args()
dest = args.destination

zip_names = [ os.path.join(dest, u[-14:]) for u in urls.urls_to_download ] 

for u,fi in zip( urls.urls_to_download,zip_names):
  print(f'Download {u}')
  os.system(f'cd {dest} && wget {u} >/dev/null 2>&1')
  ls = []
  with ZipFile(fi, 'r') as zipObj:
    # Get list of files names in zip
    listOfiles = zipObj.namelist()
    # Iterate over the list of file names in given list & print them
    for elem in listOfiles:
        if ((elem.find('final_hdf5') != -1 and elem.find( 'color.hdf5') != -1 ) or
          (elem.find('geometry_hdf5') != -1 and elem.find( 'semantic.hdf5') != -1 )) :
          print(elem)
          ls.append(elem)
  
  for l in ls:
    tar = os.path.join(dest,l)
    tar = os.path.dirname(tar)
    pathlib.Path(tar).mkdir(parents=True, exist_ok=True)
    cmd = f"""unzip -j "{fi}" "{l}" -d "{tar}/" >/dev/null 2>&1"""
    os.system(cmd)
    
  os.system(f'rm {fi}')

