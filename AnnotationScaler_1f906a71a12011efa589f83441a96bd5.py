"""


:author: Alexander Castronovo
:contact: 
:email: alexander.castronovo@mpfi.org
:organization: 
:address: 
:copyright: 
:date: Nov 12 2024 13:01
:dragonflyVersion: 2024.1.0.1601
:UUID: 1f906a71a12011efa589f83441a96bd5
"""

__version__ = '1.0.0'

from ORSServiceClass.OrsPlugin.orsPlugin import OrsPlugin
from ORSServiceClass.OrsPlugin.uidescriptor import UIDescriptor
from ORSServiceClass.actionAndMenu.menu import Menu
from ORSServiceClass.decorators.infrastructure import menuItem


class AnnotationScaler_1f906a71a12011efa589f83441a96bd5(OrsPlugin):

    # Plugin definition
    multiple = True
    savable = False
    keepAlive = False
    canBeGenericallyOpened = False

    # UIs
    UIDescriptors = [UIDescriptor(name='MainFormAnnotationscaler',
                                  title='Annotation Scaler',
                                  dock='Floating',
                                  tab='Main',
                                  modal=False,
                                  collapsible=True,
                                  floatable=True)]

    def __init__(self, varname=None):
        super().__init__(varname)

    @classmethod
    def getMainFormName(cls):
        return 'MainFormAnnotationscaler'

    @classmethod
    def getMainFormClass(cls):
        from .mainformannotationscaler import MainFormAnnotationscaler
        return MainFormAnnotationscaler

    @classmethod
    def openGUI(cls):
        instance = AnnotationScaler_1f906a71a12011efa589f83441a96bd5()

        if instance is not None:
            instance.openWidget("MainFormAnnotationscaler")

    @classmethod
    @menuItem("Plugins")
    def AnnotationScaler(cls):
        menu_item = Menu(title="Start Annotation Scaler",
                         id_="AnnotationScaler_1f906a71a12011efa589f83441a96bd5",
                         section="",
                         action="AnnotationScaler_1f906a71a12011efa589f83441a96bd5.openGUI()")

        return menu_item