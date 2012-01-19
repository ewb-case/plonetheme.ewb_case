from zope.component import getUtility

from plone.registry.interfaces import IRegistry

from plonetheme.ewb_case.interfaces import IEwbCaseThemeSettings


def getDropDownMenuSettings(context):
    """Return Ewb Case Theme settings"""
    registry = getUtility(IRegistry)
    return registry.forInterface(IEwbCaseThemeSettings)


def getNavigationRootPath(context):
    return getDropDownMenuSettings(context).second_nav_source


def getSecondaryNavLabel(context):
    return getDropDownMenuSettings(context).second_nav_label
    