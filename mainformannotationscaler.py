import ORSModel
from OrsLibraries.workingcontext import WorkingContext
from ORSServiceClass.windowclasses.orsabstractwindow import OrsAbstractWindow
from PyQt6.QtGui import QDoubleValidator
from OrsLibraries.workingcontext import WorkingContext
from ORSModel import Channel
from ORSModel import OrsSelectedObjects

from .ui_mainformannotationscaler import Ui_MainFormAnnotationscaler
import numpy as np


class MainFormAnnotationscaler(OrsAbstractWindow):
    def __init__(self, implementation, parent=None):
        super().__init__(implementation, parent)
        self.ui = Ui_MainFormAnnotationscaler()
        self.ui.setupUi(self)
        WorkingContext.registerOrsWidget('AnnotationScaler_1f906a71a12011efa589f83441a96bd5', implementation,
                                         'MainFormAnnotationscaler', self)

        # Create a QDoubleValidator with a range (optional) and set it to the QLineEdit
        validator = QDoubleValidator(0.0, 9999.99, 4, self)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)  # Standard notation, not scientific

        self.ui.edit_scale_initial_x.setValidator(validator)
        self.ui.edit_scale_initial_y.setValidator(validator)
        self.ui.edit_scale_final_x.setValidator(validator)
        self.ui.edit_scale_final_y.setValidator(validator)

    @staticmethod
    def process(initial_scale: tuple[float, float, float], final_scale: tuple[float, float, float]):
        multiplier = np.array(final_scale) / np.array(initial_scale)

        # 4x4 transformation matrix
        transformation = ORSModel.ors.Matrix4x4()
        transformation.setupAsIdentity()
        transformation.setValue(0, 0, multiplier[0])
        transformation.setValue(1, 1, multiplier[1])
        transformation.setValue(2, 2, multiplier[2])

        print(transformation)

        selected_annotations = WorkingContext.getEntitiesOfClassAsObjects(None, OrsSelectedObjects, ORSModel.ors.Annotation)

        for annotation in selected_annotations:
            annotation.applyTransformation(transformation, 0)

    @staticmethod
    def are_annotations_selected() -> bool:
        return len(WorkingContext.getEntitiesOfClass(None, OrsSelectedObjects, ORSModel.ors.Annotation)) > 0

    def get_scales(self):
        initial_scale = (
            float(self.ui.edit_scale_initial_x.text()),
            float(self.ui.edit_scale_initial_y.text()),
            float(self.ui.edit_scale_initial_z.text())
        )

        final_scale = (
            float(self.ui.edit_scale_final_x.text()),
            float(self.ui.edit_scale_final_y.text()),
            float(self.ui.edit_scale_final_z.text())
        )

        return initial_scale, final_scale

    def on_btn_process_clicked(self):
        if not self.are_annotations_selected():
            self.ui.label_output.setText("Select annotations on the right")
            return

        self.ui.label_output.setText("Processing...")

        try:
            initial_scale, final_scale = self.get_scales()
        except ValueError:
            self.ui.label_output.setText("Invalid input! Please enter a number.")
            return

        self.process(initial_scale, final_scale)
        self.ui.label_output.setText("Processed!")

    def on_btn_reverse_clicked(self):
        if not self.are_annotations_selected():
            self.ui.label_output.setText("Select annotations on the right")
            return

        self.ui.label_output.setText("Reversing...")

        try:
            initial_scale, final_scale = self.get_scales()
        except ValueError:
            self.ui.label_output.setText("Invalid input! Please enter a number.")
            return

        self.process(final_scale, initial_scale)
        self.ui.label_output.setText("Reversed!")
