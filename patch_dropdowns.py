with open('K-UI.lua', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Dropdown signature
drop_old = "function SecObj:CreateDropdown(label, options, default, callback)"
drop_new = """function SecObj:CreateDropdown(configOrLabel, optionsList, defaultVal, callbackFunc)
                local config = type(configOrLabel) == "table" and configOrLabel or {Name = configOrLabel, Options = optionsList, Default = defaultVal, Callback = callbackFunc}
                local label = config.Name or "Dropdown"
                local options = config.Options or {}
                local default = config.Default
                local callback = config.Callback
                local tooltip = config.Tooltip
                local flag = config.Flag
                local searchable = config.Searchable or false
"""
code = code.replace(drop_old, drop_new)
code = code.replace("DropContainer.Parent = SecFrame", "DropContainer.Parent = SecFrame\n                AddTooltip(TopBar, tooltip)")

# Add SearchBox to Dropdown
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
code = code.replace(drop_search_old, drop_search_new, 1)

# Modify UpdateHeight to count Visible TextButtons
drop_height_old = """                        for _, child in pairs(DropList:GetChildren()) do
                            if child:IsA("TextButton") then btnCount = btnCount + 1 end
                        end"""
drop_height_new = """                        for _, child in pairs(DropList:GetChildren()) do
                            if child:IsA("TextButton") and child.Visible then btnCount = btnCount + 1 end
                        end"""
code = code.replace(drop_height_old, drop_height_new)

# Modify Dropdown UpdateOptions
drop_opt_old = """                        OptBtn.MouseButton1Click:Connect(function()
                            selected = opt
                            ValLabel.Text = selected
                            local tween = Tween(DropList, {Size = UDim2.new(1, 0, 0, 0)}, 0.2)
                            tween.Completed:Connect(function()
                                DropList.Visible = false
                                isExpanded = false
                                Tween(Chevron, {Rotation = 0}, 0.3)
                            end)
                            if callback then callback(selected) end
                        end)
                    end
                    UpdateHeight()
                end"""

drop_opt_new = """                        OptBtn.MouseButton1Click:Connect(function()
                            selected = opt
                            ValLabel.Text = selected
                            local tween = Tween(DropList, {Size = UDim2.new(1, 0, 0, 0)}, 0.2)
                            tween.Completed:Connect(function()
                                DropList.Visible = false
                                isExpanded = false
                                Tween(Chevron, {Rotation = 0}, 0.3)
                            end)
                            if searchable then
                                SearchBox.Visible = false
                                SearchBox.Text = ""
                            end
                            if callback then callback(selected) end
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
code = code.replace(drop_opt_old, drop_opt_new)

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
code = code.replace(drop_expand_old, drop_expand_new, 1)

# Return API logic
drop_api_old = """                API.GetValue = function() return selected end
                return API
            end

            function SecObj:CreateMultiDropdown"""
drop_api_new = """                API.GetValue = function() return selected end
                if flag then Library.Flags[flag] = API end
                return API
            end

            function SecObj:CreateMultiDropdown"""
code = code.replace(drop_api_old, drop_api_new)

with open('K-UI.lua', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patched Dropdown!")
