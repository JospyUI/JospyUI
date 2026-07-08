with open('K-UI.lua', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace MultiDropdown signature
drop_old = "function SecObj:CreateMultiDropdown(label, options, defaultSelectedArray, callback)"
drop_new = """function SecObj:CreateMultiDropdown(configOrLabel, optionsList, defaultSelectedArray, callbackFunc)
                local config = type(configOrLabel) == "table" and configOrLabel or {Name = configOrLabel, Options = optionsList, Default = defaultSelectedArray, Callback = callbackFunc}
                local label = config.Name or "MultiDropdown"
                local options = config.Options or {}
                local defaultArray = config.Default or {}
                local callback = config.Callback
                local tooltip = config.Tooltip
                local flag = config.Flag
                local searchable = config.Searchable or false
"""
code = code.replace(drop_old, drop_new)
code = code.replace("DropContainer.Parent = SecFrame\n\n                local TopBar", "DropContainer.Parent = SecFrame\n                AddTooltip(DropContainer, tooltip)\n\n                local TopBar")

# Fix selectedDict initialization
code = code.replace("if defaultSelectedArray then\n                    for _, v in ipairs(defaultSelectedArray) do", "if defaultArray then\n                    for _, v in ipairs(defaultArray) do")


# Add SearchBox to MultiDropdown
drop_search_old = """                local DropList = Create("Frame", {"""
drop_search_new = """
                local SearchBox
                if searchable then
                    SearchBox = Create("TextBox", {
                        BackgroundColor3 = Theme.MainBackground,
                        Size = UDim2.new(1, 0, 0, 30),
                        Visible = false,
                        Font = Enum.Font.Ubuntu,
                        PlaceholderText = "Search...",
                        Text = "",
                        TextColor3 = Theme.TextPrimary,
                        TextSize = 13,
                        ClearTextOnFocus = false
                    }, {
                        Create("UICorner", { CornerRadius = UDim.new(0, 4) }),
                        Create("UIStroke", { Color = Theme.Border, Thickness = 1 }),
                        Create("UIPadding", { PaddingLeft = UDim.new(0, 5) })
                    })
                    SearchBox.Parent = DropContainer
                end
                
                local DropList = Create("Frame", {"""
code = code.replace(drop_search_old, drop_search_new, 1) # Only the first occurrence starting from where MultiDropdown is, actually wait, there is no way to specify start index easily. I'll just use regex or a split.

# Let's be safer: split by "function SecObj:CreateMultiDropdown" and replace in the second part.
parts = code.split("function SecObj:CreateMultiDropdown")
part2 = parts[1]
part2 = part2.replace(drop_search_old, drop_search_new, 1)

# Modify UpdateHeight to count Visible TextButtons
drop_height_old = """                        for _, child in pairs(DropList:GetChildren()) do
                            if child:IsA("TextButton") then btnCount = btnCount + 1 end
                        end"""
drop_height_new = """                        for _, child in pairs(DropList:GetChildren()) do
                            if child:IsA("TextButton") and child.Visible then btnCount = btnCount + 1 end
                        end"""
part2 = part2.replace(drop_height_old, drop_height_new)

# Modify Dropdown UpdateOptions
drop_opt_old = """                        OptBtn.MouseButton1Click:Connect(function()
                            selectedDict[opt] = not selectedDict[opt]
                            ValLabel.Text = GetSelectedString()
                            local isSelState = selectedDict[opt] == true
                            Tween(OptBtn, {TextColor3 = isSelState and Theme.Accent or Theme.TextPrimary}, 0.2)
                            if callback then callback(GetSelectedArray()) end
                        end)
                    end
                    UpdateHeight()
                end"""

drop_opt_new = """                        OptBtn.MouseButton1Click:Connect(function()
                            selectedDict[opt] = not selectedDict[opt]
                            ValLabel.Text = GetSelectedString()
                            local isSelState = selectedDict[opt] == true
                            Tween(OptBtn, {TextColor3 = isSelState and Theme.Accent or Theme.TextPrimary}, 0.2)
                            if callback then callback(GetSelectedArray()) end
                        end)
                    end
                    UpdateHeight()
                end
                
                if searchable then
                    SearchBox:GetPropertyChangedSignal("Text"):Connect(function()
                        local filter = string.lower(SearchBox.Text)
                        for _, child in pairs(DropList:GetChildren()) do
                            if child:IsA("TextButton") then
                                if filter == "" then
                                    child.Visible = true
                                else
                                    child.Visible = string.find(string.lower(child.Text), filter, 1, true) ~= nil
                                end
                            end
                        end
                        UpdateHeight()
                    end)
                end
"""
part2 = part2.replace(drop_opt_old, drop_opt_new)

# Expand / Collapse logic for Dropdown SearchBox
drop_expand_old = """                    if isExpanded then
                        DropList.Visible = true
                        UpdateHeight()
                    else
                        local tween = Tween(DropList, {Size = UDim2.new(1, 0, 0, 0)}, 0.2)
                        tween.Completed:Connect(function() if not isExpanded then DropList.Visible = false end end)
                    end"""
drop_expand_new = """                    if isExpanded then
                        if searchable then SearchBox.Visible = true end
                        DropList.Visible = true
                        UpdateHeight()
                    else
                        if searchable then
                            SearchBox.Visible = false
                            SearchBox.Text = ""
                        end
                        local tween = Tween(DropList, {Size = UDim2.new(1, 0, 0, 0)}, 0.2)
                        tween.Completed:Connect(function() if not isExpanded then DropList.Visible = false end end)
                    end"""
part2 = part2.replace(drop_expand_old, drop_expand_new, 1)

# Return API logic
drop_api_old = """                API.GetValue = function() return GetSelectedArray() end
                return API
            end

            function SecObj:CreateSlider"""
drop_api_new = """                API.GetValue = function() return GetSelectedArray() end
                if flag then Library.Flags[flag] = API end
                return API
            end

            function SecObj:CreateSlider"""
part2 = part2.replace(drop_api_old, drop_api_new)

code = parts[0] + "function SecObj:CreateMultiDropdown" + part2

with open('K-UI.lua', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patched MultiDropdown!")
