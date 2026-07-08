# Advanced Features

Jospy UI is more than just buttons and toggles. It comes with powerful built-in utilities to make your script feel like a true premium product.

## Watermark (HUD)

The Watermark API allows you to create a sleek, live-updating bar at the top of the user's screen. This is perfect for displaying FPS, Ping, or the current time. The watermark remains visible even when the main UI is toggled off!

```lua
-- Create the watermark
local Watermark = Window:CreateWatermark("Jospy UI | FPS: 60 | Ping: 20ms")

-- Dynamically update its text later
Watermark:SetText("Jospy UI | FPS: 120 | Ping: 15ms")

-- Toggle visibility
Watermark:SetVisible(false)
```

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
            -- Omitting the callback simply closes the dialog
        }
    }
})
```

## Notifications

Send unobtrusive slide-in notifications to the bottom right of the screen.

```lua
-- Title, Message, Duration (in seconds)
K_UI:Notify("Success", "Aimbot configuration loaded successfully!", 3) 
```

## Configuration Manager (Settings)

Jospy UI features a completely automatic Configuration Manager. It creates a default "Settings" tab in your UI containing buttons to Save, Load, Delete, and Auto-Load profiles.

### How to use it:
You don't need to write any saving/loading logic yourself. All you have to do is add a **`Flag`** property to your elements!

```lua
Section:CreateToggle({
    Name = "Aimbot",
    Default = false,
    Flag = "AimbotToggle", -- This is the magic key!
    Callback = function(state) end
})
```

The Config Manager will automatically scan all elements with a `Flag` property, save their values to a JSON file in the executor's `workspace` folder, and restore them when the user clicks "Load". If the user enables "Auto Load", their settings will be instantly restored every time they execute your script!
