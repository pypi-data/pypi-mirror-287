# coding: utf-8
"""module defining utils for an edf volume"""

from __future__ import annotations

import os

import fabio
import numpy
from silx.io.url import DataUrl

from tomoscan.esrf.identifier.edfidentifier import EDFVolumeIdentifier
from tomoscan.esrf.volume.singleframebase import VolumeSingleFrameBase
from tomoscan.scanbase import TomoScanBase
from tomoscan.utils import docstring


class EDFVolume(VolumeSingleFrameBase):
    """
    Save volume data to single frame edf and metadata to .txt files

    :warning: each file saved under {volume_basename}_{index_zfill6}.edf is considered to be a slice of the volume.
    """

    DEFAULT_DATA_SCHEME = "fabio"

    DEFAULT_DATA_EXTENSION = "edf"

    def __init__(
        self,
        folder: str | None = None,
        volume_basename: str | None = None,
        data: numpy.ndarray | None = None,
        source_scan: TomoScanBase | None = None,
        metadata: dict | None = None,
        data_url: DataUrl | None = None,
        metadata_url: DataUrl | None = None,
        overwrite: bool = False,
        header: dict | None = None,
        start_index=0,
        data_extension=DEFAULT_DATA_EXTENSION,
        metadata_extension=VolumeSingleFrameBase.DEFAULT_METADATA_EXTENSION,
    ) -> None:
        if folder is not None:
            url = DataUrl(
                file_path=str(folder),
                data_path=None,
            )
        else:
            url = None
        super().__init__(
            volume_basename=volume_basename,
            url=url,
            data=data,
            source_scan=source_scan,
            metadata=metadata,
            data_url=data_url,
            metadata_url=metadata_url,
            overwrite=overwrite,
            start_index=start_index,
            data_extension=data_extension,
            metadata_extension=metadata_extension,
        )

        self._header = header

    @property
    def header(self) -> dict | None:
        """possible header for the edf files"""
        return self._header

    @docstring(VolumeSingleFrameBase)
    def save_frame(self, frame, file_name, scheme):
        if scheme == "fabio":
            header = self.header or {}
            edf_writer = fabio.edfimage.EdfImage(
                data=frame,
                header=header,
            )
            parent_dir = os.path.dirname(file_name)
            if parent_dir != "":
                os.makedirs(parent_dir, exist_ok=True)
            edf_writer.write(file_name)
        else:
            raise ValueError(f"scheme {scheme} is not handled")

    @docstring(VolumeSingleFrameBase)
    def load_frame(self, file_name, scheme):
        if scheme == "fabio":
            return fabio.open(file_name).data
        else:
            raise ValueError(f"scheme {scheme} is not handled")

    @staticmethod
    @docstring(VolumeSingleFrameBase)
    def from_identifier(identifier):
        """Return the Dataset from a identifier"""
        if not isinstance(identifier, EDFVolumeIdentifier):
            raise TypeError(
                f"identifier should be an instance of {EDFVolumeIdentifier}"
            )
        return EDFVolume(
            folder=identifier.folder,
            volume_basename=identifier.file_prefix,
        )

    @docstring(VolumeSingleFrameBase)
    def get_identifier(self) -> EDFVolumeIdentifier:
        if self.url is None:
            raise ValueError("no file_path provided. Cannot provide an identifier")
        return EDFVolumeIdentifier(
            object=self, folder=self.url.file_path(), file_prefix=self._volume_basename
        )

    @staticmethod
    def example_defined_from_str_identifier() -> str:
        return " ; ".join(
            [
                f"{EDFVolume(folder='/path/to/my/my_folder').get_identifier().to_str()}",
                f"{EDFVolume(folder='/path/to/my/my_folder', volume_basename='mybasename').get_identifier().to_str()} (if mybasename != folder name)",
            ]
        )
