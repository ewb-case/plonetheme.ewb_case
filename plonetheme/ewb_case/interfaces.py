from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

from plone.registry import field


_ = MessageFactory('plonetheme.ewb_case')


class IEwbCaseThemeSettings(Interface):
    """Global EWB Case Theme settings stored in configuration registry.
    """
    
    second_nav_source = field.Id(
            title=_(u"Second Nav Source"),
            required=False
    )