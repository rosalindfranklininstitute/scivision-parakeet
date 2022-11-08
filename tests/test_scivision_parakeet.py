import intake
import os
from typing import Callable


def test_default_usage(tmpdir):
    assert isinstance(intake.open_scivision_parakeet, Callable)

    ds = intake.open_scivision_parakeet(directory=os.path.join(tmpdir, "parakeet_data"))

    images = ds.read()

    assert len(images) == 1


def test_usage(tmpdir):
    assert isinstance(intake.open_scivision_parakeet, Callable)
    config = {
        "sample": {"molecules": {"pdb": [{"id": "4v1w", "instances": 1}]}},
        "scan": {
            "mode": "tilt_series",
            "num_images": 10,
            "start_angle": -10,
            "step_angle": 2,
        },
    }

    ds = intake.open_scivision_parakeet(
        config=config, directory=os.path.join(tmpdir, "parakeet_data")
    )

    data = ds.read()
    assert len(data) == 10
    for d in data:
        assert d.shape == (1000, 1000)
