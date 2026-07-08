import re

with open('Example.lua', 'r') as f:
    text = f.read()

# Add Watermark under Window creation
watermark_code = """
-- Watermark Setup
local Watermark = Window:CreateWatermark("Blue Moon Hub | FPS: 0 | Ping: 0ms")
local lastTick = tick()
local frames = 0
RunService.RenderStepped:Connect(function()
    frames = frames + 1
    if tick() - lastTick >= 1 then
        local fps = frames
        local ping = math.floor(LocalPlayer:GetNetworkPing() * 1000)
        local timeStr = os.date("%X")
        Watermark:SetText(string.format("<b>Blue Moon</b> | FPS: %d | Ping: %dms | %s", fps, ping, timeStr))
        frames = 0
        lastTick = tick()
    end
end)
"""
text = text.replace('ToggleKey = Enum.KeyCode.RightShift\n})', 'ToggleKey = Enum.KeyCode.RightShift\n})\n' + watermark_code)

# Replace Rejoin Server
rejoin_code = """UtilitySection:CreateButton("Rejoin Server", function()
    Window:CreateDialog({
        Title = "Rejoin Server",
        Message = "Are you sure you want to leave and rejoin this server? Your current progress might not be saved if you are in combat.",
        Buttons = {
            {
                Name = "Yes, Rejoin",
                Callback = function()
                    if #Players:GetPlayers() <= 1 then
                        LocalPlayer:Kick("\\nRejoining...")
                        task.wait()
                        TeleportService:Teleport(game.PlaceId, LocalPlayer)
                    else
                        TeleportService:TeleportToPlaceInstance(game.PlaceId, game.JobId, LocalPlayer)
                    end
                end
            },
            {
                Name = "Cancel"
            }
        }
    })
end)"""

text = re.sub(r'UtilitySection:CreateButton\("Rejoin Server", function\(\).*?end\)', rejoin_code, text, flags=re.DOTALL)

serverhop_code = """UtilitySection:CreateButton("Server Hop", function()
    Window:CreateDialog({
        Title = "Server Hop",
        Message = "Are you sure you want to find a new server? This will disconnect you from the current session.",
        Buttons = {
            {
                Name = "Hop Server",
                Callback = function()
                    local HttpService = game:GetService("HttpService")
                    local req = request or http_request or (syn and syn.request)
                    if req then
                        local url = "https://games.roblox.com/v1/games/" .. game.PlaceId .. "/servers/Public?sortOrder=Asc&limit=100"
                        local success, res = pcall(function() return req({Url = url, Method = "GET"}) end)
                        if success and res.Body then
                            local data = HttpService:JSONDecode(res.Body)
                            if data and data.data then
                                for _, server in ipairs(data.data) do
                                    if type(server) == "table" and server.id ~= game.JobId and server.playing < server.maxPlayers then
                                        TeleportService:TeleportToPlaceInstance(game.PlaceId, server.id, LocalPlayer)
                                        break
                                    end
                                end
                            end
                        end
                    else
                        K_UI:Notify("Error", "Executor doesn't support request function.", 3)
                    end
                end
            },
            {
                Name = "Cancel"
            }
        }
    })
end)"""
text = re.sub(r'UtilitySection:CreateButton\("Server Hop", function\(\).*?K_UI:Notify.*?end\)\s*end\)', serverhop_code, text, flags=re.DOTALL)

with open('Example.lua', 'w') as f:
    f.write(text)
