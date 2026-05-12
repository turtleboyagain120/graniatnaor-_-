"""ZZX Custom Hybrid Terminal Logic."""
import subprocess
import ctypes
import os
from lupa import LuaRuntime

def is_admin():
    """Checks for admin rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception: # pylint: disable=broad-exception-caught
        return False

def sys_net_user(username, action):
    """Real system user management."""
    command = f"net user {username} /add" if action == "add" else f"net user {username}"
    subprocess.run(command, shell=True, check=True)

def sys_stop_service(service_name):
    """Real system service control."""
    subprocess.run(f"net stop {service_name}", shell=True, check=True)

lua = LuaRuntime(unpack_returned_tuples=True)
lua.globals().net_user = sys_net_user
lua.globals().stop_service = sys_stop_service

def run_zzx_hybrid(user_input): # Changed 'code' to 'user_input' to avoid confusion
    """Scans and executes ZZX commands."""
    if "UVAN" in user_input and not os.path.exists("C:/UVAN"):
        print("CRITICAL: UVAN 7.0 not found.")
        return

    try:
        lua.execute(f"""
            if string.find("{user_input}", "admin:yes") then
                net_user("admin", "check")
            end
        """)
    except Exception as err: # Changed 'e' to 'err'
        print(f"ZZX Runtime Error: {err}")

if __name__ == "__main__":
    print("ZZX Terminal [READY]")
    while True:
        cmd = input("ZZX >> ")
        run_zzx_hybrid(cmd)
