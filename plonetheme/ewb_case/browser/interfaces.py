from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager

from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope browser layer.
    """


class IThemeView(Interface):
    """ """

    def getColumnsClass():
        """ Returns the CSS class based on columns presence. """


class IPortalTopBar(IViewletManager):
    pass


class ILeftSubBar(IViewletManager):
    pass


class IRightSubBar(IViewletManager):
    pass
