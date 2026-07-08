-- K-UI Full Showcase Script
-- This script demonstrates every single feature available in the K-UI Library.

local K_UI = loadstring(game:HttpGet("https://raw.githubusercontent.com/GeceUstasi/BlueMoonUI/master/K-UI.lua"))()

-- 1. Create the Main Window
local Window = K_UI:CreateWindow("K-UI Showcase", {
    Accent = Color3.fromRGB(58, 108, 243),
    Acrylic = true -- Enables background blur when UI is open
})

print("Injected via:", K_UI.GetExecutor())

-- 2. Create Tabs
local CombatTab = Window:CreateTab("Combat")
local VisualsTab = Window:CreateTab("Visuals")

-- ==========================================
-- COMBAT TAB
-- ==========================================
local AimbotSection = CombatTab:CreateSection("Aimbot Settings")

-- Label (Information text)
AimbotSection:CreateLabel("Welcome to K-UI! This is a label. It's great for showing instructions, warnings, or general information to the user.")

-- Toggle
AimbotSection:CreateToggle({
    Name = "Enable Aimbot",
    Default = false,
    Tooltip = "Turn the Aimbot on or off.",
    Flag = "AimbotToggle",
    Callback = function(state)
        print("Aimbot is now:", state)
    end
})

AimbotSection:CreateDivider()

-- Slider
local fovSlider = AimbotSection:CreateSlider({
    Name = "Aimbot FOV",
    Min = 0,
    Max = 360,
    Default = 90,
    Tooltip = "Adjusts the field of view for the aimbot.",
    Flag = "AimbotFOV",
    Callback = function(value)
        print("Aimbot FOV set to:", value)
    end
})

-- Dropdown
AimbotSection:CreateDropdown({
    Name = "Target Part (Searchable)",
    Options = {"Head", "Torso", "HumanoidRootPart", "Left Arm", "Right Arm", "Left Leg", "Right Leg"},
    Default = "Head",
    Searchable = true,
    Tooltip = "Select which body part the aimbot should lock onto. You can type to search!",
    Flag = "TargetPart",
    Callback = function(selected)
        print("Target Part set to:", selected)
    end
})

-- Button
AimbotSection:CreateButton("Reset FOV to 90", function()
    fovSlider.Set(90)
    print("FOV Reset!")
end)


-- ==========================================
-- VISUALS TAB
-- ==========================================
local ESPSection = VisualsTab:CreateSection("ESP Options")

ESPSection:CreateDivider("Visual Filters")

local dynDrop = ESPSection:CreateDropdown({
    Name = "Target Priority",
    Options = {"Distance", "Health", "Threat"},
    Default = "Distance",
    Tooltip = "Choose who the Aimbot targets first.",
    Flag = "TargetPriority",
    Callback = function(selected)
        print("Priority set to:", selected)
    end
})

ESPSection:CreateButton("Update Priority Options", function()
    dynDrop.SetOptions({"Closest", "Lowest HP", "Highest Level"})
    dynDrop.SetTitle("Target Priority (Updated)")
    print("Dropdown options updated via API!")
end)

-- Multi-Dropdown
local multiDrop = ESPSection:CreateMultiDropdown({
    Name = "ESP Filters",
    Options = {"Players", "NPCs", "Items", "Vehicles", "Chests"},
    Default = {"Players", "NPCs"},
    Tooltip = "Select multiple entities to draw ESP boxes around.",
    Flag = "ESPFilters",
    Callback = function(selectedArray)
        print("ESP Filters updated:")
        for _, v in pairs(selectedArray) do
            print("-", v)
        end
    end
})

-- Color Picker
ESPSection:CreateColorPicker({
    Name = "ESP Box Color (Alpha)",
    Default = Color3.fromRGB(255, 0, 0),
    Tooltip = "Choose the color and transparency (Alpha) for the ESP boxes.",
    Flag = "ESPBoxColor",
    Callback = function(color)
        print("ESP Color changed to:", color.R, color.G, color.B)
    end
})


-- ==========================================
-- MISC / OTHER
-- ==========================================
local MiscSection = CombatTab:CreateSection("Miscellaneous")

-- Keybind
local triggerBind = MiscSection:CreateKeybind({
    Name = "Triggerbot Key (Hold Mode)",
    Default = Enum.KeyCode.E,
    Tooltip = "Hold this key to automatically shoot when aiming at an enemy.",
    Flag = "TriggerKey",
    OnBind = function(key)
        print("Triggerbot Key set to:", key.Name)
    end,
    Callback = function(state)
        print("Triggerbot Active:", state)
    end
})

-- TextBox
MiscSection:CreateTextBox({
    Name = "Player to Target",
    Placeholder = "Enter username...",
    Tooltip = "Type a player's exact username here to exclusively target them.",
    Flag = "TargetUsername",
    Callback = function(text)
        print("Now targeting player:", text)
    end
})

MiscSection:CreateClipboard("Copy Discord Invite", "https://discord.gg/invite")

MiscSection:CreateDivider("API Demonstration")

local apiToggle = MiscSection:CreateToggle({
    Name = "Disable Settings",
    Default = false,
    Callback = function(state)
        -- Demonstrating the SetDisabled API on other elements
        triggerBind.SetDisabled(state)
        if state then
            triggerBind.SetTitle("Triggerbot (DISABLED)")
        else
            triggerBind.SetTitle("Triggerbot Key (Hold Mode)")
        end
    end
})

local ConfigSection = VisualsTab:CreateSection("Configuration System")

ConfigSection:CreateButton("Save Config", function()
    -- Saves all elements that have a 'Flag' assigned to them.
    Window:SaveConfig("K_UI_Configs", "MyShowcaseConfig")
    print("Config saved!")
end)

ConfigSection:CreateButton("Load Config", function()
    Window:LoadConfig("K_UI_Configs", "MyShowcaseConfig")
    print("Config loaded!")
end)

-- The first tab is selected automatically.
