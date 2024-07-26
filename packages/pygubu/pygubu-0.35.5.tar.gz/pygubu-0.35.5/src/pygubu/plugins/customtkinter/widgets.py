import customtkinter as ctk
import pygubu.plugins.customtkinter.tabview
import pygubu.plugins.customtkinter.scrollableframe

from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
    register_custom_property,
)
from pygubu.i18n import _
from pygubu.utils.datatrans import ListDTO
from pygubu.plugins.tk.tkstdwidgets import TKCanvas as TKCanvasBO

from ..customtkinter import _designer_tab_label, _plugin_uid
from .ctkbase import (
    CTkBaseMixin,
    GCONTAINER,
    GDISPLAY,
    GINPUT,
)


class CTkFrameBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkFrame
    container = True
    container_layout = True
    properties = (
        "width",
        "height",
        "corner_radius",
        "border_width",
        "bg_color",
        "fg_color",
        "border_color",
        "background_corner_colors",
    )


_builder_uid = f"{_plugin_uid}.CTkFrame"
register_widget(
    _builder_uid,
    CTkFrameBO,
    "CTkFrame",
    ("ttk", _designer_tab_label),
    group=GCONTAINER,
)


class CTkLabelBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkLabel
    properties = (
        "anchor",
        "compound",
        "cursor",
        "image",
        "justify",
        "font",
        "height",
        "padx",
        "pady",
        "state",
        "takefocus",
        "text",
        "textvariable",
        "underline",
        "width",
        # CTK properties
        "corner_radius",
        "bg_color",
        "fg_color",
        "text_color",
        "text_color_disabled",
        "border_color",
        "border_width",
    )


_builder_uid = f"{_plugin_uid}.CTkLabel"
register_widget(
    _builder_uid,
    CTkLabelBO,
    "CTkLabel",
    ("ttk", _designer_tab_label),
    group=GDISPLAY,
)


class CTkProgressBarBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkProgressBar
    allow_bindings = False
    properties = (
        "width",
        "height",
        "variable",
        "mode",
        "orientation",
        # CTK properties
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "corner_radius",
        "progress_color",
        "determinate_speed",
        "indeterminate_speed",
    )
    ro_properties = ("orientation",)


_builder_uid = f"{_plugin_uid}.CTkProgressBar"
register_widget(
    _builder_uid,
    CTkProgressBarBO,
    "CTkProgressBar",
    ("ttk", _designer_tab_label),
    group=GDISPLAY,
)

register_custom_property(
    _builder_uid,
    "variable",
    "tkvarentry",
    type_choices=("int", "double"),
    type_default="int",
)


class CTkButtonBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkButton
    allow_bindings = False
    properties = (
        "text",
        "width",
        "height",
        "textvariable",
        "image",
        "compound",
        "state",
        "command",
        # CTK properties
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "border_spacing",
        "corner_radius",
        "hover_color",
        "text_color",
        "text_color_disabled",
        "hover",
        "font",
        "background_corner_colors",
        "round_width_to_even_numbers",
        "round_height_to_even_numbers",
        "anchor",
    )
    command_properties = ("command",)
    ro_properties = ("hover",)


_builder_uid = f"{_plugin_uid}.CTkButton"
register_widget(
    _builder_uid,
    CTkButtonBO,
    "CTkButton",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)


class CTkSliderBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkSlider
    allow_bindings = False
    properties = (
        "width",
        "height",
        "variable",
        "from_",
        "to",
        "command",
        "state",
        # CTK properties
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "corner_radius",
        "progress_color",
        "button_color",
        "button_hover_color",
        "button_corner_radius",
        "button_length",
        "number_of_steps",
        "orientation",
    )
    command_properties = ("command",)
    ro_properties = (
        "orientation",
        "button_length",
    )

    def _code_define_callback_args(self, cmd_pname, cmd):
        return ("value",)


_builder_uid = f"{_plugin_uid}.CTkSlider"
register_widget(
    _builder_uid,
    CTkSliderBO,
    "CTkSlider",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)

