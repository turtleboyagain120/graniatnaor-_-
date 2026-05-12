import subprocess
import ctypes
import os
import sys
from lupa import LuaRuntime # Install this via 'pip install lupa'

# 1. Admin Verification
def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()

# 2. Real System Hooks (The "Not Fake" parts)
def sys_net_user(username, action):
    """Physically creates or modifies a Windows user."""
    cmd = f"net user {username} /add" if action == "add" else f"net user {username}"
    subprocess.run(cmd, shell=True, check=True)

def sys_stop_service(service_name):
    """Physically stops a real Windows service."""
    subprocess.run(f"net stop {service_name}", shell=True, check=True)

# 3. Hybrid Lua Integration
lua = LuaRuntime(unpack_returned_tuples=True)
# Inject Python system functions into the Lua environment
lua.globals().net_user = sys_net_user
lua.globals().stop_service = sys_stop_service

def run_zzx_hybrid(code):
    # PRE-SCAN: Real check for UVAN directory
    if "UVAN" in code and not os.path.exists("C:/UVAN"):
        print("CRITICAL: UVAN 7.0 not found on PC.")
        return

    # EXECUTION: Pass the command to Lua logic
    # This turns your custom syntax into real actions
    try:
        lua.execute(f"""
            if string.find("{code}", "admin:yes") then
                net_user("admin", "check")
            end
            if string.find("{code}", "force net stop") then
                stop_service("bits") -- Example: stops Background Intelligent Transfer Service
            end
        """)
    except Exception as e:
        print(f"ZZX Runtime Error: {e}")

# Terminal Loop
print("ZZX Python-Lua Hybrid Terminal [READY]")
while True:
    cmd = input("ZZX >> ")
    run_zzx_hybrid(cmd)
