"""Utility functions."""

import numpy as np
from scipy.spatial.distance import cdist

__all__ = [
    "parameter_space",
    "curve_matching",
    "sample_polyline",
    "refine_polyline",
]


def parameter_space(P, Q, p_num, q_num):
    r"""Parameter space betwee two polylines.

    Parameters
    ----------
    P : array_like
        A :math:`p` by :math:`n` array of :math:`p` vertices in an
        :math:`n`-dimensional space.
    Q : array_like
        A :math:`q` by :math:`n` array of :math:`q` vertices in an
        :math:`n`-dimensional space.
    p_num, q_num : int
        Number of sample points in `P` and `Q`, respectively.

    Returns
    -------
    weight : ndarray
        A `p_num` by `q_num` array containing the distance between the points in
        `P` and `Q`.
    p_coord, q_coord : ndarray
        Axis coordinates for the parameter space.
    p_vert, q_vert : ndarray
        Coordinates for the vertices of polylines.

    Examples
    --------
    Curve space:

    .. plot::
        :context: close-figs

        >>> P = np.array([[0, 0], [2, 2], [4, 2], [4, 4], [2, 1], [5, 1], [7, 2]])
        >>> Q = np.array([[2, 0], [1, 3], [5, 3], [5, 2], [7, 3]])
        >>> import matplotlib.pyplot as plt  # doctest: +SKIP
        >>> plt.plot(*P.T)  # doctest: +SKIP
        >>> plt.plot(*Q.T)  # doctest: +SKIP

    Parameter space with vertices as dashed lines:

    .. plot::
        :context: close-figs

        >>> weight, p, q, p_vert, q_vert = parameter_space(P, Q, 200, 100)
        >>> plt.pcolormesh(p, q, weight.T)  # doctest: +SKIP
        >>> plt.vlines(p_vert, 0, q[-1], "k", "--")  # doctest: +SKIP
        >>> plt.hlines(q_vert, 0, p[-1], "k", "--")  # doctest: +SKIP

    Free space diagram with Fréchet distance as :math:`\epsilon`:

    .. plot::
        :context: close-figs

        >>> eps = fd(P, Q)
        >>> plt.pcolormesh(p, q, weight.T < eps, cmap="gray")  # doctest: +SKIP
        >>> plt.vlines(p_vert, 0, q[-1], "k", "--")  # doctest: +SKIP
        >>> plt.hlines(q_vert, 0, p[-1], "k", "--")  # doctest: +SKIP

    Optimal warping path with integral Fréchet distance:

    .. plot::
        :context: close-figs

        >>> _, owp = ifd_owp(P, Q, 0.1, "squared_euclidean")
        >>> plt.pcolormesh(p, q, weight.T)  # doctest: +SKIP
        >>> plt.plot(*owp.T, "k")  # doctest: +SKIP
    """
    p_vert = np.insert(np.cumsum(np.linalg.norm((np.diff(P, axis=0)), axis=-1)), 0, 0)
    p_coord = np.linspace(0, p_vert[-1], p_num)
    P_pts = sample_polyline(P, p_coord)
    q_vert = np.insert(np.cumsum(np.linalg.norm((np.diff(Q, axis=0)), axis=-1)), 0, 0)
    q_coord = np.linspace(0, q_vert[-1], q_num)
    Q_pts = sample_polyline(Q, q_coord)
    return cdist(P_pts, Q_pts), p_coord, q_coord, p_vert, q_vert


def curve_matching(P, Q, path, sample_num):
    """Return pairs of points in curve space defined by a path in parameter space.

    Parameters
    ----------
    P : array_like
        A :math:`p` by :math:`n` array of :math:`p` vertices in an
        :math:`n`-dimensional space.
    Q : array_like
        A :math:`q` by :math:`n` array of :math:`q` vertices in an
        :math:`n`-dimensional space.
    path : ndarray
        A :math:`N` by :math:`2` array of :math:`N` vertices of polyline in
        curve space.
    sample_num : int
        Number of sample points to be uniformly taken from `path`.

    Returns
    -------
    ndarray
        A :math:`n` by :math:`2` by `sample_num` array of point pairs in curve space.

    Examples
    --------
    >>> P = np.array([[0, 0], [2, 2], [4, 2], [4, 4], [2, 1], [5, 1], [7, 2]])
    >>> Q = np.array([[2, 0], [1, 3], [5, 3], [5, 2], [7, 3]])
    >>> _, path = ifd_owp(P, Q, 0.1, "squared_euclidean")
    >>> pairs = curve_matching(P, Q, path, 100)
    """
    path_len = np.sum(np.linalg.norm(np.diff(path, axis=0), axis=-1))
    path_pts = sample_polyline(path, np.linspace(0, path_len, sample_num))
    P_pts = sample_polyline(P, path_pts[:, 0])
    Q_pts = sample_polyline(Q, path_pts[:, 1])
    return np.stack([P_pts, Q_pts]).transpose(2, 0, 1)


def sample_polyline(vert, param):
    """Sample points from a polyline.

    Parameters
    ----------
    vert : array_like
        A :math:`p` by :math:`n` array of :math:`p` vertices in an
        :math:`n`-dimensional space.
    param : array_like
        An 1-D array of :math:`q` parameters for sampled points.
        Natural parametrization is used, i.e., the polygonal curve
        is parametrized by its arc length.
        Parameters smaller than :math:`0` or larger than the total
        arc length are clipped to the nearest valid value.

    Returns
    -------
    array_like
        A :math:`q` by :math:`n` array of sampled points.

    Examples
    --------
    >>> vert = [[0, 0], [0.5, 0.5], [1, 0]]
    >>> param = np.linspace(0, 2, 10)
    """
    vert = np.asarray(vert)

    seg_vec = np.diff(vert, axis=0)
    seg_len = np.linalg.norm(seg_vec, axis=-1)
    vert_param = np.insert(np.cumsum(seg_len), 0, 0)
    param = np.clip(param, vert_param[0], vert_param[-1])

    pt_vert_idx = np.clip(np.searchsorted(vert_param, param) - 1, 0, len(vert) - 2)
    t = param - vert_param[pt_vert_idx]
    seg_unitvec = seg_vec / seg_len[..., np.newaxis]
    return vert[pt_vert_idx] + t[..., np.newaxis] * seg_unitvec[pt_vert_idx]


def refine_polyline(vert):
    r"""Remove degenerate vertices from a polyline.

    Consecutive duplicate vertices, and three or more vertices on a same line
    are removed.

    Parameters
    ----------
    vert : array_like
        A :math:`p` by :math:`n` array of :math:`p` vertices in an
        :math:`n`-dimensional space.

    Returns
    -------
    array_like
        A :math:`q` by :math:`n` array of :math:`q \leq p` vertices in an
        :math:`n`-dimensional space.

    Examples
    --------
    >>> vert = [[0, 0], [0, 0], [1, 0], [2, 0]]
    >>> refine_polyline(vert)
    array([[0, 0],
           [2, 0]])
    """
    ret = np.empty_like(vert)
    ret[0] = vert[0]
    count = 1

    for i in range(1, len(vert)):
        current = vert[i]
        prev = ret[count - 1]
        if np.all(prev == current):
            continue
        if count >= 2:
            vec = current - prev
            prev_vec = prev - ret[count - 2]
            if np.dot(vec, prev_vec) == np.linalg.norm(vec) * np.linalg.norm(prev_vec):
                ret[count - 1] = current
                continue
        ret[count] = current
        count += 1
    return ret[:count]
