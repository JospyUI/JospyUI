# Getting Started

Welcome to **Jospy UI**, a premium library designed to give your Roblox exploits a modern, sleek, and interactive feel.

## Booting the Library

To load Jospy UI into your script, use the following `loadstring`. Make sure to store the result in a variable so you can use its functions!

```lua
local K_UI = loadstring(game:HttpGet("https://raw.githubusercontent.com/JospyUI/JospyUI/master/K-UI.lua"))()
```

## Creating a Window

Once the library is loaded, you can create your main Hub window. 

```lua
local Window = K_UI:CreateWindow("My Hub Name", {
    Accent = Color3.fromRGB(114, 137, 218), -- Primary theme color (Blurple)
    Ping = true, -- Displays ping/fps in the header
    ToggleKey = Enum.KeyCode.RightShift -- Key to hide/show the UI
})
```

## Creating Tabs

Jospy UI uses a clean tab system. You can create as many tabs as you like. We highly recommend using [Lucide Icons](https://lucide.dev/icons/) for the best look!

```lua
local MainTab = Window:CreateTab("Main", K_UI.GetIcon("lucide-home"))
local CombatTab = Window:CreateTab("Combat", K_UI.GetIcon("lucide-crosshair"))
local VisualsTab = Window:CreateTab("Visuals", K_UI.GetIcon("lucide-eye"))
local MiscTab = Window:CreateTab("Misc", K_UI.GetIcon("lucide-folder-open"))
```

## Creating Sections

Inside each tab, you can create sections to group your elements together logically.

```lua
local PlayerSection = MainTab:CreateSection("LocalPlayer")
local WeaponSection = CombatTab:CreateSection("Weapons")
```

Once you have your Sections set up, you can start adding Elements! Check out the [Elements Guide](./elements.md) to see what you can build.
