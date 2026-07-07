-- Require the module from GitHub using loadstring
local BlueMoonUI = loadstring(game:HttpGet("https://raw.githubusercontent.com/GeceUstasi/BlueMoonUI/master/BlueMoonUI.lua"))()

-- Create the main window
local Window = BlueMoonUI:CreateWindow({
    Title = "Blue Moon",
    Version = "v1.1.2 Alpha",
    ProfileName = "XxGECEUSTASIxX",
    Ping = "106 ms"
})

-- Create Tabs with specific icon IDs
local InfoTab = Window:CreateTab("Info", "") -- No icon needed for info if it was just a header, but it's a tab here.
local FarmTab = Window:CreateTab("Farm", BlueMoonUI.Icons.Farm)
local FishingTab = Window:CreateTab("Fishing", BlueMoonUI.Icons.Fishing)
local MicrowaveTab = Window:CreateTab("Microwave", BlueMoonUI.Icons.Microwave)
local PlayerTab = Window:CreateTab("Player", BlueMoonUI.Icons.Player)
local TeleportsTab = Window:CreateTab("Teleports", BlueMoonUI.Icons.Teleports)
local OtherTab = Window:CreateTab("Other", BlueMoonUI.Icons.Other)

-- Populate the 'Farm' Tab (as seen in the provided image)
local AutoDigSection = FarmTab:CreateSection("Auto Dig")

AutoDigSection:CreateDropdown("Select Dig Tool", {"None", "Shovel", "Pickaxe"}, "None", function(selected)
    print("Selected Dig Tool: " .. selected)
end)

AutoDigSection:CreateSeparator()

AutoDigSection:CreateToggle("Auto Dig", false, function(state)
    print("Auto Dig state: " .. tostring(state))
end)

AutoDigSection:CreateToggle("Play Animation", false, function(state)
    print("Play Animation state: " .. tostring(state))
end)

local SellingSection = FarmTab:CreateSection("Selling")

SellingSection:CreateToggle("Auto Sell Trash", true, function(state)
    print("Auto Sell Trash state: " .. tostring(state))
end)

SellingSection:CreateButton("Manual Sell All Trash", function()
    print("Manual Sell All Trash clicked!")
end)

-- The exact info box at the bottom of the section
SellingSection:CreateInfo("Info", "Always keep Disable AFK Animation ON for Auto Sell when you are afking.\n\nThese functions use teleportation to the point of sale.\nBe careful and use at your own risk.")
