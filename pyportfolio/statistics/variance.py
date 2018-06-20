import numpy as np


def variance(list):
    r"""Calculate the variance.

    .. math::

        E((X-E\left( X \right))^2)

    :param list: data
    :type list: pandas Dataframe
    :return: variance of the data
    :rtype: float
    """
    return np.var(list)[0]

