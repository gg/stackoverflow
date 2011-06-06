import os, fnmatch

def locate(pattern, root=os.curdir):
    #ignore directories- uncomment to make ignore work
    #ignored = ["0201", "0306"]
  for path, dirs, files in os.walk(os.path.abspath(root)):
 #for dir in ignored:                  # if dir in dirs:                        #dirs.remove(dir)
    for filename in fnmatch.filter(files, pattern):
       yield os.path.join(path, filename)



for filename in locate("*_passive.sss"):
   #found the files that i want to rename, but os.rename() refuses to overwrite !!
    newfilename=filename.rstrip("_passive.sss") + ".sss"
    os.rename(filename,newfilename)
