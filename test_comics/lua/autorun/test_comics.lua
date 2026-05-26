COMICS_DATABASE = COMICS_DATABASE or {}

local function RegisterComics()
    if not BuildPages then
        hook.Add("Initialize", "RegisterComics_Retry_" .. debug.getinfo(1, "S").short_src, RegisterComics)
        return
    end

    local function AddComic(id, data)
        COMICS_DATABASE[id] = data
    end

    -- test comic, use that as a base
    AddComic("comic_test_1", { -- THIS IS IMPORTANT! This is the weapon's class, keep it unique, you can name it however you want but try keeping a format, like "comic_<title>_<issue>" etc..
        title = "Test Comic", -- The title is the title of the series, if multiple comics have the same title, they will all be grouped together.
        issue = "Issue 1", -- This is the issue number of the comic, you can call it however you want, but it is recommended to leave the format "Issue 1", "Issue 2", etc..
        author = "Your name here", -- This is the author, explicit.
        icon = "comics/test/issue1/0.jpg", -- This is the icon of the weapon that will be used, it is recommended to leave it at the first one, being the cover.
        pages = BuildPages("comics/test/issue1", 3) -- This controls how many pages there is in the issue (+ the 0 one), simply change the last number to the last page name you have (so for example if the last is 25.png, then put 25)

        -- Add other comics/issues here using the same AddComic(".. base.
    })
end
RegisterComics()