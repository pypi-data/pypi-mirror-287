import numpy as np

from scipy import ndimage

from AnyQt import QtCore, QtGui, QtWidgets

import Orange.data
from Orange.widgets import gui, settings, widget
from Orange.widgets.utils.concurrent import ConcurrentWidgetMixin
from Orange.widgets.utils.itemmodels import DomainModel

from Orange.data.util import get_unique_names




def generate_coords(*xss):
    if len(xss) == 0:
        return None
    
    if len(xss) == 1:
        return xss[0]
    
    vss = np.meshgrid(xss[1], xss[0], *xss[2:])
    
    coords = np.column_stack([vs.flatten() for vs in vss])
    
    coords[:, [0, 1]] = coords[:, [1, 0]]
    
    return coords





class OWTransposeColumn(widget.OWWidget, ConcurrentWidgetMixin):
    name = "Transpose Column"
    description = "Example description."
    icon = "icons/transpose_column.svg"
    id = "orangecontrib.core_extended.widgets.owtransposecolumn"


    class Inputs:
        data = widget.Input("Data", Orange.data.Table, default=True)


    class Outputs:
        data = widget.Output("Data", Orange.data.Table, default=True)


    settingsHandler = settings.DomainContextHandler()
    
    want_main_area = False
    resizing_enabled = False

    transpose_attr = settings.ContextSetting(None)

    transpose_model = DomainModel(DomainModel.METAS | DomainModel.CLASSES)

    autocommit = settings.Setting(True)


    class Warning(widget.OWWidget.Warning):
        no_categories = widget.Msg("No categories found.")



    def __init__(self):
        widget.OWWidget.__init__(self)
        ConcurrentWidgetMixin.__init__(self)

        self.data = None

        self.transpose_attr = None

        gui.comboBox(
            self.controlArea, self, "transpose_attr",
            contentsLength=12, searchable=True,
            callback=self.transpose_attr_changed, model=self.transpose_model
        )

        gui.auto_commit(self.controlArea, self, "autocommit", "Send Data")


    def init_models(self):
        domain = self.data.domain if self.data else None
        self.transpose_model.set_domain(domain)

        if len(self.transpose_model) == 0:
            self.transpose_attr = None
            self.Warning.no_categories()

        else:
            if self.transpose_attr is None:
                self.transpose_attr = self.transpose_model[0]


    def transpose_attr_changed(self):
        self.commit.deferred()


    @Inputs.data
    def set_data(self, data):
        self.Warning.no_categories.clear()
        self.data = data
        self.init_models()
        self.commit.now()


    @staticmethod
    def transpose_column(table, attr):
        if table is None or attr is None:
            return None
        
        coords = table.metas.astype(np.float64)
        assert(np.unique(coords, axis=0).shape == coords.shape)
        
        data = table.X
        
        column = table.get_column(attr)
        
        # Use values_to_linspace for numeric variables.
        uniques = [np.unique(coords[:, i]) for i in range(coords.shape[1])]
        
        ideal_coords = generate_coords(*uniques)
        
        coord_values_dict = {vals: value for vals, value in zip(map(tuple, coords), data)}
        
        ideal_values = np.array([coord_values_dict.get(tuple(coord), np.full(data.shape[1], np.nan)) for coord in ideal_coords])

        unique = np.unique(column)

        n = len(unique)
        m = ideal_values.shape[1]

        valid = np.array([i for i, v in enumerate(table.domain.metas) if v!=attr])
        index = list(set([i for i in range(len(table.domain.metas))]) - set(valid))[0]

        new_coords = np.unique(
            ideal_coords[:, valid],
            axis=0,
        )

        swap_axes = (0, *[i+1 for i in valid], index+1)

        x0 = ideal_values.T.reshape(-1)
        
        x1 = x0.reshape(m, *[len(x) for x in uniques])
        
        x2 = np.transpose(x1, axes=swap_axes)
        
        new_values = np.column_stack(x2.reshape(m, -1, n))
        
        metas = [meta for meta in table.domain.metas if meta != attr]
        
        if m == 1:
            attributes = [attribute.renamed(f"{k}") for attribute in table.domain.attributes for k in unique]
        else:
            attributes = [attribute.renamed(f"{attribute.name}_{attr.name}({k})") for attribute in table.domain.attributes for k in unique]

        domain = Orange.data.Domain(attributes, metas=metas)
        table = Orange.data.Table.from_numpy(domain, new_values, metas=new_coords)
        
        return table


    @gui.deferred
    def commit(self):
        new_data = OWTransposeColumn.transpose_column(self.data, self.transpose_attr)

        self.Outputs.data.send(new_data)


    






if __name__ == "__main__":  # pragma: no cover
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    WidgetPreview(OWTransposeColumn).run()