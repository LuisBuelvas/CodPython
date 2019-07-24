
import os
import logging
path = "/home/dev06/Descargas/prueba nombre/ok"
dirs = os.listdir( path )

for fn in dirs:
    src = path + fn
    dst = path + fn[:-8] +fn[-7:]
    print(dst)
    os.rename(src, dst)
    
#     if fn.endswith("-407.cam2") or fn.endswith('-407.cam1'):
#         os.rename(src, dst)
#         print("Objeto Renombrado")

#logging.debug()
       
