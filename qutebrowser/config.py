config.load_autoconfig()

bg = "#CFD5FF"
bg1 = "#EBEDFF"
text1 = "#5458D4"
text2 = "#CB1A64"
text3 = "#1E202F"


c.colors.tabs.bar.bg = bg

c.colors.tabs.selected.even.bg = bg1
c.colors.tabs.selected.odd.bg = bg1
c.colors.tabs.selected.even.fg = text3
c.colors.tabs.selected.odd.fg = text3

c.colors.tabs.even.bg = bg
c.colors.tabs.odd.bg = bg
c.colors.tabs.even.fg = text1
c.colors.tabs.odd.fg = text1

c.colors.tabs.indicator.start = text2
c.colors.tabs.indicator.stop = text2

c.colors.statusbar.normal.bg = bg1
c.colors.statusbar.normal.fg = text3

c.colors.statusbar.insert.bg = text2
c.colors.statusbar.insert.fg = bg1

c.colors.statusbar.command.bg = bg1
c.colors.statusbar.command.fg = text3

c.colors.completion.category.bg = bg
c.colors.completion.category.fg = text3

c.colors.completion.item.selected.bg = text1
c.colors.completion.item.selected.fg = bg1

c.colors.completion.fg = text3
c.colors.completion.odd.bg = bg
c.colors.completion.even.bg = bg1

c.colors.downloads.bar.bg = bg
c.colors.downloads.start.bg = text1
c.colors.downloads.start.fg = bg1
c.colors.downloads.stop.bg = text2
c.colors.downloads.stop.fg = bg1

c.colors.messages.info.bg = bg1
c.colors.messages.info.fg = text3

c.colors.messages.warning.bg = "#FFD166"
c.colors.messages.warning.fg = "#000000"

c.colors.messages.error.bg = text2
c.colors.messages.error.fg = bg1

c.colors.prompts.bg = bg1
c.colors.prompts.fg = text3
c.tabs.show = "multiple"


c.tabs.title.format = "{audio}{current_title}"
c.fonts.web.size.default = 20

c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

c.auto_save.session = True

c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 9, 'right': 9}
c.tabs.indicator.width = 0 
c.tabs.width = '7%'

#fonts

c.fonts.default_family = []
c.fonts.default_size = '13pt'
c.fonts.web.family.fixed = 'monospace'
c.fonts.web.family.sans_serif = 'monospace'
c.fonts.web.family.serif = 'monospace'
c.fonts.web.family.standard = 'monospace'

# privacy

config.set("content.webgl", False, "*")
config.set("content.canvas_reading", False)
config.set("content.geolocation", False)
config.set("content.webrtc_ip_handling_policy", "default-public-interface-only")
config.set("content.cookies.accept", "all")
config.set("content.cookies.store", True)

# Adblock 
c.content.blocking.enabled = False

# French language 
c.content.headers.accept_language = "fr-FR,fr;q=0.9,en;q=0.8"


# style and cosmetics

c.content.user_stylesheets = [
    "/Users/adonisdulaurent/.qutebrowser/styles/escriptorium.css"
]
