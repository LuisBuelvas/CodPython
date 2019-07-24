import os
path = "/home/dev06/Descargas/prueba nombre/id/"
dirs = os.listdir( path )
i="4"
for fn in dirs:
    src = path + fn
    dst = path + fn[:-8] + str(i) + fn[-7:] 
    print(dst)

    if fn[-8] == "6":
       os.rename(src, dst)
        #print("objeto encontrado")
