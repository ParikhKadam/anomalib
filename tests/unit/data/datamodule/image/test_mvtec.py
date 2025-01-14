"""Unit Tests - MVTec Datamodule."""

# Copyright (C) 2023-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

import pytest
from torchvision.transforms.v2 import Resize

from anomalib.data import MVTec
from tests.unit.data.datamodule.base.image import _TestAnomalibImageDatamodule


class TestMVTec(_TestAnomalibImageDatamodule):
    """MVTec Datamodule Unit Tests."""

    @pytest.fixture()
    @staticmethod
    def datamodule(dataset_path: Path) -> MVTec:
        """Create and return a MVTec datamodule."""
        _datamodule = MVTec(
            root=dataset_path / "mvtec",
            category="dummy",
            train_batch_size=4,
            eval_batch_size=4,
            augmentations=Resize((256, 256)),
        )
        _datamodule.prepare_data()
        _datamodule.setup()

        return _datamodule

    @pytest.fixture()
    @staticmethod
    def fxt_data_config_path() -> str:
        """Return the path to the test data config."""
        return "examples/configs/data/mvtec.yaml"