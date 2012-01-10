from zope.component import getMultiAdapter

from Acquisition import aq_inner

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import GlobalSectionsViewlet

from plonetheme.ewb_case.util import getSecondaryNavLabel


class PrimarySectionsViewlet(GlobalSectionsViewlet):
    """Viewlet for the primary navigation tabs.
    """
    
    index = ViewPageTemplateFile('templates/sections.pt')


class SecondarySectionsViewlet(GlobalSectionsViewlet):
    """Viewlet for secondary navigation tabs.
    """
    
    index = ViewPageTemplateFile('templates/labeled_sections.pt')
    
    def update(self):
        context = aq_inner(self.context)
        portal_tabs_view = getMultiAdapter((context, self.request),
                                               name='plonetheme.ewb_case.secondary_tabs_view')
        self.portal_tabs = portal_tabs_view.topLevelTabs()
    
        self.selected_tabs = self.selectedTabs(portal_tabs=self.portal_tabs)
        self.selected_portal_tab = self.selected_tabs['portal']
        self.sections_label = getSecondaryNavLabel(context)
        


