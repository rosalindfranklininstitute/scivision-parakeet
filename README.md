# scivision-parakeet
> Provides an [Intake](https://intake.readthedocs.io/en/latest/index.html) interface to synthetic cryoEM images from [Parakeet](https://github.com/rosalindfranklininstitute/parakeet).

[![Building](https://github.com/rosalindfranklininstitute/parakeet/actions/workflows/python-package.yml/badge.svg)](https://github.com/rosalindfranklininstitute/parakeet/actions/workflows/python-package.yml)

## Installation:

```
pip install git+https://github.com/rosalind-franklin-institute/scivision-parakeet.git
```

## Usage:

```python
import intake

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
    config=config, directory="parakeet_data"
)

data = ds.read()
```

## Issues

Please use the [GitHub issue tracker](https://github.com/rosalindfranklininstitute/parakeet/issues) to submit bugs or request features.

