local K_UI = loadstring(game:HttpGet("https://raw.githubusercontent.com/JospyUI/JospyUI/master/K-UI.lua"))()

local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local LocalPlayer = Players.LocalPlayer

local Window = K_UI:CreateWindow("Jospy Hub", {
    Accent = Color3.fromRGB(255, 85, 127),
    Ping = true,
    ToggleKey = Enum.KeyCode.RightShift
})

-- ==========================================
-- LOCALPLAYER TAB
-- ==========================================
local MovementTab = Window:CreateTab("LocalPlayer", K_UI.GetIcon("lucide-user"))
local MoveSection = MovementTab:CreateSection("Character Mods")

-- Speed
local WalkSpeedVal = 16
MoveSection:CreateSlider({
    Name = "WalkSpeed",
    Min = 16,
    Max = 250,
    Default = 16,
    Flag = "WalkSpeed",
    Callback = function(val)
        WalkSpeedVal = val
        if LocalPlayer.Character and LocalPlayer.Character:FindFirstChild("Humanoid") then
            LocalPlayer.Character.Humanoid.WalkSpeed = val
        end
    end
})

-- WalkSpeed Loop (Anti-Cheat bypass)
task.spawn(function()
    while task.wait(0.5) do
        if LocalPlayer.Character and LocalPlayer.Character:FindFirstChild("Humanoid") then
            if WalkSpeedVal ~= 16 then 
                LocalPlayer.Character.Humanoid.WalkSpeed = WalkSpeedVal 
            end
        end
    end
end)

-- Inf Jump
local InfJumpEnabled = false
MoveSection:CreateToggle({
    Name = "Infinite Jump",
    Default = false,
    Flag = "InfJump",
    Callback = function(state) InfJumpEnabled = state end
})

UserInputService.JumpRequest:Connect(function()
    if InfJumpEnabled and LocalPlayer.Character and LocalPlayer.Character:FindFirstChild("Humanoid") then
        LocalPlayer.Character.Humanoid:ChangeState(Enum.HumanoidStateType.Jumping)
    end
end)

-- Noclip
local NoclipEnabled = false
MoveSection:CreateToggle({
    Name = "Noclip",
    Default = false,
    Flag = "Noclip",
    Callback = function(state) NoclipEnabled = state end
})

RunService.Stepped:Connect(function()
    if NoclipEnabled and LocalPlayer.Character then
        for _, part in ipairs(LocalPlayer.Character:GetDescendants()) do
            if part:IsA("BasePart") then 
                part.CanCollide = false 
            end
        end
    end
end)

-- Fly
local FlyEnabled = false
local FlySpeed = 50
local Camera = workspace.CurrentCamera

local function RemoveFly()
    if LocalPlayer.Character and LocalPlayer.Character:FindFirstChild("HumanoidRootPart") then
        local hrp = LocalPlayer.Character.HumanoidRootPart
        LocalPlayer.Character.Humanoid.PlatformStand = false
        if hrp:FindFirstChild("FlyVelocity") then hrp.FlyVelocity:Destroy() end
        if hrp:FindFirstChild("FlyGyro") then hrp.FlyGyro:Destroy() end
    end
end

MoveSection:CreateToggle({
    Name = "Fly",
    Default = false,
    Flag = "FlyToggle",
    Callback = function(state)
        FlyEnabled = state
        if not state then
            RemoveFly()
        else
            if LocalPlayer.Character and LocalPlayer.Character:FindFirstChild("HumanoidRootPart") then
                local hrp = LocalPlayer.Character.HumanoidRootPart
                LocalPlayer.Character.Humanoid.PlatformStand = true
                
                local bodyVel = Instance.new("BodyVelocity")
                bodyVel.Name = "FlyVelocity"
                bodyVel.MaxForce = Vector3.new(9e9, 9e9, 9e9)
                bodyVel.Velocity = Vector3.zero
                bodyVel.Parent = hrp
                
                local bodyGyro = Instance.new("BodyGyro")
                bodyGyro.Name = "FlyGyro"
                bodyGyro.MaxTorque = Vector3.new(9e9, 9e9, 9e9)
                bodyGyro.P = 9e4
                bodyGyro.CFrame = hrp.CFrame
                bodyGyro.Parent = hrp
            end
        end
    end
})

MoveSection:CreateSlider({
    Name = "Fly Speed",
    Min = 10,
    Max = 300,
    Default = 50,
    Flag = "FlySpeed",
    Callback = function(val) FlySpeed = val end
})

-- Fly Controls (W, A, S, D, Space, LCtrl)
local W, A, S, D, Space, LCtrl = false, false, false, false, false, false
UserInputService.InputBegan:Connect(function(input, gpe)
    if gpe then return end
    if input.KeyCode == Enum.KeyCode.W then W = true
    elseif input.KeyCode == Enum.KeyCode.A then A = true
    elseif input.KeyCode == Enum.KeyCode.S then S = true
    elseif input.KeyCode == Enum.KeyCode.D then D = true
    elseif input.KeyCode == Enum.KeyCode.Space then Space = true
    elseif input.KeyCode == Enum.KeyCode.LeftControl then LCtrl = true end
end)
UserInputService.InputEnded:Connect(function(input, gpe)
    if input.KeyCode == Enum.KeyCode.W then W = false
    elseif input.KeyCode == Enum.KeyCode.A then A = false
    elseif input.KeyCode == Enum.KeyCode.S then S = false
    elseif input.KeyCode == Enum.KeyCode.D then D = false
    elseif input.KeyCode == Enum.KeyCode.Space then Space = false
    elseif input.KeyCode == Enum.KeyCode.LeftControl then LCtrl = false end
end)