register_custom_property(
    _builder_uid,
    "variable",
    "tkvarentry",
    type_choices=("int", "double"),
    type_default="int",
)


class CTkEntryBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkEntry
    allow_bindings = False
    properties = (
        "borderwidth",
        "cursor",
        "exportselection",
        "font",
        "insertborderwidth",
        "insertofftime",
        "insertontime",
        "insertwidth",
        "justify",
        "selectborderwidth",
        "takefocus",
        "textvariable",
        "xscrollcommand",
        # specific
        "invalidcommand",
        "readonlybackground",
        "show",
        "state",
        "validate",
        "validatecommand",
        "width",
        # custom
        "text",
        # CTK options
        "bg_color",
        "fg_color",
        "border_color",
        "border_width",
        "corner_radius",
        "text_color",
        "placeholder_text_color",
        "placeholder_text",
    )

    def _set_property(self, target_widget, pname, value):
        if pname == "text":
            target_widget.delete(0, "end")
            target_widget.insert(0, value)
        else:
            super()._set_property(target_widget, pname, value)

    def _code_set_property(self, targetid, pname, value, code_bag):
        if pname == "text":
            sval = self.builder.code_translate_str(value)
            lines = [
                f"""{targetid}.delete(0, "end")""",
                f"{targetid}.insert(0, {sval})",
            ]
            code_bag[pname] = lines
        else:
            super()._code_set_property(targetid, pname, value, code_bag)


_builder_uid = f"{_plugin_uid}.CTkEntry"
register_widget(
    _builder_uid,
    CTkEntryBO,
    "CTkEntry",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)


_list_dto = ListDTO()


class CTkOptionMenuBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkOptionMenu
    allow_bindings = False
    properties = (
        "command",
        "variable",
        "values",
        "bg_color",
        "fg_color",
        "button_color",
        "button_hover_color",
        "text_color",
        "text_color_disabled",
        "dropdown_hover_color",
        "dropdown_text_color",
        "dropdown_color",
        "dropdown_font",
        "width",
        "height",
        "corner_radius",
        "state",
        "dynamic_resizing",
        "font",
    )
    command_properties = ("command",)

    def _process_property_value(self, pname, value):
        if pname == "values":
            return _list_dto.transform(value)
        return super()._process_property_value(pname, value)

    def _code_define_callback_args(self, cmd_pname, cmd):
        return ("current_value",)

    def _code_process_property_value(self, targetid, pname, value: str):
        if pname == "values":
            return super()._process_property_value(pname, value)
        return super()._code_process_property_value(targetid, pname, value)


_builder_uid = f"{_plugin_uid}.CTkOptionMenu"
_ctk_values_help = _(
    "Specifies the list of values to display. "
    "In code you can pass any iterable. "
    'In Designer, a json like list: ["item1", "item2"]'
)
register_widget(
    _builder_uid,
    CTkOptionMenuBO,
    "CTkOptionMenu",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)
register_custom_property(_builder_uid, "values", "entry", help=_ctk_values_help)
register_custom_property(
    _builder_uid,
    "state",
    "choice",
    values=("", "normal", "disabled", "readonly"),
    state="readonly",
)


class CTkComboBoxBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkComboBox
    allow_bindings = False
    properties = (
        "corner_radius",
        "border_width",
        "bg_color",
        "fg_color",
        "border_color",
        "button_color",
        "button_hover_color",
        "dropdown_fg_color",
        "dropdown_hover_color",
        "dropdown_text_color",
        "text_color",
        "text_color_disabled",
        "font",
        "dropdown_font",
        "command",
        "variable",
        "values",
        "width",
        "height",
        "state",
        "hover",
    )
    command_properties = ("command",)
    ro_properties = ("hover",)

    def _process_property_value(self, pname, value):
        if pname == "values":
            return _list_dto.transform(value)
        return super()._process_property_value(pname, value)

    def _code_define_callback_args(self, cmd_pname, cmd):
        return ("value",)

    def _code_process_property_value(self, targetid, pname, value: str):
        if pname == "values":
            return super()._process_property_value(pname, value)
        return super()._code_process_property_value(targetid, pname, value)


