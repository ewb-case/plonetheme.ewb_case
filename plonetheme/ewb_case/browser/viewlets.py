from zope.component import getMultiAdapter

from Acquisition import aq_base, aq_inner

from plone.app.layout.viewlets.common import GlobalSectionsViewlet


class SecondaryNav(GlobalSectionsViewlet):
    
    def update(self):
        context = aq_inner(self.context)
        portal_tabs_view = getMultiAdapter((context, self.request),
                                               name='plonetheme.ewb_case.secondary_tabs_view')
        self.portal_tabs = portal_tabs_view.topLevelTabs()
    
        self.selected_tabs = self.selectedTabs(portal_tabs=self.portal_tabs)
        self.selected_portal_tab = self.selected_tabs['portal']

