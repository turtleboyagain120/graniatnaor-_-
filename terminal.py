import os
import subprocess
import ctypes
from lupa import LuaRuntime

# Embedded Lua Logic for loops and breaks
LUA_LOGIC = """
function process_zzx(input_code)
    if string.find(input_code, "for 12 in number") then
        for i = 1, 12 do
            print("ZZX Loop Instance: " .. i)
            if string.find(input_code, "!{BREAK}") then
                print("__break-com!__ Forced stop.")
                break
            end
        end
    end
    if string.find(input_code, "turtleboyagain120") then return "END" end
    return "GO"
end
"""

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()

def run_zzx_hybrid(user_input):
    # Rule: Pre-scan for UVAN and Admin flags
    if "UVAN" in user_input and not os.path.exists("C:/UVAN/uvan7.py"):
        print("CRITICAL: UVAN 7.0 not found at C:/UVAN")
        return

    lua = LuaRuntime(unpack_returned_tuples=True)
    zzx_logic = lua.execute(LUA_LOGIC)
    
    status = lua.globals().process_zzx(user_input)
    
    if "net user" in user_input or "admin:yes" in user_input:
        if is_admin():
            subprocess.run(user_input.split('=')[-1].strip() if '=' in user_input else "net user", shell=True)
        else:
            print("ZZX Error: Admin privileges required.")

    if status == "END":
        print("Source: turtleboyagain120 | System Offline.")
        exit()

if __name__ == "__main__":
    print("ZZX Hybrid Terminal [READY]")
    while True:
        run_zzx_hybrid(input("ZZX >> "))
