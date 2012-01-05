from zope.interface import Interface

from plone.theme.interfaces import IDefaultPloneLayer

from zope.viewlet.interfaces import IViewletManager


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope browser layer.
    """

class IThemeView(Interface):
    """ """

    def getColumnsClass():
        """ Returns the CSS class based on columns presence. """



class IPortalTabs(IViewletManager):
    pass