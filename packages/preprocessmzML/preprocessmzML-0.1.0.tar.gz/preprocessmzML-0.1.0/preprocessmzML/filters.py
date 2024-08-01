import pyopenms as oms

def set_filter_parameters(filter, parameters):
    """
    Set the parameters for a given filter

    Args:
        filter (oms.Filter): The filter object to set parameters for.
        parameters (dict): A dictionary of parameters where the key is the parameter name
                           and the value is the parameter value.

    Example:
        >>> filter = oms.MorphologicalFilter()
        >>> params = {"struc_elem_length": 3.0, "struc_elem_unit": "Thomson", "method": "tophat"}
        >>> set_filter_parameters(filter, params)
    """
    param = oms.Param()
    for key, value in parameters.items():
        param.setValue(key, value)
    filter.setParameters(param)
