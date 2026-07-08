import re

with open('K-UI.lua', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix Dropdown chevron and ValLabel
code = code.replace('Position = UDim2.new(1, -30, 0.5, -10)', 'Position = UDim2.new(1, -55, 0.5, -10)') # Chevron
code = code.replace('Size = UDim2.new(0, 100, 1, 0),\n                    Position = UDim2.new(1, -140, 0, 0)', 'Size = UDim2.new(0, 100, 1, 0),\n                    Position = UDim2.new(1, -165, 0, 0)') # ValLabel

# Fix MultiDropdown
code = code.replace('Size = UDim2.new(0, 150, 1, 0),\n                    Position = UDim2.new(1, -190, 0, 0)', 'Size = UDim2.new(0, 150, 1, 0),\n                    Position = UDim2.new(1, -215, 0, 0)') # ValLabel (Multi)

# Fix TextBox input box
tb_old = 'Position = UDim2.new(0.5, 0, 0, 2),\n                    Size = UDim2.new(0.5, -10, 1, -4),'
tb_new = 'Position = UDim2.new(0.5, -20, 0, 2),\n                    Size = UDim2.new(0.5, -15, 1, -4),'
code = code.replace(tb_old, tb_new)

# Fix Keybind button
kb_old = 'Position = UDim2.new(0.5, 0, 0, 2),\n                    Size = UDim2.new(0.5, 0, 1, -4),'
kb_new = 'Position = UDim2.new(0.5, -20, 0, 2),\n                    Size = UDim2.new(0.5, -15, 1, -4),'
code = code.replace(kb_old, kb_new)

# Fix ColorPicker preview box
cp_old = 'Position = UDim2.new(1, -60, 0.5, -9),\n                    Size = UDim2.new(0, 40, 0, 18)'
cp_new = 'Position = UDim2.new(1, -85, 0.5, -9),\n                    Size = UDim2.new(0, 40, 0, 18)'
code = code.replace(cp_old, cp_new)

with open('K-UI.lua', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed positions!")
