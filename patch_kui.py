import re

with open('K-UI.lua', 'r', encoding='utf-8') as f:
    code = f.read()

def inject_config_and_tooltip(func_signature, defaults, args_mapping, code):
    # This is a bit complex, let's just do standard string replacements.
    pass

# Helper to inject Tooltip logic
tooltip_logic = """
                local function AddTooltip(parent, text)
                    if not text then return end
                    local InfoIcon = Create("ImageLabel", {
                        BackgroundTransparency = 1,
                        Position = UDim2.new(1, -25, 0.5, -10),
                        Size = UDim2.new(0, 20, 0, 20),
                        Image = "rbxassetid://6031094678",
                        ImageColor3 = Theme.TextSecondary,
                        Parent = parent,
                        ZIndex = parent.ZIndex + 1
                    })
                    local TipFrame = Create("Frame", {
                        BackgroundColor3 = Theme.HeaderButtonBackground,
                        Position = UDim2.new(1, 5, 0.5, -15),
                        Size = UDim2.new(0, 0, 0, 30),
                        AutomaticSize = Enum.AutomaticSize.X,
                        Visible = false,
                        Parent = parent,
                        ZIndex = 1000
                    }, {
                        Create("UICorner", { CornerRadius = UDim.new(0, 6) }),
                        Create("UIStroke", { Color = Theme.Border, Thickness = 1 }),
                        Create("UIPadding", { PaddingLeft = UDim.new(0, 10), PaddingRight = UDim.new(0, 10) })
                    })
                    Create("TextLabel", {
                        BackgroundTransparency = 1,
                        Size = UDim2.new(1, 0, 1, 0),
                        Font = Enum.Font.Ubuntu,
                        Text = text,
                        TextColor3 = Theme.TextPrimary,
                        TextSize = 13,
                        Parent = TipFrame,
                        ZIndex = 1001
                    })
                    InfoIcon.MouseEnter:Connect(function() TipFrame.Visible = true end)
                    InfoIcon.MouseLeave:Connect(function() TipFrame.Visible = false end)
                end
"""

# Let's insert tooltip_logic inside SecObj creation or right before it.
if "local function AddTooltip" not in code:
    code = code.replace("            local SecObj = {}", tooltip_logic + "\n            local SecObj = {}")

# Replace Toggle
toggle_old = "function SecObj:CreateToggle(label, default, callback)"
toggle_new = """function SecObj:CreateToggle(configOrLabel, defaultVal, callbackFunc)
                local config = type(configOrLabel) == "table" and configOrLabel or {Name = configOrLabel, Default = defaultVal, Callback = callbackFunc}
                local label = config.Name or "Toggle"
                local default = config.Default or false
                local callback = config.Callback
                local tooltip = config.Tooltip
                local flag = config.Flag
"""
code = code.replace(toggle_old, toggle_new)
code = code.replace("Create(\"TextLabel\", {\n                    BackgroundTransparency = 1,\n                    Position = UDim2.new(0, 15, 0, 0),\n                    Size = UDim2.new(1, -70, 1, 0),\n                    Font = Enum.Font.Ubuntu,\n                    Text = label,", 
                    "Create(\"TextLabel\", {\n                    BackgroundTransparency = 1,\n                    Position = UDim2.new(0, 15, 0, 0),\n                    Size = UDim2.new(1, -70, 1, 0),\n                    Font = Enum.Font.Ubuntu,\n                    Text = label,")
code = code.replace("TogBtn.Parent = SecFrame", "TogBtn.Parent = SecFrame\n                AddTooltip(TogBtn, tooltip)")
code = code.replace("return API\n            end\n\n            function SecObj:CreateButton", "if flag then Library.Flags[flag] = API end\n                return API\n            end\n\n            function SecObj:CreateButton")

# Similar for Slider
slider_old = "function SecObj:CreateSlider(label, min, max, default, callback)"
slider_new = """function SecObj:CreateSlider(configOrLabel, minVal, maxVal, defaultVal, callbackFunc)
                local config = type(configOrLabel) == "table" and configOrLabel or {Name = configOrLabel, Min = minVal, Max = maxVal, Default = defaultVal, Callback = callbackFunc}
                local label = config.Name or "Slider"
                local min = config.Min or 0
                local max = config.Max or 100
                local default = config.Default or min
                local callback = config.Callback
                local tooltip = config.Tooltip
                local flag = config.Flag
"""
code = code.replace(slider_old, slider_new)
code = code.replace("SliderContainer.Parent = SecFrame", "SliderContainer.Parent = SecFrame\n                AddTooltip(SliderContainer, tooltip)")
code = code.replace("return API\n            end\n\n            function SecObj:CreateTextBox", "if flag then Library.Flags[flag] = API end\n                return API\n            end\n\n            function SecObj:CreateTextBox")

with open('K-UI.lua', 'w', encoding='utf-8') as f:
    f.write(code)

print("Applied quick regexes!")