RunService.RenderStepped:Connect(function()
    if FlyEnabled and LocalPlayer.Character and LocalPlayer.Character:FindFirstChild("HumanoidRootPart") then
        local hrp = LocalPlayer.Character.HumanoidRootPart
        local bodyVel = hrp:FindFirstChild("FlyVelocity")
        local bodyGyro = hrp:FindFirstChild("FlyGyro")
        
        if bodyVel and bodyGyro then
            local moveDir = Vector3.zero
            if W then moveDir = moveDir + Camera.CFrame.LookVector end
            if S then moveDir = moveDir - Camera.CFrame.LookVector end
            if A then moveDir = moveDir - Camera.CFrame.RightVector end
            if D then moveDir = moveDir + Camera.CFrame.RightVector end
            if Space then moveDir = moveDir + Vector3.new(0, 1, 0) end
            if LCtrl then moveDir = moveDir - Vector3.new(0, 1, 0) end
            
            bodyVel.Velocity = moveDir * FlySpeed
            bodyGyro.CFrame = Camera.CFrame
        end
    end
end)


-- ==========================================
-- MISC TAB
-- ==========================================
local TeleportTab = Window:CreateTab("Misc", K_UI.GetIcon("lucide-folder-open"))
local TPSection = TeleportTab:CreateSection("Teleports")

local function teleportTo(x, y, z)
    if LocalPlayer.Character and LocalPlayer.Character:FindFirstChild("HumanoidRootPart") then
        LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(x, y, z)
    end
end

TPSection:CreateButton("Location 1 (-193, 3, 61)", function()
    teleportTo(-193, 3, 61)
    K_UI:Notify("Teleport", "Teleported to Location 1!", 2)
end)

TPSection:CreateButton("Location 2 (-158, 4, -157)", function()
    teleportTo(-158, 4, -157)
    K_UI:Notify("Teleport", "Teleported to Location 2!", 2)
end)

local CustomTPSection = TeleportTab:CreateSection("Custom Coordinates")
local tpX, tpY, tpZ = 0, 0, 0

CustomTPSection:CreateInput({
    Name = "X, Y, Z (Comma separated)",
    Placeholder = "e.g., 100, 50, -100",
    Flag = "CustomCoords",
    Callback = function(text)
        local coords = string.split(text, ",")
        if #coords == 3 then
            tpX = tonumber(coords[1]) or 0
            tpY = tonumber(coords[2]) or 0
            tpZ = tonumber(coords[3]) or 0
        end
    end
})

CustomTPSection:CreateButton("Teleport to Coordinates", function()
    teleportTo(tpX, tpY, tpZ)
end)

-- ==========================================
-- FARM / COMBAT TAB
-- ==========================================
local FarmTab = Window:CreateTab("Farm", K_UI.GetIcon("lucide-crosshair"))
local AutoFarmSection = FarmTab:CreateSection("Auto Farming")

local AutoFarmEnabled = false
local ReplicatedStorage = game:GetService("ReplicatedStorage")

AutoFarmSection:CreateToggle({
    Name = "Fast Auto-Farm (Tool Spammer)",
    Default = false,
    Flag = "AutoFarmToggle",
    Callback = function(state)
        AutoFarmEnabled = state
    end
})

task.spawn(function()
    while task.wait(0.05) do -- Sunucuyu tamamen çökertmemek için küçük bir gecikme ekliyoruz. 0.05 saniyede bir vurur (Saniyede 20 vuruş).
        if AutoFarmEnabled then
            -- ReplicatedStorage içindeki Event'i güvenli şekilde bulalım
            local eventsFolder = ReplicatedStorage:FindFirstChild("Events")
            if eventsFolder then
                local toolEvent = eventsFolder:FindFirstChild("ToolEvent")
                if toolEvent then
                    -- Animasyonu beklemeden iki sinyali de peş peşe atıyoruz!
                    toolEvent:FireServer("Activated", false)
                    toolEvent:FireServer("Activated", true)
                end
            end
        end
    end
end)

AutoFarmSection:CreateButton("Give VIP & Cola Effects (Local)", function()
    if LocalPlayer.Character then
        -- Karaktere gizli özellikleri tanımlıyoruz
        LocalPlayer.Character:SetAttribute("Effect_Cola", true)
        LocalPlayer.Character:SetAttribute("Rebirth", true)
        K_UI:Notify("Boost", "Kola ve Rebirth efektleri karakterine uygulandı!", 3)
    end
end)

K_UI:Notify("Jospy Hub", "Script loaded successfully!", 3)
