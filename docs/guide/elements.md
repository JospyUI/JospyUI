# Elements

Jospy UI provides a wide variety of interactive elements. All elements must be created inside a `Section`.

> **Note:** If you want an element's value to be saved automatically by the Config Manager, you **must** provide a unique `Flag` property!

## Button

A simple clickable button. It features a tactile click sound effect.

```lua
Section:CreateButton("Kill All", function()
    print("Action executed!")
end)
```

## Toggle

A switch that can be turned on or off. Plays a high-pitch sound when turned on, and a low-pitch sound when turned off.

```lua
Section:CreateToggle({
    Name = "Aimbot",
    Default = false,
    Flag = "AimbotToggle", 
    Callback = function(state)
        print("Aimbot is now:", state)
    end
})
```

## Slider

A draggable slider for selecting numeric values.

```lua
Section:CreateSlider({
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

## Dropdown

A searchable dropdown menu.

```lua
Section:CreateDropdown({
    Name = "Target Part",
    Options = {"Head", "Torso", "Legs"},
    Default = "Head",
    Flag = "TargetDropdown",
    Searchable = true,
    Callback = function(value)
        print("Target set to:", value)
    end
})
```

## Multi-Dropdown

Similar to a Dropdown, but allows selecting multiple options simultaneously. The callback returns a table of selected values.

```lua
Section:CreateDropdown({
    Name = "ESP Options",
    Options = {"Boxes", "Names", "Tracers"},
    Default = {"Boxes"},
    Flag = "ESPDropdown",
    Multi = true,
    Callback = function(values)
        for _, v in ipairs(values) do print(v) end
    end
})
```

## ColorPicker

A sleek RGB color picker.

```lua
Section:CreateColorPicker({
    Name = "ESP Color",
    Default = Color3.fromRGB(255, 0, 0),
    Flag = "ESPColor",
    Callback = function(color)
        print("New color selected!", color)
    end
})
```

## Keybind

Allows users to map a specific action to a keyboard key.

```lua
Section:CreateKeybind({
    Name = "Fly Toggle Key",
    Default = Enum.KeyCode.F,
    Flag = "FlyKey",
    OnBind = function(key)
        print("Key changed to:", key.Name)
    end
})
```

## TextBox

An input field for the user to type text.

```lua
Section:CreateTextBox({
    Name = "Custom Username",
    Placeholder = "Type here...",
    Flag = "UsernameBox",
    Callback = function(text)
        print("Typed:", text)
    end
})
```

## Info Label

A simple text label for displaying information or instructions.

```lua
Section:CreateInfo("Information", "This is a simple text label for giving users instructions.")
```
