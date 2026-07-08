# Elements & API

Jospy UI provides a wide variety of interactive elements. All elements must be created inside a `Section`.

When you create an interactive element (like a Toggle, Slider, Dropdown), the function **returns an API object**. You can use this API object to manipulate the element later in your script (e.g., changing its value, disabling it, or listening to changes).

> **Note:** If you want an element's value to be saved automatically by the Config Manager, you **must** provide a unique `Flag` property!

---

## Common API Methods
Almost all interactive elements (Toggle, Slider, Dropdown, etc.) return an object containing these common methods:

- `Element.SetValue(value)` : Programmatically changes the value of the element and fires the callback. (Can also be called as `Element.Set(value)`)
- `Element.GetValue()` : Returns the current value of the element.
- `Element.SetVisible(boolean)` : Hides or shows the element.
- `Element.SetDisabled(boolean)` : Disables interactions with the element and grays it out.
- `Element.SetTitle(string)` : Changes the name/title of the element.
- `Element.SetDescription(string)` : Adds or updates the tooltip description of the element.
- `Element.OnChanged(function)` : Appends an additional callback function that fires when the value changes.

---

## Button

A simple clickable button. It features a tactile click sound effect.

```lua
local MyButton = Section:CreateButton({
    Name = "Kill All",
    Tooltip = "Kills all players in the game", -- Optional
    Callback = function()
        print("Action executed!")
    end
})

-- Button specific methods:
MyButton.SetTitle("New Button Name")
MyButton.SetVisible(false)
```

## Toggle

A switch that can be turned on or off.

```lua
local AimbotToggle = Section:CreateToggle({
    Name = "Aimbot",
    Default = false,
    Flag = "AimbotToggle", 
    Callback = function(state)
        print("Aimbot is now:", state)
    end
})

-- Updating the toggle programmatically
AimbotToggle.SetValue(true) -- Turns it on
print(AimbotToggle.GetValue()) -- Returns true
```

## Slider

A draggable slider for selecting numeric values.

```lua
local SpeedSlider = Section:CreateSlider({
    Name = "WalkSpeed",
    Min = 16,
    Max = 100,
    Default = 16,
    Flag = "WS_Slider",
    Callback = function(value)
        game.Players.LocalPlayer.Character.Humanoid.WalkSpeed = value
    end
})

-- Changing slider value via script
SpeedSlider.SetValue(50)
SpeedSlider.SetDisabled(true) -- Locks the slider
```

## Dropdown

A single-selection dropdown menu. Can be searchable.

```lua
local TargetDrop = Section:CreateDropdown({
    Name = "Target Part",
    Options = {"Head", "Torso", "Legs"},
    Default = "Head",
    Flag = "TargetDropdown",
    Searchable = true,
    Callback = function(value)
        print("Target set to:", value)
    end
})

-- Dropdown specific methods:
TargetDrop.SetOptions({"Left Arm", "Right Arm"}) -- Updates the list of options!
TargetDrop.SetValue("Torso")
```

## Multi-Dropdown

Similar to a Dropdown, but allows selecting multiple options simultaneously. The callback returns a table of selected values.

```lua
local ESPDrop = Section:CreateMultiDropdown({
    Name = "ESP Options",
    Options = {"Boxes", "Names", "Tracers"},
    Default = {"Boxes"},
    Flag = "ESPDropdown",
    Searchable = true,
    Callback = function(values)
        -- 'values' is a dictionary: { ["Boxes"] = true, ["Names"] = false, ... }
        for k, v in pairs(values) do 
            if v then print(k, "is selected") end 
        end
    end
})

-- Changing multiple selections
ESPDrop.SetValue({"Names", "Tracers"})
ESPDrop.SetOptions({"Chams", "Skeleton", "HealthBar"})
```

## ColorPicker

A sleek RGB color picker.

```lua
local ChamsColor = Section:CreateColorPicker({
    Name = "ESP Color",
    Default = Color3.fromRGB(255, 0, 0),
    Flag = "ESPColor",
    Callback = function(color)
        print("New color selected!", color)
    end
})

-- Setting color programmatically
ChamsColor.SetValue(Color3.fromRGB(0, 255, 0))
```

## Keybind

Allows users to map a specific action to a keyboard key.

```lua
local FlyKey = Section:CreateKeybind({
    Name = "Fly Toggle Key",
    Default = Enum.KeyCode.F,
    Flag = "FlyKey",
    OnBind = function(key)
        print("Key changed to:", key.Name)
    end
})

-- Changing the bind via script
FlyKey.SetValue(Enum.KeyCode.Q)
```

## TextBox

An input field for the user to type text.

```lua
local UserBox = Section:CreateTextBox({
    Name = "Custom Username",
    Placeholder = "Type here...",
    Flag = "UsernameBox",
    Callback = function(text)
        print("Typed:", text)
    end
})

UserBox.SetValue("NewText")
```

## Info Label

A simple text label for displaying information or instructions. *Info labels do not return an API object.*

```lua
Section:CreateInfo("Information", "This is a simple text label for giving users instructions.")
```
