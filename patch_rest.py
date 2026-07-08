with open('K-UI.lua', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace TextBox
tb_old = "function SecObj:CreateTextBox(label, placeholder, callback)"
tb_new = """function SecObj:CreateTextBox(configOrLabel, placeholderText, callbackFunc)
                local config = type(configOrLabel) == "table" and configOrLabel or {Name = configOrLabel, Placeholder = placeholderText, Callback = callbackFunc}
                local label = config.Name or "TextBox"
                local placeholder = config.Placeholder or "Type here..."
                local callback = config.Callback
                local tooltip = config.Tooltip
                local flag = config.Flag
"""
code = code.replace(tb_old, tb_new)
code = code.replace("TxtContainer.Parent = SecFrame", "TxtContainer.Parent = SecFrame\n                AddTooltip(TxtContainer, tooltip)")
code = code.replace("return API\n            end\n\n            function SecObj:CreateKeybind", "if flag then Library.Flags[flag] = API end\n                return API\n            end\n\n            function SecObj:CreateKeybind")

# Replace Keybind
kb_old = "function SecObj:CreateKeybind(label, defaultKey, callback)"
kb_new = """function SecObj:CreateKeybind(configOrLabel, defaultKeyVal, callbackFunc)
                local config = type(configOrLabel) == "table" and configOrLabel or {Name = configOrLabel, Default = defaultKeyVal, Callback = callbackFunc}
                local label = config.Name or "Keybind"
                local defaultKey = config.Default or Enum.KeyCode.Unknown
                local callback = config.Callback
                local tooltip = config.Tooltip
                local flag = config.Flag
                local mode = config.Mode or "Toggle" -- Toggle, Hold, Always
"""
code = code.replace(kb_old, kb_new)
code = code.replace("BindContainer.Parent = SecFrame", "BindContainer.Parent = SecFrame\n                AddTooltip(BindContainer, tooltip)")

# Add advanced keybind mode logic
kb_logic_old = """                UserInputService.InputBegan:Connect(function(input, gameProcessed)
                    if not binding then
                        if input.UserInputType == Enum.UserInputType.Keyboard and input.KeyCode == currentKey and not gameProcessed then
                            if callback then callback() end
                        end
                        return
                    end"""
kb_logic_new = """                local keyState = false
                UserInputService.InputBegan:Connect(function(input, gameProcessed)
                    if not binding then
                        if input.UserInputType == Enum.UserInputType.Keyboard and input.KeyCode == currentKey and not gameProcessed then
                            if mode == "Toggle" then
                                keyState = not keyState
                                if callback then callback(keyState) end
                            elseif mode == "Hold" then
                                keyState = true
                                if callback then callback(true) end
                            elseif mode == "Always" then
                                if callback then callback(true) end
                            else
                                if callback then callback() end
                            end
                        end
                        return
                    end"""
code = code.replace(kb_logic_old, kb_logic_new)

kb_up_old = """                        binding = false
                    end
                end)"""
kb_up_new = """                        binding = false
                    end
                end)
                
                UserInputService.InputEnded:Connect(function(input, gameProcessed)
                    if not binding and mode == "Hold" and input.UserInputType == Enum.UserInputType.Keyboard and input.KeyCode == currentKey and not gameProcessed then
                        keyState = false
                        if callback then callback(false) end
                    end
                end)
"""
code = code.replace(kb_up_old, kb_up_new)
code = code.replace("return API\n            end\n\n            function SecObj:CreateColorPicker", "if flag then Library.Flags[flag] = API end\n                return API\n            end\n\n            function SecObj:CreateColorPicker")


# Replace ColorPicker
cp_old = "function SecObj:CreateColorPicker(label, defaultColor, callback)"
cp_new = """function SecObj:CreateColorPicker(configOrLabel, defaultColorVal, callbackFunc)
                local config = type(configOrLabel) == "table" and configOrLabel or {Name = configOrLabel, Default = defaultColorVal, Callback = callbackFunc}
                local label = config.Name or "Color Picker"
                local defaultColor = config.Default or Color3.new(1, 1, 1)
                local callback = config.Callback
                local tooltip = config.Tooltip
                local flag = config.Flag
"""
code = code.replace(cp_old, cp_new)
code = code.replace("CPContainer.Parent = SecFrame", "CPContainer.Parent = SecFrame\n                AddTooltip(TopBar, tooltip)")
code = code.replace("return API\n            end\n\n            function SecObj:CreateToggle", "if flag then Library.Flags[flag] = API end\n                return API\n            end\n\n            function SecObj:CreateToggle")


with open('K-UI.lua', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patched Rest!")
