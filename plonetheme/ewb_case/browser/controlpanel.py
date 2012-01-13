from plone.app.registry.browser import controlpanel

from plonetheme.ewb_case.interfaces import IEwbCaseThemeSettings, _


class EwbCaseThemeSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IEwbCaseThemeSettings
    
    label = _(u"Ewb Case Theme settings")
    description = _(u""" """)


class EwbCaseThemeSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = EwbCaseThemeSettingsEditForm