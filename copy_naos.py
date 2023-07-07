import sys
import pyperclip
import os
windows_path=sys.argv[1]
#On prend le répertoire parent de celui qui contient le script
if getattr(sys, 'frozen', False):
    naos_share = os.path.dirname(os.path.dirname(sys.executable))
elif __file__:
    naos_share = os.path.dirname(os.path.dirname(__file__))
naos_share=naos_share.split("\\",1)[1]
#J'arrive pas à gérer les chemins UNC correctement, alors je prends ce qu'il y a 'après' le chemin d'où se situe le dossier parent
relative_path=windows_path.split(naos_share)[1]
linux_path="file:///mnt/naos_share"+relative_path.replace("\\", '/')
pyperclip.copy(linux_path)