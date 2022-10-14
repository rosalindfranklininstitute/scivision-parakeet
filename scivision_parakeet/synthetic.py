import intake
from functools import lru_cache
from . import __version__


class ParakeetSource(intake.source.base.DataSource):
    container = "python"
    name = "parakeet"
    version = __version__
    partition_access = True

    def __init__(
        self,
        metadata=None,
        directory=None,
        config=None,
    ):
        super().__init__(metadata=metadata)

        # Set the config
        if config is None:
            self._config = {
                "sample": {"molecules": {"pdb": [{"id": "4v1w", "instances": 1}]}},
            }
        else:
            self._config = config

        # Set the output directory
        if directory is None:
            self._directory = "parakeet_data"
        else:
            self._directory = directory

        self._ds = None
        self.image_count = 0

    def _get_schema(self):
        import mrcfile
        import parakeet
        import os

        if self._ds is None:

            # Set the filenames
            sample_file = os.path.join(self._directory, "sample.h5")
            exit_wave_file = os.path.join(self._directory, "exit_wave.h5")
            optics_file = os.path.join(self._directory, "optics.h5")
            image_file = os.path.join(self._directory, "image.mrc")

            # Create the directory
            if not os.path.exists(self._directory):
                os.mkdir(self._directory)

            # Run the simulation
            parakeet.run(
                self._config, sample_file, exit_wave_file, optics_file, image_file
            )
            assert os.path.exists(sample_file)
            assert os.path.exists(exit_wave_file)
            assert os.path.exists(optics_file)
            assert os.path.exists(image_file)

            # Set the dataset
            self._ds = mrcfile.mmap(image_file)

            # Get number of images
            self.image_count = self._ds.data.shape[0]

        return intake.source.base.Schema(
            dtype="float32",
            shape=None,
            datashape=None,
            npartitions=self.image_count,
            extra_metadata=self.metadata,
        )

    @lru_cache(maxsize=None)
    def _get_partition(self, i):
        self._load_metadata()
        assert self._ds is not None
        data = self._ds.data[i, :, :]
        return data

    def read(self):
        self._load_metadata()
        return [self.read_partition(i) for i in range(self.image_count)]

    def _close(self):
        self._ds = None
