# SPDX-License-Identifier: GPL-2.0-or-later

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QPalette as QP, QColor

themes = [
    ("Light", {
        QP.ColorRole.Window: "#ffefebe7",
        QP.ColorRole.WindowText: "#ff000000",
        QP.ColorRole.Base: "#ffffffff",
        QP.ColorRole.AlternateBase: "#fff7f5f3",
        QP.ColorRole.ToolTipBase: "#ffffffdc",
        QP.ColorRole.ToolTipText: "#ff000000",
        QP.ColorRole.Text: "#ff000000",
        QP.ColorRole.Button: "#ffefebe7",
        QP.ColorRole.ButtonText: "#ff000000",
        QP.ColorRole.BrightText: "#ffffffff",
        QP.ColorRole.Link: "#ff0000ff",
        QP.ColorRole.Highlight: "#ff308cc6",
        QP.ColorRole.HighlightedText: "#ffffffff",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#ffefebe7",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#ffbebebe",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#ffbebebe",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#ffbebebe",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#ffffffff",
    }),
    ("Dark", {
        QP.ColorRole.Window: "#353535",
        QP.ColorRole.WindowText: "#ffffff",
        QP.ColorRole.Base: "#232323",
        QP.ColorRole.AlternateBase: "#353535",
        QP.ColorRole.ToolTipBase: "#191919",
        QP.ColorRole.ToolTipText: "#ffffff",
        QP.ColorRole.Text: "#ffffff",
        QP.ColorRole.Button: "#353535",
        QP.ColorRole.ButtonText: "#ffffff",
        QP.ColorRole.BrightText: "#ff0000",
        QP.ColorRole.Link: "#f7a948",
        QP.ColorRole.Highlight: "#bababa",
        QP.ColorRole.HighlightedText: "#232323",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#353535",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#808080",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#808080",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#808080",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#353535",
    }),
    ("Arc", {
        QP.ColorRole.Window: "#353945",
        QP.ColorRole.WindowText: "#d3dae3",
        QP.ColorRole.Base: "#353945",
        QP.ColorRole.AlternateBase: "#404552",
        QP.ColorRole.ToolTipBase: "#4B5162",
        QP.ColorRole.ToolTipText: "#d3dae3",
        QP.ColorRole.Text: "#d3dae3",
        QP.ColorRole.Button: "#353945",
        QP.ColorRole.ButtonText: "#d3dae3",
        QP.ColorRole.BrightText: "#5294e2",
        QP.ColorRole.Link: "#89b1e0",
        QP.ColorRole.Highlight: "#5294e2",
        QP.ColorRole.HighlightedText: "#d3dae3",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#353945",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#d3dae3",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#d3dae3",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#d3dae3",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#404552",
    }),
    ("Nord", {
        QP.ColorRole.Window: "#2e3440",
        QP.ColorRole.WindowText: "#eceff4",
        QP.ColorRole.Base: "#2e3440",
        QP.ColorRole.AlternateBase: "#434c5e",
        QP.ColorRole.ToolTipBase: "#4c566a",
        QP.ColorRole.ToolTipText: "#eceff4",
        QP.ColorRole.Text: "#eceff4",
        QP.ColorRole.Button: "#2e3440",
        QP.ColorRole.ButtonText: "#eceff4",
        QP.ColorRole.BrightText: "#88c0d0",
        QP.ColorRole.Link: "#88c0d0",
        QP.ColorRole.Highlight: "#88c0d0",
        QP.ColorRole.HighlightedText: "#eceff4",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#2e3440",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#eceff4",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#eceff4",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#eceff4",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#88c0d0",
    }),
    ("Olivia", {
        QP.ColorRole.Window: "#181818",
        QP.ColorRole.WindowText: "#d9d9d9",
        QP.ColorRole.Base: "#181818",
        QP.ColorRole.AlternateBase: "#2c2c2c",
        QP.ColorRole.ToolTipBase: "#363636 ",
        QP.ColorRole.ToolTipText: "#d9d9d9",
        QP.ColorRole.Text: "#d9d9d9",
        QP.ColorRole.Button: "#181818",
        QP.ColorRole.ButtonText: "#d9d9d9",
        QP.ColorRole.BrightText: "#fabcad",
        QP.ColorRole.Link: "#fabcad",
        QP.ColorRole.Highlight: "#fabcad",
        QP.ColorRole.HighlightedText: "#2c2c2c",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#181818",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#d9d9d9",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#d9d9d9",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#d9d9d9",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#fabcad",
    }),
    ("Dracula", {
        QP.ColorRole.Window: "#282a36",
        QP.ColorRole.WindowText: "#f8f8f2",
        QP.ColorRole.Base: "#282a36",
        QP.ColorRole.AlternateBase: "#44475a",
        QP.ColorRole.ToolTipBase: "#6272a4",
        QP.ColorRole.ToolTipText: "#f8f8f2",
        QP.ColorRole.Text: "#f8f8f2",
        QP.ColorRole.Button: "#282a36",
        QP.ColorRole.ButtonText: "#f8f8f2",
        QP.ColorRole.BrightText: "#8be9fd",
        QP.ColorRole.Link: "#8be9fd",
        QP.ColorRole.Highlight: "#8be9fd",
        QP.ColorRole.HighlightedText: "#f8f8f2",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#282a36",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#f8f8f2",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#f8f8f2",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#f8f8f2",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#8be9fd",
    }),
    ("Bliss", {
        QP.ColorRole.Window: "#343434",
        QP.ColorRole.WindowText: "#cbc8c9",
        QP.ColorRole.Base: "#343434",
        QP.ColorRole.AlternateBase: "#3b3b3b",
        QP.ColorRole.ToolTipBase: "#424242",
        QP.ColorRole.ToolTipText: "#cbc8c9",
        QP.ColorRole.Text: "#cbc8c9",
        QP.ColorRole.Button: "#343434",
        QP.ColorRole.ButtonText: "#cbc8c9",
        QP.ColorRole.BrightText: "#f5d1c8",
        QP.ColorRole.Link: "#f5d1c8",
        QP.ColorRole.Highlight: "#f5d1c8",
        QP.ColorRole.HighlightedText: "#424242",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#343434",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#cbc8c9",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#cbc8c9",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#cbc8c9",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#f5d1c8",
    }),
    ("Catppuccin Latte", {
        QP.ColorRole.Window: "#eff1f5",
        QP.ColorRole.WindowText: "#4c4f69",
        QP.ColorRole.Base: "#eff1f5",
        QP.ColorRole.AlternateBase: "#e6e9ef",
        QP.ColorRole.ToolTipBase: "#e6e9ef",
        QP.ColorRole.ToolTipText: "#4c4f69",
        QP.ColorRole.Text: "#4c4f69",
        QP.ColorRole.Button: "#eff1f5",
        QP.ColorRole.ButtonText: "#4c4f69",
        QP.ColorRole.BrightText: "#d20f39",
        QP.ColorRole.Link: "#dd7878",
        QP.ColorRole.Highlight: "#8839ef",
        QP.ColorRole.HighlightedText: "#dce0e8",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#eff1f5",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#8c8fa1",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#8c8fa1",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#8c8fa1",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#ccd0da",
    }),
    ("Catppuccin Frappé", {
        QP.ColorRole.Window: "#303446",
        QP.ColorRole.WindowText: "#c6d0f5",
        QP.ColorRole.Base: "#303446",
        QP.ColorRole.AlternateBase: "#292c3c",
        QP.ColorRole.ToolTipBase: "#292c3c",
        QP.ColorRole.ToolTipText: "#c6d0f5",
        QP.ColorRole.Text: "#c6d0f5",
        QP.ColorRole.Button: "#303446",
        QP.ColorRole.ButtonText: "#c6d0f5",
        QP.ColorRole.BrightText: "#e78284",
        QP.ColorRole.Link: "#eebebe",
        QP.ColorRole.Highlight: "#ca9ee6",
        QP.ColorRole.HighlightedText: "#232634",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#303446",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#838ba7",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#838ba7",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#838ba7",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#414559",
    }),
    ("Catppuccin Macchiato", {
        QP.ColorRole.Window: "#24273a",
        QP.ColorRole.WindowText: "#cad3f5",
        QP.ColorRole.Base: "#24273a",
        QP.ColorRole.AlternateBase: "#1e2030",
        QP.ColorRole.ToolTipBase: "#1e2030",
        QP.ColorRole.ToolTipText: "#cad3f5",
        QP.ColorRole.Text: "#cad3f5",
        QP.ColorRole.Button: "#24273a",
        QP.ColorRole.ButtonText: "#cad3f5",
        QP.ColorRole.BrightText: "#f38ba8",
        QP.ColorRole.Link: "#f0c6c6",
        QP.ColorRole.Highlight: "#c6a0f6",
        QP.ColorRole.HighlightedText: "#181926",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#24273a",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#8087a2",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#8087a2",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#8087a2",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#363a4f",
    }),
    ("Catppuccin Mocha", {
        QP.ColorRole.Window: "#1e1e2e",
        QP.ColorRole.WindowText: "#cdd6f4",
        QP.ColorRole.Base: "#1e1e2e",
        QP.ColorRole.AlternateBase: "#181825",
        QP.ColorRole.ToolTipBase: "#181825",
        QP.ColorRole.ToolTipText: "#cdd6f4",
        QP.ColorRole.Text: "#cdd6f4",
        QP.ColorRole.Button: "#1e1e2e",
        QP.ColorRole.ButtonText: "#cdd6f4",
        QP.ColorRole.BrightText: "#f38ba8",
        QP.ColorRole.Link: "#f2cdcd",
        QP.ColorRole.Highlight: "#cba6f7",
        QP.ColorRole.HighlightedText: "#11111b",
        (QP.ColorGroup.Active, QP.ColorRole.Button): "#1e1e2e",
        (QP.ColorGroup.Disabled, QP.ColorRole.ButtonText): "#7f849c",
        (QP.ColorGroup.Disabled, QP.ColorRole.WindowText): "#7f849c",
        (QP.ColorGroup.Disabled, QP.ColorRole.Text): "#7f849c",
        (QP.ColorGroup.Disabled, QP.ColorRole.Light): "#313244",
    }),
]

palettes = dict()

for name, colors in themes:
    palette = QPalette()
    for role, color in colors.items():
        if not hasattr(role, '__iter__'):
            role = [role]
        palette.setColor(*role, QColor(color))
    palettes[name] = palette


class Theme:

    theme = ""

    @classmethod
    def set_theme(cls, theme):
        cls.theme = theme
        if theme in palettes:
            QApplication.setPalette(palettes[theme])
            QApplication.setStyle("Fusion")
        # For default/system theme, do nothing
        # User will have to restart the application for it to be applied

    @classmethod
    def get_theme(cls):
        return cls.theme

    @classmethod
    def mask_light_factor(cls):
        if cls.theme == "Light":
            return 103
        return 150
