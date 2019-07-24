# #!/usr/bin/python3
# import os, sys

# # Open a file
# path = "/home/dev06/Descargas/prueba nombre/"
# dirs = os.listdir( path )

# # This would print all the files and director0ies
# for file in dirs:
#    print (file)



import os
path = "/home/dev06/Descargas/prueba nombre/"
dirs = os.listdir( path )

for fn in dirs:
    src = path + fn
    dst = path + fn[3:] 
    if fn.startswith("ok_"):
        os.rename(src, dst)
print("Objeto Renombrado")
       
# for filename in dirs:
#      if filename.startswith("ok-"):
#          os.rename(filename, filename[3:])