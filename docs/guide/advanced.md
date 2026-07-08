# Advanced Features & Modules

Jospy UI is more than just buttons and toggles. It comes with powerful built-in modules and utilities to make your script feel like a true premium product.

## The Library API
When you load the Jospy UI library, you gain access to global utility methods that you can call anywhere in your script.

```lua
local Library = loadstring(game:HttpGet("..."))()

-- Send a notification
Library:Notify("Title", "Message", 3) -- Title, Text, Duration

-- Copy text to user's clipboard securely (handles executor differences)
Library:CopyToClipboard("discord.gg/yourserver")

-- Get the user's executor name and version
local execName, execVersion = Library:GetExecutor()
print("User is using:", execName)
```

---

## Watermark (HUD)

The Watermark API allows you to create a sleek, live-updating bar at the top of the user's screen. This is perfect for displaying FPS, Ping, or the current time. The watermark remains visible even when the main UI is toggled off!

```lua
-- Create the watermark (Returns a Watermark API object)
local Watermark = Window:CreateWatermark("Jospy UI | FPS: 60 | Ping: 20ms")

-- Dynamically update its text later in a loop
RunService.RenderStepped:Connect(function()
    Watermark:SetText("Jospy UI | FPS: " .. getFPS() .. " | Ping: " .. getPing())
end)

-- Toggle visibility
Watermark:SetVisible(false)
```

---

## Modal Dialogs (Popups)

Never let a user accidentally click a dangerous button again. The Dialog API creates a stunning, animated modal popup in the center of the screen, dimming the background until the user makes a choice.

```lua
Window:CreateDialog({
    Title = "Server Hop",
    Message = "Are you sure you want to find a new server? Your current progress will be lost.",
    Buttons = {
        {
            Name = "Yes, Hop",
            Callback = function() 
                print("Hopping to a new server...") 
            end
        },
        {
            Name = "Cancel"
            -- Omitting the callback simply closes the dialog without doing anything
        }
    }
})
```

---

## Configuration Manager (Settings)

Jospy UI features a completely automatic Configuration Manager. It creates a default "Settings" tab in your UI containing buttons to Save, Load, Delete, and Auto-Load profiles.

### How to use it:
You don't need to write any complex saving/loading logic yourself. All you have to do is add a **`Flag`** property to your elements!

```lua
Section:CreateToggle({
    Name = "Aimbot",
    Default = false,
    Flag = "AimbotToggle", -- This is the magic key!
    Callback = function(state) end
})
```

The Config Manager will automatically scan all elements with a `Flag` property, save their values to a JSON file in the executor's `workspace` folder, and restore them when the user clicks "Load". 

If the user enables **"Auto Load"** in the Settings tab, their settings will be instantly restored every time they execute your script!

### Manual Config Control
You can also manually trigger config saves/loads via the Library API if you want to bypass the UI:
```lua
Library:SaveConfig("MyHubFolder", "MyProfile")
Library:LoadConfig("MyHubFolder", "MyProfile")
```
