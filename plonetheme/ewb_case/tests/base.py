from zope.component import getUtility

from Testing.ZopeTestCase import Sandboxed

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase.PloneTestCase import installPackage
from Products.Five.testbrowser import Browser
from Products.PloneTestCase import PloneTestCase as ptc

from collective.testcaselayer.ptc import BasePTCLayer, ptc_layer

from plone.registry.interfaces import IRegistry

from plonetheme.ewb_case.interfaces import IEwbCaseThemeSettings


class Layer(BasePTCLayer):
    """ set up basic testing layer """

    def afterSetUp(self):
        # load zcml for this package and its dependencies
        fiveconfigure.debug_mode = True
        from plonetheme import ewb_case
        zcml.load_config('configure.zcml', package=ewb_case)
        fiveconfigure.debug_mode = False
        # after which the required packages can be initialized
        installPackage('plonetheme.ewb_case', quiet=True)
        # finally load the testing profile
        self.addProfile('plonetheme.ewb_case:default')
        
        

layer = Layer(bases=[ptc_layer])

ptc.setupPloneSite()

zcml_string = """\
<configure xmlns="http://namespaces.zope.org/zope"
           xmlns:browser="http://namespaces.zope.org/browser"
           xmlns:plone="http://namespaces.plone.org/plone"
           xmlns:gs="http://namespaces.zope.org/genericsetup"
           package="plonetheme.ewb_case"
           i18n_domain="test">

    <gs:registerProfile
        name="testing"
        title="plonetheme.ewb_case testing"
        description="Used for testing only"
        directory="tests/profiles/testing"
        for="Products.CMFCore.interfaces.ISiteRoot"
        provides="Products.GenericSetup.interfaces.EXTENSION"
        />

</configure>
"""

class Themeewb_caseTestCase(Sandboxed, ptc.PloneTestCase):
    """ Base class used for test cases """

    layer = layer



    
class FunctionalTestCase(ptc.FunctionalTestCase):

    layer = layer

    def getBrowser(self, loggedIn=True):
        """ instantiate and return a testbrowser for convenience """
        browser = Browser()
        if loggedIn:
            user = ptc.default_user
            pwd = ptc.default_password
            browser.addHeader('Authorization', 'Basic %s:%s' % (user, pwd))
        return browser
