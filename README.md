<div align="center">
  <h1>🌑 Jospy UI Library</h1>
  <p>A premium, modern, and highly customizable UI library for Roblox exploit scripts.</p>
</div>

## ✨ Features
- 🎨 **Modern Design:** Clean, sleek interface with smooth animations and rounded corners.
- 📦 **Built-in Config Manager:** Automatically save, load, and auto-execute user preferences!
- 🔊 **Sound Effects:** Tactile audio feedback for hover, clicks, and toggles.
- 🔔 **Notifications & Dialogs:** Stunning slide-in notifications and interactive confirmation popups.
- 🧩 **Rich Elements:** Includes Buttons, Toggles, Sliders, Dropdowns, Multi-Dropdowns, ColorPickers, and Keybinds.
- 💧 **Lucide Icons:** Beautiful, consistent iconography for all tabs and core UI elements.

## 🚀 Booting the Library
```lua
local K_UI = loadstring(game:HttpGet("https://raw.githubusercontent.com/ijosephyusufk-dev/JospyUI/master/K-UI.lua"))()
```

## 🪟 Creating a Window
```lua
local Window = K_UI:CreateWindow("My Hub Name", {
    Accent = Color3.fromRGB(114, 137, 218), -- Primary theme color
    Ping = true, -- Displays ping/fps in header (optional)
    ToggleKey = Enum.KeyCode.RightShift -- Key to hide/show the UI
})
```

## 📑 Creating Tabs & Sections
```lua
local MainTab = Window:CreateTab("Main", K_UI.GetIcon("lucide-home"))
local CombatSection = MainTab:CreateSection("Combat")
```

## 🛠️ Elements

### Button
```lua
CombatSection:CreateButton("Kill All", function()
    print("Action executed!")
end)
```

### Toggle
```lua
CombatSection:CreateToggle({
    Name = "Aimbot",
    Default = false,
    Flag = "AimbotToggle", -- Needed for the Config system!
    Callback = function(state)
        print("Aimbot is now:", state)
    end
})
```

### Slider
```lua
CombatSection:CreateSlider({
    Name = "WalkSpeed",
    Min = 16,
    Max = 100,
    Default = 16,
    Flag = "WS_Slider",
    Callback = function(value)
        game.Players.LocalPlayer.Character.Humanoid.WalkSpeed = value
    end
})
```

### Dropdown (Single & Multi)
```lua
CombatSection:CreateDropdown({
    Name = "Target Part",
    Options = {"Head", "Torso", "Legs"},
    Default = "Head",
    Flag = "TargetDropdown",
    Searchable = true,
    Callback = function(value)
        print("Target set to:", value)
    end
})

-- Multi Dropdown
CombatSection:CreateDropdown({
    Name = "ESP Options",
    Options = {"Boxes", "Names", "Tracers"},
    Default = {"Boxes"},
    Flag = "ESPDropdown",
    Multi = true,
    Callback = function(values)
        -- values is a table!
        for _, v in ipairs(values) do print(v) end
    end
})
```

### ColorPicker
```lua
CombatSection:CreateColorPicker({
    Name = "ESP Color",
    Default = Color3.fromRGB(255, 0, 0),
    Flag = "ESPColor",
    Callback = function(color)
        print("New color selected!", color)
    end
})
```

### Keybind
```lua
CombatSection:CreateKeybind({
    Name = "Fly Toggle Key",
    Default = Enum.KeyCode.F,
    Flag = "FlyKey",
    OnBind = function(key)
        print("Key changed to:", key.Name)
    end
})
```

### TextBox & Label
```lua
CombatSection:CreateTextBox({
    Name = "Custom Username",
    Placeholder = "Type here...",
    Flag = "UsernameBox",
    Callback = function(text)
        print("Typed:", text)
    end
})

CombatSection:CreateInfo("Information", "This is a simple text label for giving users instructions.")
```

## 💎 Advanced Features

### Watermark (HUD)
Creates a live-updating bar at the top of the screen.
```lua
local Watermark = Window:CreateWatermark("Jospy UI | FPS: 60")
-- You can dynamically update it:
Watermark:SetText("Jospy UI | FPS: 120")
```

### Dialogs (Popups)
Confirm critical actions with a modal dialog!
```lua
Window:CreateDialog({
    Title = "Warning",
    Message = "Are you sure you want to clear all data?",
    Buttons = {
        {
            Name = "Yes",
            Callback = function() print("Cleared!") end
        },
        {
            Name = "Cancel"
        }
    }
})
```

### Notifications
```lua
K_UI:Notify("Success", "Loaded successfully!", 3) -- Title, Message, Duration (seconds)
```

## ⚙️ Configuration Manager
Jospy UI comes with a built-in configuration manager located in the **Settings** tab. As long as you provide a `Flag = "String"` property to your elements (Toggles, Sliders, Dropdowns, etc.), the Config Manager will automatically handle saving, loading, deleting, and auto-executing user profiles without writing a single line of extra code!
