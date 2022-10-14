#
# Copyright (C) 2020 RFI
#
# Author: James Parkhurst
#
# This code is distributed under the Apache license, a copy of
# which is included in the root directory of this package.
#

from setuptools import setup


def main():
    """
    Setup the package

    """
    tests_require = ["pytest", "pytest-cov"]

    setup(
        packages=["scivision-parakeet"],
        install_requires=[
            "python-parakeet",
            "intake",
        ],
        setup_requires=["setuptools_scm", "pytest-runner"],
        entry_points={
            "intake.drivers": ["scivision_parakeet=scivision_parakeet:ParakeetSource"]
        },
        tests_require=tests_require,
        test_suite="tests",
    )


if __name__ == "__main__":
    main()
