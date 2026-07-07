local BlueMoonUI = loadstring(game:HttpGet("https://raw.githubusercontent.com/GeceUstasi/BlueMoonUI/master/BlueMoonUI.lua"))()

-- Step 1: Initialize Key System
BlueMoonUI:CreateKeySystem({
    Title = "Blue Moon Premium",
    Key = "TESTKEY", -- You can change this or use KeyUrl instead
    -- KeyUrl = "https://raw.githubusercontent.com/your/repo/key.txt", -- Checks key from website
    GetKeyUrl = "https://discord.gg/yourserver", -- Copies to clipboard when Get Key is pressed
    
    -- Step 2: Load Main UI after successful login
    OnComplete = function()
        local Window = BlueMoonUI:CreateWindow({
            Title = "Blue Moon",
            Version = "v2.0 PRO"
        })

        -- TAB 1: Combat
        local CombatTab = Window:CreateTab("Combat", BlueMoonUI.Icons.Farm)
        
        local MainSec = CombatTab:CreateSection("Main Settings")
        
        MainSec:CreateToggle("Aimbot", false, function(state)
            if state then
                BlueMoonUI:Notify("Aimbot Enabled", "Warning: Use at your own risk!", 3)
            end
        end)
        
        -- Fully working Dropdown!
        MainSec:CreateDropdown("Target Part", {"Head", "Torso", "HumanoidRootPart"}, "Head", function(selected)
            print("Targeting: " .. selected)
        end)
        
        -- Slider!
        MainSec:CreateSlider("Aimbot Smoothness", 1, 100, 50, function(value)
            print("Smoothness set to " .. value)
        end)

        -- Keybind!
        MainSec:CreateKeybind("Aimbot Key", Enum.KeyCode.E, function()
            print("Aimbot key pressed!")
        end)

        -- TAB 2: Visuals
        local VisTab = Window:CreateTab("Visuals", BlueMoonUI.Icons.Eye)
        
        local EspSec = VisTab:CreateSection("ESP Options")
        
        EspSec:CreateToggle("Player ESP", true, function() end)
        
        -- Color Picker (Wheel Style!)
        EspSec:CreateColorPicker("ESP Box Color", Color3.fromRGB(255, 80, 80), function(color)
            print("Color changed!")
        end)

        -- MultiDropdown Example
        MainSec:CreateMultiDropdown("Target ESP Types", {"Players", "NPCs", "Items", "Vehicles"}, {"Players", "NPCs"}, function(selectedArray)
            -- selectedArray is a table, e.g. {"Players", "NPCs"}
            print("Selected ESP Types count: " .. #selectedArray)
        end)

        -- TextBox!
        local MiscSec = VisTab:CreateSection("Misc")
        MiscSec:CreateTextBox("Whitelist Player", "Enter Username...", function(text)
            BlueMoonUI:Notify("Whitelisted", text .. " has been ignored by aimbot.", 4)
        end)

        -- Example of Programmatic Module Control
        local TestToggle = MiscSec:CreateToggle("Module A (Target)", true, function(state)
            print("Module A is now: " .. tostring(state))
        end)

        MiscSec:CreateButton("Turn OFF Module A", function()
            TestToggle:Set(false) -- This will visibly update the toggle!
            BlueMoonUI:Notify("Code Executed", "Module A turned off via code.", 3)
        end)
        
        -- Welcome Notification
        BlueMoonUI:Notify("Authentication Success", "Welcome back to Blue Moon PRO!", 5)
    end
})
