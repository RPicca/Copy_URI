import winreg as reg
import os
import sys
#Creation clé pour fichier
if getattr(sys, 'frozen', False):
    naos_share = os.path.dirname(os.path.dirname(sys.executable))
elif __file__:
    naos_share = os.path.dirname(os.path.dirname(__file__))
key=reg.CreateKey(reg.HKEY_CURRENT_USER, "SOFTWARE\\Classes\\*\\shell\\URI_NAOS")
reg.SetValue(key, '', reg.REG_SZ, "URI_NAOS")
reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, naos_share+"\\URI_NAOS\\naos.ico")
reg.SetValue(key, 'command', reg.REG_SZ, "\""+naos_share+"\\URI_NAOS\\copy_naos.exe\" \"%1\"")

#Creation clé pour dossier
key=reg.CreateKey(reg.HKEY_CURRENT_USER, "SOFTWARE\\Classes\\directory\\shell\\URI_NAOS")
reg.SetValue(key, '', reg.REG_SZ, "URI_NAOS")
reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, naos_share+"\\URI_NAOS\\naos.ico")
reg.SetValue(key, 'command', reg.REG_SZ, "\""+naos_share+"\\URI_NAOS\\copy_naos.exe\" \"%1\"")

