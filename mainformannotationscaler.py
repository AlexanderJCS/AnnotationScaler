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
        print(multiplier)

        selected_annotations = WorkingContext.getEntitiesOfClassAsObjects(None, OrsSelectedObjects, ORSModel.ors.Annotation)

        for annotation in selected_annotations:
            print("annotation")

            control_points = annotation.getControlPoints(0).getAsNDArray()

            print(control_points)

            for i in range(0, len(control_points), 3):
                point = np.array([control_points[i], control_points[i + 1], control_points[i + 2]])
                print(f"Before: {point}")
                point *= multiplier
                print(f"After: {point}")
                vec_point = ORSModel.ors.Vector3()
                vec_point.setXYZ(*point)

                annotation.addControlPoint(vec_point, 0, None)
                appended_ctrl_point_idx = annotation.getControlPointCount(0) - 1
                annotation.setControlPointCaptionAtIndex(
                    appended_ctrl_point_idx,
                    0,
                    annotation.getControlPointCaptionAtIndex(0, 0),
                )
                annotation.removeControlPoint(0, 0)

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
