import numpy as np
from bolero.representation.ul_policies import (LinearGaussianPolicy,
                                               ContextTransformationPolicy,
                                               BoundedScalingPolicy)
from bolero.representation.context_transformations import quadratic
from numpy.testing import assert_array_almost_equal, assert_array_equal
from nose.tools import assert_almost_equal, assert_raises_regexp


def test_linear_gaussian():
    random_state = np.random.RandomState(0)

    n_samples = 1001
    X = np.linspace(0, 1, n_samples)[:, np.newaxis]
    X_bias = np.hstack((X, np.ones((n_samples, 1))))
    Y_wo_noise = 3.0 * X + 10.0
    Y = Y_wo_noise + 0.05 * random_state.randn(n_samples, 1)

    ulp = LinearGaussianPolicy(1, 2)
    ulp.fit(X_bias, Y, weights=np.ones(n_samples))
    Y_pred = np.array([ulp(x, explore=False) for x in X_bias])
    assert_array_almost_equal(Y_pred, Y_wo_noise, decimal=2)
    assert_almost_equal(ulp.W[0, 0], 3.0, places=2)
    assert_almost_equal(ulp.W[0, 1], 10.0, places=2)

    ulp = LinearGaussianPolicy(1, 2, mean=np.array([10.0]),
                               random_state=random_state)
    Y_sampled = np.array([ulp(x, explore=True) for x in X_bias])
    assert_almost_equal(np.mean(Y_sampled), 10.0, places=1)
    assert_almost_equal(np.std(Y_sampled), 1.0, places=1)


def test_context_transformation():
    random_state = np.random.RandomState(0)

    n_samples = 101
    X = np.linspace(0, 1, n_samples)[:, np.newaxis]
    Y = 3.0 * X ** 2 + 2.0 * X + 10.0

    ulp = ContextTransformationPolicy(LinearGaussianPolicy, 1, 1, "quadratic")
    ulp.fit(X, Y, weights=np.ones(n_samples))
    Y_pred = np.array([ulp(x, explore=False) for x in X])
    assert_array_almost_equal(Y_pred, Y)
    assert_almost_equal(ulp.W[0, 0], 3.0)
    assert_almost_equal(ulp.W[0, 1], 2.0)
    assert_almost_equal(ulp.W[0, 2], 10.0)

    ulp = ContextTransformationPolicy(LinearGaussianPolicy, 1, 1, "quadratic")
    phi_X = np.array([ulp.transform_context(x) for x in X])
    ulp.fit(phi_X, Y, weights=np.ones(n_samples), context_transform=False)
    Y_pred2 = np.array([ulp(x, explore=False) for x in X])
    assert_array_equal(Y_pred, Y_pred2)

    ulp = ContextTransformationPolicy(LinearGaussianPolicy, 1, 1, quadratic)
    phi_X = np.array([ulp.transform_context(x) for x in X])
    ulp.fit(phi_X, Y, weights=np.ones(n_samples), context_transform=False)
    Y_pred3 = np.array([ulp(x, explore=False) for x in X])
    assert_array_equal(Y_pred, Y_pred3)


def test_bounded_scaling():
    random_state = np.random.RandomState(0)

    n_samples = 1001
    X = np.linspace(0, 1, n_samples)[:, np.newaxis]
    X_bias = np.hstack((X, np.ones((n_samples, 1))))
    Y = 3.0 * X + 10.0

    lg_ulp = LinearGaussianPolicy(1, 2)

    assert_raises_regexp(
        ValueError, "requires boundaries", BoundedScalingPolicy, lg_ulp,
        scaling="auto")

    ulp = BoundedScalingPolicy(
        lg_ulp, scaling="auto", bounds=np.array([[10.0, 12.0]]))
    ulp.fit(X_bias, Y, weights=np.ones(n_samples))
    Y_pred = np.array([ulp(x, explore=False) for x in X_bias])
    assert_array_almost_equal(Y_pred, np.clip(Y, 10.0, 12.0))
    assert_almost_equal(ulp.W[0, 0], 3.0)
    assert_almost_equal(ulp.W[0, 1], 10.0)
