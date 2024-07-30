import numpy as np

from scipy import ndimage

from AnyQt import QtCore, QtGui, QtWidgets

import Orange.data
from Orange.widgets import gui, settings, widget
from Orange.widgets.utils.concurrent import ConcurrentWidgetMixin
from Orange.widgets.utils.itemmodels import DomainModel

from orangecontrib.spatial.utils.spectroscopy import values_to_linspace, index_values

from Orange.data.util import get_unique_names




class CloseButton(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        
        self.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_TitleBarCloseButton))

        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0);
                border: 0px;
            }
            QPushButton::hover {
                background-color: rgba(200, 50, 50, 255);
            }
        """)




class AttrItem(QtWidgets.QListWidgetItem):
    def __init__(self, widget, master, label, callback=None):
        QtWidgets.QListWidgetItem.__init__(self)

        self.widget = widget
        self.master = master
        self.label = label
        self.callback = callback

        self.item = QtWidgets.QWidget()

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        text_widget = QtWidgets.QLabel(label)
        layout.addWidget(text_widget)

        layout.addStretch()

        remove_widget = CloseButton()
        remove_widget.clicked.connect(self.callback)
        layout.addWidget(remove_widget)

        self.item.setLayout(layout)

        self.setSizeHint(self.sizeHint())

        self.widget.addItem(self)
        self.widget.setItemWidget(self, self.item)









class OWClusterConnectivity(widget.OWWidget, ConcurrentWidgetMixin):
    name = "Cluster Connectivity"
    description = "Example description."
    icon = "icons/cluster_connectivity.svg"
    id = "orangecontrib.spatial.widgets.owclusterconnectivity"


    class Inputs:
        data = widget.Input("Data", Orange.data.Table, default=True)


    class Outputs:
        data = widget.Output("Data", Orange.data.Table, default=True)


    settingsHandler = settings.DomainContextHandler()
    
    want_main_area = False
    resizing_enabled = False


    cluster_attr = settings.ContextSetting(None)
    constrain_continuous = settings.ContextSetting(False)

    axis_model = DomainModel(DomainModel.METAS | DomainModel.CLASSES,
                             valid_types=Orange.data.ContinuousVariable)
    
    category_model = DomainModel(DomainModel.METAS | DomainModel.CLASSES,
                             valid_types=Orange.data.DiscreteVariable)


    connectivity = settings.Setting(0)
    autocommit = settings.Setting(True)



    class Error(widget.OWWidget.Error):
        pass


    class Warning(widget.OWWidget.Warning):
        no_categories = widget.Msg("No categories found.")



    def __init__(self):
        widget.OWWidget.__init__(self)
        ConcurrentWidgetMixin.__init__(self)

        self.data = None

        self.cluster_attr = None
        self.constrain_continuous = False
        self.axis_attrs = []
        self.connectivity = 0

        gui.comboBox(
            self.controlArea, self, "cluster_attr",
            contentsLength=12, searchable=True,
            callback=self.cluster_attr_changed, model=self.category_model
        )
        
        layout = QtWidgets.QVBoxLayout()

        gbox = QtWidgets.QGroupBox("Spatial Constraints")
        vbox = QtWidgets.QVBoxLayout()

        checkbox = QtWidgets.QCheckBox("Neighbourhood Constraint")
        checkbox.stateChanged.connect(self.spatial_constraint_changed)
        vbox.addWidget(checkbox)


        form = QtWidgets.QFormLayout()
        self.spinbox = gui.spin(self, self, "connectivity", minv=1, maxv=1,
                              step=1, callback=self.connectivity_changed)
        
        form.addRow("Connectivity", self.spinbox)
        vbox.addLayout(form)


        gbox.setLayout(vbox)
        layout.addWidget(gbox)

        self.controlArea.layout().addLayout(layout)

        gui.rubber(self.controlArea)

        gui.auto_commit(self.controlArea, self, "autocommit", "Send Data")


    def init_models(self):
        domain = self.data.domain if self.data else None
        self.axis_model.set_domain(domain)
        self.category_model.set_domain(domain)

        if len(self.category_model) == 0:
            self.cluster_attr = None
            self.Warning.no_categories()

        else:
            if self.cluster_attr is None:
                self.cluster_attr = self.category_model[0]

        self.spinbox.setMaximum(len(self.axis_model))


    def cluster_attr_changed(self):
        self.commit.deferred()


    def spatial_constraint_changed(self, flag):
        self.constrain_continuous = flag
        self.commit.deferred()

    
    def connectivity_changed(self):
        self.commit.deferred()
    

    @staticmethod
    def spatial_cluster(col, axes, connectivity):
        if axes is None:
            return col
        
        ls = []
        indices = []
        
        for i in range(axes.shape[1]):
            axis = axes[:, i]

            lsa = values_to_linspace(axis)
            
            ls.append(lsa)
            indices.append(index_values(axis, lsa))

        new_shape = tuple([lsa[2] for lsa in ls])
        hyperspec = np.ones(new_shape) * np.nan

        hyperspec[tuple(indices)] = col
        labelled = np.empty(hyperspec.shape)

        vals = np.unique(hyperspec)
        k = -1

        structure = ndimage.generate_binary_structure(axes.shape[1], connectivity)

        for i in vals:
            labels, n = ndimage.label(hyperspec == i, structure=structure)
            labelled[labels != 0] = labels[labels != 0] + k
            k += n

        return labelled[tuple(indices)], k


    @Inputs.data
    def set_data(self, data):
        self.Warning.no_categories.clear()
        self.data = data
        self.init_models()
        self.commit.now()

    
    def get_attrs_data(self, attr_names):
        if len(attr_names) == 0:
            return None, None
        
        indices = [self.data.domain.index(col) for col in attr_names]

        attrs = list(self.data.domain.select_columns(indices))
        data = np.column_stack([self.data.get_column(attr) for attr in attr_names])

        return attrs, data




    @gui.deferred
    def commit(self):
        new_data = None

        if not self.data is None:
            data = self.data.get_column(self.cluster_attr)

            n = int(np.nanmax(data))

            if self.constrain_continuous:
                _, axis_data = self.get_attrs_data(self.axis_model)

                data, n = OWClusterConnectivity.spatial_cluster(data, axis_data, self.connectivity) # metric=self.metric.lower()

            values = [f"C{i+1}" for i in range(n+1)]
            var = Orange.data.DiscreteVariable(name=get_unique_names(self.data.domain, "Cluster"), values=values)

            new_data = self.data.add_column(var, data, to_metas=True)

        self.Outputs.data.send(new_data)


    






if __name__ == "__main__":  # pragma: no cover
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    WidgetPreview(OWClusterConnectivity).run()