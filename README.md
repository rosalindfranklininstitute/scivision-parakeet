# scivision-parakeet
> Provides an [Intake](https://intake.readthedocs.io/en/latest/index.html) interface to synthetic cryoEM images from [Parakeet](https://github.com/rosalindfranklininstitute/parakeet).

[![Building](https://github.com/rosalindfranklininstitute/scivision-parakeet/actions/workflows/python-package.yml/badge.svg)](https://github.com/rosalindfranklininstitute/scivision-parakeet/actions/workflows/python-package.yml)

## Installation

```
pip install git+https://github.com/rosalind-franklin-institute/scivision-parakeet.git
```

> **_NOTE:_** Because the package needs to be built locally from source and has
some external dependencies you may need to ensure your environment is ready before
running this command. You need to set the location of the CUDA compiler and
possibly G++ and FFTW libraries. For full instructions please see the
installation documentation
[here](https://rosalindfranklininstitute.github.io/parakeet/installation.html).


## Usage

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
