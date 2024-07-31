__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "08/04/2020"

from typing import Optional

from Orange.widgets.widget import OWWidget, Input, Output

from darfix.gui.PCAWidget import PCAWidget
from darfix import dtypes


class PCAWidgetOW(OWWidget):
    """
    Widget that computes the background substraction from a dataset
    """

    name = "PCA"
    icon = "icons/pca.png"
    want_main_area = False

    # Inputs
    class Inputs:
        dataset = Input("dataset", dtypes.OWSendDataset)

    # Outputs
    class Outputs:
        dataset = Output("dataset", dtypes.OWSendDataset)

    def __init__(self):
        super().__init__()

        self._widget = PCAWidget(parent=self)
        self.controlArea.layout().addWidget(self._widget)

    @Inputs.dataset
    def setDataset(self, _input: Optional[dtypes.OWSendDataset]):
        if _input is not None:
            dataset, update = _input
            self._widget.setDataset(dataset)
            if update is None:
                self.open()
            owdataset = dtypes.OWDataset(self, *dataset[1:])
            senddataset = dtypes.OWSendDataset(owdataset, update)
            self.Outputs.dataset.send(senddataset)

    def _updateDataset(self, widget, dataset):
        self._widget._updateDataset(widget, dataset)
