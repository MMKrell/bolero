import numpy as np
from bolero.utils.testing import all_subclasses
from bolero.representation import Behavior
from nose.tools import assert_true


ALL_BEHAVIORS = all_subclasses(Behavior)


def test_environments_have_default_constructor():
    for name, Behavior in ALL_BEHAVIORS:
        try:
            beh = Behavior()
        except:
            raise AssertionError("Behavior '%s' is not default "
                                 "constructable" % name)


def test_environments_follow_standard_protocol():
    for _, Behavior in ALL_BEHAVIORS:
        beh = Behavior()
        beh.set_meta_parameters([], [])
        assert_true(beh.can_step())
        inputs = np.array([])
        beh.set_inputs(inputs)
        beh.step()
        outputs = np.array([])
        beh.get_outputs(outputs)
