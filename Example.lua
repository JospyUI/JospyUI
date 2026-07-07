local BlueMoonUI = loadstring(game:HttpGet("https://raw.githubusercontent.com/GeceUstasi/BlueMoonUI/master/BlueMoonUI.lua"))()

-- Step 1: Initialize Key System
BlueMoonUI:CreateKeySystem({
    Title = "Blue Moon Premium",
    Key = "TESTKEY", 
    GetKeyUrl = "https://discord.gg/yourserver", 
    
    -- Step 2: Load Main UI after successful login
    OnComplete = function()
        local Window = BlueMoonUI:CreateWindow({
            Title = "Blue Moon",
            Version = "v2.0 PRO"
        })

        -- TAB 1: Combat
        local CombatTab = Window:CreateTab("Combat", BlueMoonUI.Icons.Farm)
        
        local MainSec = CombatTab:CreateSection("Aimbot Settings")
        
        local AimbotToggle = MainSec:CreateToggle("Enable Aimbot", false, function(state)
            if state then
                BlueMoonUI:Notify("Aimbot", "Aimbot is now active!", 3)
            else
                BlueMoonUI:Notify("Aimbot", "Aimbot disabled.", 3)
            end
        end)
        
        -- Dropdown Example
        local TargetPartDrop = MainSec:CreateDropdown("Target Part", {"Head", "Torso", "HumanoidRootPart"}, "Head", function(selected)
            print("Targeting: " .. selected)
        end)
        
        -- Slider Example
        MainSec:CreateSlider("Aimbot Smoothness", 1, 100, 50, function(value)
            print("Smoothness: " .. value)
        end)

        -- Keybind Example
        MainSec:CreateKeybind("Aimbot Key", Enum.KeyCode.E, function()
            print("Aimbot hotkey triggered!")
        end)

        -- TAB 2: Visuals
        local VisTab = Window:CreateTab("Visuals", BlueMoonUI.Icons.Eye)
        
        local EspSec = VisTab:CreateSection("ESP Options")
        
        local EspToggle = EspSec:CreateToggle("Player ESP", true, function(state)
            print("ESP: " .. tostring(state))
        end)
        
        -- MultiDropdown Example
        local EspTypesMulti = EspSec:CreateMultiDropdown("ESP Types", {"Players", "NPCs", "Items", "Vehicles"}, {"Players", "NPCs"}, function(selectedArray)
            print("Selected ESP Types count: " .. #selectedArray)
        end)

        -- Color Picker Example
        local EspColor = EspSec:CreateColorPicker("ESP Box Color", Color3.fromRGB(255, 80, 80), function(color)
            print("ESP Color changed!")
        end)

        -- TAB 3: Controllers (Showcase)
        local CtrlTab = Window:CreateTab("Controllers", BlueMoonUI.Icons.Settings)
        
        local FuncSec = CtrlTab:CreateSection("Programmatic Control")

        FuncSec:CreateButton("Turn ON Aimbot Toggle", function()
            AimbotToggle:Set(true) 
            BlueMoonUI:Notify("Code Executed", "Aimbot turned on via code.", 3)
        end)

        FuncSec:CreateButton("Change Target to Torso", function()
            TargetPartDrop:Set("Torso")
            BlueMoonUI:Notify("Code Executed", "Dropdown changed to Torso.", 3)
        end)

        FuncSec:CreateButton("Add 'Bosses' to ESP Types", function()
            EspTypesMulti:Refresh({"Players", "NPCs", "Items", "Vehicles", "Bosses"}, {"Players", "Bosses"})
            BlueMoonUI:Notify("Code Executed", "Multi-Dropdown refreshed.", 3)
        end)

        local MiscSec = CtrlTab:CreateSection("Misc")
        
        -- TextBox Example
        local WhitelistBox = MiscSec:CreateTextBox("Whitelist Player", "Enter Username...", function(text)
            BlueMoonUI:Notify("Whitelisted", text .. " has been ignored.", 4)
        end)

        MiscSec:CreateButton("Clear Whitelist Box", function()
            WhitelistBox:Set("")
        end)
        
        -- Welcome Notification
        BlueMoonUI:Notify("Authentication Success", "Welcome back to Blue Moon PRO!", 5)
    end
})
