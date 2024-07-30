import numpy as np

import Orange.data
from Orange.widgets import gui, settings, widget
from Orange.widgets.utils.concurrent import ConcurrentWidgetMixin
from Orange.widgets.utils.itemmodels import DomainModel

from orangecontrib.core_extended.widgets.components.widgets import IntLineEdit




def histogram(values, bins):
    hist, bin_edges = np.histogram(values, bins)
    means = (bin_edges[:-1] + bin_edges[1:]) / 2

    return hist, means




class OWHistogram(widget.OWWidget, ConcurrentWidgetMixin):
    name = "Histogram"
    description = "Example description."
    icon = "icons/histogram.svg"
    keywords = "histogram"
    id = "orangecontrib.core_extended.widgets.owhistogram"


    class Inputs:
        data = widget.Input("Data", Orange.data.Table, default=True)


    class Outputs:
        data = widget.Output("Data", Orange.data.Table, default=True)


    MIN_BINS = 2
    DEFAULT_BINS = 100
    MAX_BINS = 999

    want_main_area = False
    resizing_enabled = False


    settingsHandler = settings.DomainContextHandler()

    hist_attr = settings.ContextSetting(None)
    bins = settings.Setting(DEFAULT_BINS)

    autocommit = settings.Setting(True)


    hist_model = DomainModel(DomainModel.MIXED, valid_types=Orange.data.ContinuousVariable)


    def __init__(self):
        widget.OWWidget.__init__(self)
        ConcurrentWidgetMixin.__init__(self)

        self.data = None
        self.hist_attr = None
        self.bins = self.DEFAULT_BINS
        
        gui.comboBox(
            self.controlArea, self, "hist_attr",
            contentsLength=12, searchable=True,
            callback=self.attr_changed, model=self.hist_model
        )

        vbox = gui.vBox(self.controlArea)
        hbox = gui.hBox(vbox)

        gui.widgetLabel(hbox, label="Bins:", labelWidth=50)

        le = IntLineEdit(
            self, "bins", bounds=(self.MIN_BINS, self.MAX_BINS),
            default=self.DEFAULT_BINS, callback=self.n_bins_changed
        )

        hbox.layout().addWidget(le)
        vbox.layout().addWidget(hbox)
        self.controlArea.layout().addWidget(vbox)


        gui.rubber(self.controlArea)

        gui.auto_commit(self.controlArea, self, "autocommit", "Send Data")


    def get_attr_data(self):
        if self.data is None or self.hist_attr is None:
            return None
        
        attr = self.data.domain[self.hist_attr]
        return self.data.get_column(attr)
    

    def create_histogram(self):
        values = self.get_attr_data()

        if values is None:
            return None

        ys, xs = histogram(values, self.bins)

        vars = [Orange.data.ContinuousVariable(name=str(x)) for x in xs]

        domain = Orange.data.Domain(vars)

        return Orange.data.Table.from_numpy(domain, ys[np.newaxis, :])


    def init_attr_models(self):
        domain = self.data.domain if self.data else None
        self.hist_model.set_domain(domain)

        if not self.hist_attr:
            self.hist_attr = self.hist_model[0] if len(self.hist_model) >= 1 else None

    
    def attr_changed(self):
        self.commit.deferred()


    def n_bins_changed(self):
        self.commit.deferred()


    @Inputs.data
    def set_data(self, data):
        self.data = data
        self.init_attr_models()
        self.commit.now()


    @gui.deferred
    def commit(self):
        data = self.create_histogram()
        self.Outputs.data.send(data)




if __name__ == "__main__":  # pragma: no cover
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    # collagen = Orange.data.Table("collagen.csv")
    # WidgetPreview(OWHistogram).run(set_data=collagen)
    WidgetPreview(OWHistogram).run()
