from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

from plone.registry import field


_ = MessageFactory('plonetheme.ewb_case')


class IEwbCaseThemeSettings(Interface):
    """Global EWB Case Theme settings stored in configuration registry.
    """
    
    second_nav_source = field.TextLine(
            title=_(u"Second Nav Source"),
            required=False
    )
    
    second_nav_label = field.TextLine(
            title=_(u"Second Nav Label"),
            required=False
    )