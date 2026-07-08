with open('K-UI.lua', 'r', encoding='utf-8') as f:
    code = f.read()

cp_alpha_old = """                local ValueSlider = Create("TextButton", {
                    BackgroundColor3 = Color3.new(1,1,1),
                    Position = UDim2.new(0, 95, 0, 5),
                    Size = UDim2.new(1, -100, 0, 80),"""

cp_alpha_new = """                local alpha = 1
                local ValueSlider = Create("TextButton", {
                    BackgroundColor3 = Color3.new(1,1,1),
                    Position = UDim2.new(0, 95, 0, 5),
                    Size = UDim2.new(0.5, -55, 0, 80),"""

code = code.replace(cp_alpha_old, cp_alpha_new)

cp_alpha_rest_old = """                local ValueLine = Create("Frame", {
                    BackgroundColor3 = Color3.new(1,1,1),
                    Size = UDim2.new(1, 4, 0, 2),
                    Position = UDim2.new(0, -2, 0, 0),
                    AnchorPoint = Vector2.new(0, 0.5)
                }, { Create("UIStroke", { Thickness = 1 }) })
                ValueLine.Parent = ValueSlider

                local function UpdateColor()
                    currentColor = Color3.fromHSV(hue, sat, val)
                    ColorPreview.BackgroundColor3 = currentColor
                    ValueSlider.UIGradient.Color = ColorSequence.new({
                        ColorSequenceKeypoint.new(0, Color3.fromHSV(hue, sat, 1)),
                        ColorSequenceKeypoint.new(1, Color3.new(0,0,0))
                    })
                    if callback then callback(currentColor) end
                end"""

cp_alpha_rest_new = """                local ValueLine = Create("Frame", {
                    BackgroundColor3 = Color3.new(1,1,1),
                    Size = UDim2.new(1, 4, 0, 2),
                    Position = UDim2.new(0, -2, 0, 0),
                    AnchorPoint = Vector2.new(0, 0.5)
                }, { Create("UIStroke", { Thickness = 1 }) })
                ValueLine.Parent = ValueSlider
                
                local AlphaSlider = Create("TextButton", {
                    BackgroundColor3 = Color3.new(1,1,1),
                    Position = UDim2.new(0.5, 45, 0, 5),
                    Size = UDim2.new(0.5, -55, 0, 80),
                    Text = "",
                    AutoButtonColor = false
                }, {
                    Create("UICorner", { CornerRadius = UDim.new(0, 4) }),
                    Create("UIStroke", { Color = Theme.Border, Thickness = 1 }),
                    Create("UIGradient", {
                        Color = ColorSequence.new({
                            ColorSequenceKeypoint.new(0, Color3.new(1,1,1)),
                            ColorSequenceKeypoint.new(1, Color3.new(1,1,1))
                        }),
                        Transparency = NumberSequence.new({
                            NumberSequenceKeypoint.new(0, 0),
                            NumberSequenceKeypoint.new(1, 1)
                        }),
                        Rotation = 90
                    })
                })
                AlphaSlider.Parent = DropList

                local AlphaLine = Create("Frame", {
                    BackgroundColor3 = Color3.new(1,1,1),
                    Size = UDim2.new(1, 4, 0, 2),
                    Position = UDim2.new(0, -2, 0, 0),
                    AnchorPoint = Vector2.new(0, 0.5)
                }, { Create("UIStroke", { Thickness = 1 }) })
                AlphaLine.Parent = AlphaSlider

                local function UpdateColor()
                    currentColor = Color3.fromHSV(hue, sat, val)
                    ColorPreview.BackgroundColor3 = currentColor
                    ColorPreview.BackgroundTransparency = 1 - alpha
                    ValueSlider.UIGradient.Color = ColorSequence.new({
                        ColorSequenceKeypoint.new(0, Color3.fromHSV(hue, sat, 1)),
                        ColorSequenceKeypoint.new(1, Color3.new(0,0,0))
                    })
                    AlphaSlider.UIGradient.Color = ColorSequence.new({
                        ColorSequenceKeypoint.new(0, currentColor),
                        ColorSequenceKeypoint.new(1, currentColor)
                    })
                    if callback then callback(currentColor, alpha) end
                end"""

