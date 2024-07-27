import numpy as np

import Orange.data
from Orange.widgets import gui, settings, widget
from Orange.widgets.utils.concurrent import ConcurrentWidgetMixin
from Orange.data.util import get_unique_names




class MissingPrimaryException(Exception):
    pass

class IncompatibleShapeException(Exception):
    pass

class NoAttributesException(Exception):
    pass

class MultipleTargetsException(Exception):
    pass




class Operation:
    def __init__(self, name, func):
        self.name = name
        self.func = func



def rename(names, proposed):
    proposed_names = [attr.name for attr in proposed]
    valid_names = get_unique_names(names, proposed_names)

    return [attr if proposed_names[i] == valid_names[i] else attr.renamed(valid_names[i]) for i, attr in enumerate(proposed)]




def bubble_operation(operation, *args):
    n = len(args)

    if n > 2:
        mid = n // 2
        left = bubble_operation(operation, *args[:mid])
        right = bubble_operation(operation, *args[mid:])
        return operation(left, right)
    
    if n == 2:
        return operation(*args)
    
    if n == 1:
        return args[0]



def divide(p_data, s_data):
    # RULES:
    # 1. INF / x = INF
    # 2. x / INF = 0

    # 3. INF / INF = NAN
    # 4. x / 0 = NAN
    # 5. NAN / x = NAN
    # 6. x / NAN = NAN

    # 7. x / y = z

    p_inf = np.isinf(p_data)
    s_inf = np.isinf(s_data)

    infs = np.logical_and(p_inf, np.logical_not(s_inf)) # 1
    zero = np.logical_and(s_inf, np.logical_not(p_inf)) # 2

    nans_arrs = [
        np.logical_and(infs, zero), # 3
        s_data == 0, # 4
        np.isnan(p_data), # 5
        np.isnan(s_data), # 6
    ]

    nans = bubble_operation(np.logical_or, *nans_arrs)

    base = np.full_like(p_data, np.nan)
    base[infs] = p_data[infs]
    base[zero] = 0

    valid = np.logical_not(bubble_operation(np.logical_or, infs, zero, nans))

    return np.divide(p_data, s_data, out=base, where=valid)



OPERATIONS = [
    Operation("Addition", lambda p_data, s_data: p_data + s_data),
    Operation("Subtraction", lambda p_data, s_data: p_data - s_data),
    Operation("Multiplication", lambda p_data, s_data: p_data * s_data),
    Operation("Division", lambda p_data, s_data: divide(p_data, s_data)),
]




def get_targets(p_data, s_data):
    p_cols = 1 if len(p_data.Y.shape) == 1 else p_data.Y.shape[1]
    s_cols = 1 if len(s_data.Y.shape) == 1 else s_data.Y.shape[1]

    if p_cols + s_cols > 1:
        raise MultipleTargetsException()

    if p_cols == 1:
        return p_data.Y.copy()[:, np.newaxis]
    
    if s_cols == 1:
        return s_data.Y.copy()[:, np.newaxis]
    
    return None



