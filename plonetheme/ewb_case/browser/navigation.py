from Products.CMFPlone.browser.navigation import CatalogNavigationTabs

from plonetheme.ewb_case.util import getNavigationRootPath


class SecondaryNavigationTabs(CatalogNavigationTabs):
    def _getNavQuery(self):
        query = super(SecondaryNavigationTabs, self)._getNavQuery()
        navRootPath = getNavigationRootPath(self.context)
        if navRootPath is None or len(navRootPath) == 0:
            query['portal_type'] = []
        else:
            query['path']['query'] = navRootPath
        return query