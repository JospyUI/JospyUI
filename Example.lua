-- Example.lua: K-UI Showcase Script

local K_UI = loadstring(game:HttpGet("https://raw.githubusercontent.com/GeceUstasi/BlueMoonUI/master/K-UI.lua"))()

local Window = K_UI:CreateWindow("K-UI Showcase", {
    Accent = Color3.fromRGB(255, 90, 90) -- Example of overriding the accent color
})

local MainTab = Window:CreateTab("Main Features", "rbxassetid://6026568240")
local ConfigTab = Window:CreateTab("Settings", "rbxassetid://6031280882")

local MainSec = MainTab:CreateSection("Premium Elements")

MainSec:CreateLabel("Welcome to K-UI! This label is great for paragraphs and instructions.")

MainSec:CreateToggle({
    Name = "Aimbot",
    Default = false,
    Tooltip = "Automatically aims at the nearest enemy.",
    Flag = "AimbotToggle",
    Callback = function(state)
        print("Aimbot:", state)
    end
})

MainSec:CreateSlider({
    Name = "Aimbot FOV",
    Min = 0,
    Max = 360,
    Default = 90,
    Tooltip = "Field of view for the aimbot.",
    Flag = "AimbotFOV",
    Callback = function(val)
        print("FOV:", val)
    end
})

MainSec:CreateDropdown({
    Name = "Target Part (Searchable)",
    Options = {"Head", "Torso", "HumanoidRootPart", "Left Arm", "Right Arm", "Left Leg", "Right Leg"},
    Default = "Head",
    Searchable = true,
    Tooltip = "Select which part to aim at.",
    Flag = "TargetPartDrop",
    Callback = function(selected)
        print("Target Part:", selected)
    end
})

MainSec:CreateMultiDropdown({
    Name = "ESP Filters",
    Options = {"Players", "NPCs", "Items", "Vehicles", "Bosses", "Allies", "Enemies"},
    Default = {"Players", "Bosses"},
    Searchable = true,
    Tooltip = "Select multiple entities to draw ESP on.",
    Flag = "ESPTypes",
    Callback = function(selectedArray)
        print("ESP Types:")
        for _, v in ipairs(selectedArray) do print("-", v) end
    end
})

MainSec:CreateColorPicker({
    Name = "ESP Box Color (Alpha)",
    Default = Color3.fromRGB(255, 0, 0),
    Tooltip = "Change the color and transparency of the ESP box.",
    Flag = "ESPColor",
    Callback = function(color, transparency)
        print("Color changed:", color, "Transparency:", transparency)
    end
})

MainSec:CreateKeybind({
    Name = "Triggerbot Key (Hold Mode)",
    Default = Enum.KeyCode.E,
    Mode = "Hold", -- Can be Toggle, Hold, or Always
    Tooltip = "Hold this key to automatically shoot enemies.",
    Flag = "TriggerKey",
    Callback = function(isActive)
        print("Triggerbot Active:", isActive)
    end
})

MainSec:CreateTextBox({
    Name = "Player to Target",
    Placeholder = "Enter username...",
    Tooltip = "Target a specific player.",
    Flag = "TargetName",
    Callback = function(txt)
        print("Targeting:", txt)
    end
})

local ConfigSec = ConfigTab:CreateSection("Config System")

ConfigSec:CreateButton("Save Settings", function()
    local success = Window:SaveConfig("K_UI_Configs", "MySettings")
    if success then
        print("Settings saved successfully!")
    else
        print("Your executor does not support writefile.")
    end
end)

ConfigSec:CreateButton("Load Settings", function()
    local success = Window:LoadConfig("K_UI_Configs", "MySettings")
    if success then
        print("Settings loaded successfully!")
    else
        print("Failed to load settings.")
    end
end)
