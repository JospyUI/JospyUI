import os
import random

def obfuscate_lua(filepath, outpath):
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()

    # Create the byte array string
    byte_str = ""
    for char in code:
        byte_str += f"\\{ord(char)}"
        
    # Add some random junk variables to confuse simple decompilers
    junk1 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
    junk2 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=15))
    
    obfuscated_code = f"""-- Obfuscated by Jospy Builder
local {junk1} = "JOSPY_PROTECTED"
local {junk2} = 0
for i = 1, 10 do {junk2} = {junk2} + i end
return loadstring("{byte_str}")()
"""

    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(obfuscated_code)
    print(f"Obfuscated {filepath} -> {outpath}")

if __name__ == "__main__":
    if not os.path.exists("src"):
        print("src/ directory not found!")
        exit(1)
        
    # Obfuscate core library
    if os.path.exists("src/K-UI.lua"):
        obfuscate_lua("src/K-UI.lua", "K-UI.lua")
        
    # Obfuscate example script
    if os.path.exists("src/Example.lua"):
        obfuscate_lua("src/Example.lua", "Example.lua")
        
    # Obfuscate any other scripts in src
    for file in os.listdir("src"):
        if file.endswith(".lua") and file not in ["K-UI.lua", "Example.lua"]:
            obfuscate_lua(os.path.join("src", file), file)
            
    print("Build complete! All files have been obfuscated to the root directory.")
