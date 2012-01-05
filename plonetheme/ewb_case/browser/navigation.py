from Products.CMFPlone.browser.navigation import CatalogNavigationTabs

from plonetheme.ewb_case.util import getNavigationRootPath


class SecondaryNavigationTabs(CatalogNavigationTabs):
    def _getNavQuery(self):
        query = super(SecondaryNavigationTabs, self)._getNavQuery()
        navRootPath = getNavigationRootPath(self.context)
        if navRootPath is not None:
            query['path']['query'] = navRootPath
        return query