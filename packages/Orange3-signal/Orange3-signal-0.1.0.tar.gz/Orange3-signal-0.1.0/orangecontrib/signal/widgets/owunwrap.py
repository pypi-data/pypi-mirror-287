import numpy as np

import Orange.data
from Orange.widgets import gui, settings, widget
from Orange.widgets.utils.concurrent import ConcurrentWidgetMixin




class OWUnwrap(widget.OWWidget, ConcurrentWidgetMixin):
    name = "Unwrap"
    description = "Unwrap signal (phase correction)."
    icon = "icons/unwrap.svg"
    id = "orangecontrib.signal.widgets.owunwrap"
    priority = 10


    class Inputs:
        data = widget.Input("Data", Orange.data.Table, default=True)


    class Outputs:
        data = widget.Output("Data", Orange.data.Table, default=True)


    want_main_area = False
    want_control_area = True
    resizing_enabled = False

    settingsHandler = settings.DomainContextHandler()

    autocommit = settings.Setting(True)

    DEFAULT_DISCONT = np.pi
    DEFAULT_PERIOD = 2 * np.pi

    discont = settings.Setting(DEFAULT_DISCONT)
    period = settings.Setting(DEFAULT_PERIOD)


    def __init__(self):
        widget.OWWidget.__init__(self)
        ConcurrentWidgetMixin.__init__(self)

        self.data = None
        self.discont = OWUnwrap.DEFAULT_DISCONT
        self.period = OWUnwrap.DEFAULT_PERIOD

        # Todo: Add discont and period options?

        gui.auto_commit(self.controlArea, self, "autocommit", "Send Data")


    @Inputs.data
    def set_data(self, data):
        self.data = data
        self.commit.now()


    @gui.deferred
    def commit(self):
        out_data = None

        if self.data is not None:
            out_data = OWUnwrap.unwrap_table(self.data, discont=self.discont, period=self.period)

        self.Outputs.data.send(out_data)


    @staticmethod
    def unwrap_table(table, discont=DEFAULT_DISCONT, period=DEFAULT_PERIOD):
        new_table = table.copy()
        new_table.X = OWUnwrap.unwrap(table.X, discont=discont, period=period)
        return new_table
    

    @staticmethod
    def unwrap(data, discont=DEFAULT_DISCONT, period=DEFAULT_PERIOD):
        new_data = data.copy()

        for row_i in range(data.shape[0]):
            valid = ~np.isnan(data[row_i, :])
            new_data[row_i, valid] = np.unwrap(data[row_i, valid], discont=discont, period=period)

        return new_data




if __name__ == "__main__":  # pragma: no cover
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    WidgetPreview(OWUnwrap).run()