class OWOperations(widget.OWWidget, ConcurrentWidgetMixin):
    name = "Elementwise Operations"
    description = "Perform elementwise operations on two tables."
    icon = "icons/operations.svg"
    id = "orangecontrib.elementwise.widgets.owoperations"
    priority = 10

    class Inputs:
        p_data = widget.Input("Primary Data", Orange.data.Table, default=True)
        s_data = widget.Input("Secondary Data", Orange.data.Table)


    class Outputs:
        data = widget.Output("Data", Orange.data.Table, default=True)




    settingsHandler = settings.DomainContextHandler()
    
    want_main_area = False
    resizing_enabled = False


    operation_index = settings.Setting(0)

    operations = OPERATIONS


    class Error(widget.OWWidget.Error):
        incompatible_shapes = widget.Msg("Incompatible shapes: {} and {}")
        missing_primary = widget.Msg("Secondary data but no primary")
        no_attributes = widget.Msg("{} has no attributes")
        multiple_targets = widget.Msg("The number of targets in primary and secondary data combined is greater than 1")


    class Warning(widget.OWWidget.Warning):
        pass


    def __init__(self):
        widget.OWWidget.__init__(self)
        ConcurrentWidgetMixin.__init__(self)

        self.p_data = None
        self.s_data = None

        gui.comboBox(
            self.controlArea, self, "operation_index",
            contentsLength=12, searchable=True,
            callback=self.operation_changed, items=[op.name for op in self.operations]
        )
        

    @staticmethod
    def reshape_data(data, shape):
        # Same shape.
        if data.shape == shape:
            return data

        # A single row.
        if data.shape[0] == 1 and data.shape[1] == shape[1]:
            return np.tile(data, (shape[0], 1))

        # A single column.
        if data.shape[0] == shape[0] and data.shape[1] == 1:
            return np.tile(data, (1, shape[1]))

        raise IncompatibleShapeException(data.shape, shape)
    

    @staticmethod
    def get_domain(row, col):
        attributes = row.attributes
        metas = list(row.metas) + rename(row, col.metas)
        class_vars = list(row.class_vars) + rename(row, col.class_vars)

        return Orange.data.Domain(attributes, class_vars=class_vars, metas=metas)
    

    @staticmethod
    def transform(p_data, s_data):
        rows = max(p_data.X.shape[0], s_data.X.shape[0])
        cols = max(p_data.X.shape[1], s_data.X.shape[1])

        attributes = np.empty((rows, cols), dtype=p_data.X.dtype)

        if p_data.X.shape[1] == cols:
            domain = OWOperations.get_domain(p_data.domain, s_data.domain)
            metas = np.hstack((
                OWOperations.reshape_data(p_data.metas.copy(), (rows, p_data.metas.shape[1])),
                OWOperations.reshape_data(s_data.metas.copy(), (rows, s_data.metas.shape[1]))
            ))

        else:
            domain = OWOperations.get_domain(s_data.domain, p_data.domain)
            metas = np.hstack((
                OWOperations.reshape_data(s_data.metas.copy(), (rows, s_data.metas.shape[1])),
                OWOperations.reshape_data(p_data.metas.copy(), (rows, p_data.metas.shape[1]))
            ))

        p_X = OWOperations.reshape_data(p_data.X.copy(), (rows, cols))
        s_X = OWOperations.reshape_data(s_data.X.copy(), (rows, cols))

        class_vars = get_targets(p_data, s_data)

        if not class_vars is None:
            class_vars = OWOperations.reshape_data(class_vars, (rows, 1))

        table = Orange.data.Table.from_numpy(domain, attributes, Y=class_vars, metas=metas)
        table.attributes = p_data.attributes

        return p_X, s_X, table
    

    def get_transformed(self):
        p_shape = self.p_data.X.shape
        s_shape = self.s_data.X.shape

        rows = max(p_shape[0], s_shape[0])
        cols = max(p_shape[1], s_shape[1])

        p_data = self.reshape_data(self.p_data.X.copy(), (rows, cols))
        s_data = self.reshape_data(self.s_data.X.copy(), (rows, cols))

        return p_data, s_data
    
        
    def calculate(self):
        if self.p_data is None:
            if self.s_data is None:
                return None
            
            raise MissingPrimaryException()

        if self.p_data.X.shape[1] == 0:
            raise NoAttributesException("Primary data")
        
        if self.s_data is None:
            return self.p_data.copy()
        
        if self.s_data.X.shape[1] == 0:
            raise NoAttributesException("Secondary data")

        operation = self.get_operation_func()

        p_X, s_X, data = OWOperations.transform(self.p_data, self.s_data)

        data.X = operation(p_X, s_X)

        return data


    def get_operation_func(self):
        return self.operations[self.operation_index].func


    def operation_changed(self):
        self.commit()


    @Inputs.p_data
    def set_primary_data(self, data):
        self.Error.clear()
        print(1, "data")

        self.p_data = data
        self.commit()


    @Inputs.s_data
    def set_secondary_data(self, data):
        self.Error.clear()
        print(2, "data")


        self.s_data = data
        self.commit()


    def commit(self):
        data = None
        
        try:
            data = self.calculate()

        except IncompatibleShapeException as e:
            self.Error.incompatible_shapes(e.args[0], e.args[1])

        except NoAttributesException as e:
            self.Error.no_attributes(e.args[0])
        
        except MissingPrimaryException:
            self.Error.missing_primary()

        except MultipleTargetsException:
            self.Error.multiple_targets()

        self.Outputs.data.send(data)





# if __name__ == "__main__":  # pragma: no cover
#     from Orange.widgets.utils.widgetpreview import WidgetPreview
#     import orangecontrib.spectroscopy
#     collagen = Orange.data.Table("collagen.csv")

#     domain = Orange.data.Domain(
#         collagen.domain.attributes,
#         metas=collagen.domain.class_vars + collagen.domain.metas
#     )
    
#     collagen = Orange.data.Table.from_table(domain, collagen)

#     WidgetPreview(OWElementWise).run(
#         set_primary_data=collagen[:50],
#         set_secondary_data=collagen[50:100]
#     )