from plonetheme.ewb_case.tests.base import Themeewb_caseTestCase as TestCase


class Themeewb_caseTestCase(TestCase):

    def test_ewb_case_layers_available(self):
        self.failUnless('ewb_case_images' in self.portal.portal_skins)
        self.failUnless('ewb_case_styles' in self.portal.portal_skins)
        self.failUnless('ewb_case_templates' in self.portal.portal_skins)

    def test_ewb_case_skin_installed(self):
        self.skins = self.portal.portal_skins
        theme = self.skins.getDefaultSkin()
        self.failUnless(theme == 'ewb_case Theme', 'Default theme is %s' % theme)


def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