code = code.replace(cp_alpha_rest_old, cp_alpha_rest_new)

cp_alpha_line_old = """                    WheelRing.Position = UDim2.new(0, center.X + x, 0, center.Y - y) -- y inverted for UI
                    ValueLine.Position = UDim2.new(0, -2, 1 - val, 0)
                end

                local wheelDragging, valDragging = false, false"""

cp_alpha_line_new = """                    WheelRing.Position = UDim2.new(0, center.X + x, 0, center.Y - y) -- y inverted for UI
                    ValueLine.Position = UDim2.new(0, -2, 1 - val, 0)
                    AlphaLine.Position = UDim2.new(0, -2, 1 - alpha, 0)
                end

                local wheelDragging, valDragging, alphaDragging = false, false, false"""

code = code.replace(cp_alpha_line_old, cp_alpha_line_new)

cp_alpha_input_old = """                local function UpdateValue(input)
                    local y = math.clamp(input.Position.Y - ValueSlider.AbsolutePosition.Y, 0, ValueSlider.AbsoluteSize.Y)
                    val = 1 - (y / ValueSlider.AbsoluteSize.Y)
                    ValueLine.Position = UDim2.new(0, -2, 0, y)
                    UpdateColor()
                end

                Wheel.InputBegan:Connect(function(input)
                    if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then
                        wheelDragging = true
                        UpdateWheel(input)
                    end
                end)
                ValueSlider.InputBegan:Connect(function(input)
                    if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then
                        valDragging = true
                        UpdateValue(input)
                    end
                end)
                UserInputService.InputEnded:Connect(function(input)
                    if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then
                        wheelDragging, valDragging = false, false
                    end
                end)
                UserInputService.InputChanged:Connect(function(input)
                    if input.UserInputType == Enum.UserInputType.MouseMovement or input.UserInputType == Enum.UserInputType.Touch then
                        if wheelDragging then UpdateWheel(input) end
                        if valDragging then UpdateValue(input) end
                    end
                end)"""

cp_alpha_input_new = """                local function UpdateValue(input)
                    local y = math.clamp(input.Position.Y - ValueSlider.AbsolutePosition.Y, 0, ValueSlider.AbsoluteSize.Y)
                    val = 1 - (y / ValueSlider.AbsoluteSize.Y)
                    ValueLine.Position = UDim2.new(0, -2, 0, y)
                    UpdateColor()
                end
                
                local function UpdateAlpha(input)
                    local y = math.clamp(input.Position.Y - AlphaSlider.AbsolutePosition.Y, 0, AlphaSlider.AbsoluteSize.Y)
                    alpha = 1 - (y / AlphaSlider.AbsoluteSize.Y)
                    AlphaLine.Position = UDim2.new(0, -2, 0, y)
                    UpdateColor()
                end

                Wheel.InputBegan:Connect(function(input)
                    if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then
                        wheelDragging = true
                        UpdateWheel(input)
                    end
                end)
                ValueSlider.InputBegan:Connect(function(input)
                    if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then
                        valDragging = true
                        UpdateValue(input)
                    end
                end)
                AlphaSlider.InputBegan:Connect(function(input)
                    if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then
                        alphaDragging = true
                        UpdateAlpha(input)
                    end
                end)
                UserInputService.InputEnded:Connect(function(input)
                    if input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch then
                        wheelDragging, valDragging, alphaDragging = false, false, false
                    end
                end)
                UserInputService.InputChanged:Connect(function(input)
                    if input.UserInputType == Enum.UserInputType.MouseMovement or input.UserInputType == Enum.UserInputType.Touch then
                        if wheelDragging then UpdateWheel(input) end
                        if valDragging then UpdateValue(input) end
                        if alphaDragging then UpdateAlpha(input) end
                    end
                end)"""

code = code.replace(cp_alpha_input_old, cp_alpha_input_new)

with open('K-UI.lua', 'w', encoding='utf-8') as f:
    f.write(code)

print("Patched Alpha Color Picker!")
