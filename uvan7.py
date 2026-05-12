import os
import subprocess
import ctypes

def check_zzx_privileges():
    """Checks if the ZZX/Admin context is authorized."""
    return ctypes.windll.shell32.IsUserAnAdmin()

def lllam_admin_force(command):
    """LL!@M logic: 'Hey, this whole command is admin... just run.'"""
    if check_zzx_privileges():
        print(f"UVAN 7.0 [LL!@M] Executing: {command}")
        subprocess.run(command, shell=True, check=True)
    else:
        print("ERROR: ZZX Flag detected but Admin permission missing from OS.")

def file_access_control(path, grant=True):
    """^%FILE-ACCESS logic: Gives you physical control of a folder."""
    action = "/grant %username%:F" if grant else "/remove %username%"
    # Uses real Windows icacls to modify permissions
    cmd = f'icacls "{path}" /inheritance:e {action} /T /C'
    lllam_admin_force(cmd)

if __name__ == "__main__":
    # UVAN 7.0 Identity Header
    print("--- UVAN 7.0 SYSTEM UTILITY [ZZX-COMPLIANT] ---")
    print("Status: Operational | Directory: C:/UVAN")