_builder_uid = f"{_plugin_uid}.CTkComboBox"
register_widget(
    _builder_uid,
    CTkComboBoxBO,
    "CTkComboBox",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)
register_custom_property(_builder_uid, "values", "entry", help=_ctk_values_help)
register_custom_property(
    _builder_uid,
    "state",
    "choice",
    values=("", "normal", "disabled", "readonly"),
    state="readonly",
)


class CTkCheckBoxBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkCheckBox
    allow_bindings = False
    properties = (
        "width",
        "height",
        "checkbox_width",
        "checkbox_height",
        "corner_radius",
        "border_width",
        "bg_color",
        "fg_color",
        "hover_color",
        "border_color",
        "checkmark_color",
        "text_color",
        "text_color_disabled",
        "text",
        "font",
        "textvariable",
        "state",
        "hover",
        "command",
        "onvalue",
        "offvalue",
        "variable",
    )
    command_properties = ("command",)
    ro_properties = ("hover", "onvalue", "offvalue")


_builder_uid = f"{_plugin_uid}.CTkCheckBox"
register_widget(
    _builder_uid,
    CTkCheckBoxBO,
    "CTkCheckBox",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)


class CTkRadioButtonBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkRadioButton
    allow_bindings = False
    properties = (
        "width",
        "height",
        "radiobutton_width",
        "radiobutton_height",
        "corner_radius",
        "border_width_unchecked",
        "border_width_checked",
        "bg_color",
        "fg_color",
        "hover_color",
        "border_color",
        "text_color",
        "text_color_disabled",
        "text",
        "font",
        "textvariable",
        "variable",
        "value",
        "state",
        "hover",
        "command",
    )
    command_properties = ("command",)
    ro_properties = ("hover", "value")


_builder_uid = f"{_plugin_uid}.CTkRadioButton"
register_widget(
    _builder_uid,
    CTkRadioButtonBO,
    "CTkRadioButton",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)


class CTkSwitchBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkSwitch
    allow_bindings = False
    properties = (
        "width",
        "height",
        "switch_width",
        "switch_height",
        "corner_radius",
        "border_width",
        "button_length",
        "bg_color",
        "fg_color",
        "border_color",
        "progress_color",
        "button_color",
        "button_hover_color",
        "text_color",
        "text_color_disabled",
        "text",
        "font",
        "textvariable",
        "onvalue",
        "offvalue",
        "variable",
        "hover",
        "command",
        "state",
    )
    command_properties = ("command",)
    ro_properties = (
        "onvalue",
        "offvalue",
        "hover",
        "text_color",
        "text_color_disabled",
    )


_builder_uid = f"{_plugin_uid}.CTkSwitch"
register_widget(
    _builder_uid,
    CTkSwitchBO,
    "CTkSwitch",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)


class CTkTextboxBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkTextbox
    properties = (
        "autoseparators",
        "cursor",
        "exportselection",
        "insertborderwidth",
        "insertofftime",
        "insertontime",
        "insertwidth",
        "maxundo",
        "padx",
        "pady",
        "selectborderwidth",
        "spacing1",
        "spacing2",
        "spacing3",
        "state",
        "tabs",
        "takefocus",
        "undo",
        "wrap",
        # ctk
        "width",
        "height",
        "corner_radius",
        "border_width",
        "border_spacing",
        "bg_color",
        "fg_color",
        "border_color",
        "text_color",
        "font",
        "scrollbar_button_color",
        "scrollbar_button_hover_color",
        "activate_scrollbars",
        # custom
        "text",
    )

    def _set_property(self, target_widget, pname, value):
        if pname == "text":
            target_widget = target_widget._textbox
            state = target_widget.cget("state")
            if state == ctk.DISABLED:
                target_widget.configure(state=ctk.NORMAL)
                target_widget.insert("0.0", value)
                target_widget.configure(state=ctk.DISABLED)
            else:
                target_widget.insert("0.0", value)
        else:
            super()._set_property(target_widget, pname, value)

    def _code_set_property(self, targetid, pname, value, code_bag):
        if pname == "text":
            state_value = ""
            if "state" in self.wmeta.properties:
                state_value = self.wmeta.properties["state"]
            sval = self.builder.code_translate_str(value)
            lines = [
                f"_text_ = {sval}",
            ]
            if state_value == ctk.DISABLED:
                lines.extend(
                    (
                        f'{targetid}.configure(state="normal")',
                        f'{targetid}.insert("0.0", _text_)',
                        f'{targetid}.configure(state="disabled")',
                    )
                )
            else:
                lines.append(f'{targetid}.insert("0.0", _text_)')
            code_bag[pname] = lines
        else:
            super()._code_set_property(targetid, pname, value, code_bag)


_builder_uid = f"{_plugin_uid}.CTkTextbox"
register_widget(
    _builder_uid,
    CTkTextboxBO,
    "CTkTextbox",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)

register_custom_property(
    _builder_uid,
    "wrap",
    "choice",
    values=("", ctk.CHAR, ctk.WORD, ctk.NONE),
    state="readonly",
)


class CTkScrollbarBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkScrollbar
    properties = (
        "width",
        "height",
        "orientation",
        "command",
        # CTK
        "cursor",
        "corner_radius",
        "border_spacing",
        "minimum_pixel_length",
        "bg_color",
        "fg_color",
        "button_color",
        "button_hover_color",
        "hover",
    )
    ro_properties = ("orientation", "cursor")
    command_properties = ("command",)


_builder_uid = f"{_plugin_uid}.CTkScrollbar"
register_widget(
    _builder_uid,
    CTkScrollbarBO,
    "CTkScrollbar",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)

register_custom_property(
    _builder_uid,
    "orientation",
    "choice",
    values=("vertical", "horizontal"),
    state="readonly",
    default_value="vertical",
)
register_custom_property(
    _builder_uid,
    "command",
    "scrollcommandentry",
)


class CTkSegmentedButtonBO(CTkBaseMixin, BuilderObject):
    class_ = ctk.CTkSegmentedButton
    allow_bindings = False
    properties = (
        "width",
        "height",
        "corner_radius",
        "border_width",
        "bg_color",
        "fg_color",
        "selected_color",
        "selected_hover_color",
        "unselected_color",
        "unselected_hover_color",
        "text_color",
        "text_color_disabled",
        "background_corner_colors",
        "font",
        "values",
        "variable",
        "dynamic_resizing",
        "command",
        "state",
    )
    command_properties = ("command",)
    ro_properties = ("hover",)

    def _process_property_value(self, pname, value):
        if pname == "values":
            return _list_dto.transform(value)
        return super()._process_property_value(pname, value)

    def _code_define_callback_args(self, cmd_pname, cmd):
        return ("current_value",)

    def _code_process_property_value(self, targetid, pname, value: str):
        if pname == "values":
            return super()._process_property_value(pname, value)
        return super()._code_process_property_value(targetid, pname, value)


_builder_uid = f"{_plugin_uid}.CTkSegmentedButton"
register_widget(
    _builder_uid,
    CTkSegmentedButtonBO,
    "CTkSegmentedButton",
    ("ttk", _designer_tab_label),
    group=GINPUT,
)

register_custom_property(_builder_uid, "values", "entry", help=_ctk_values_help)


class CTkCanvasBO(TKCanvasBO):
    class_ = ctk.CTkCanvas


_builder_uid = f"{_plugin_uid}.CTkCanvas"
register_widget(
    _builder_uid,
    CTkCanvasBO,
    "CTkCanvas",
    ("ttk", _designer_tab_label),
    group=GDISPLAY,
)
