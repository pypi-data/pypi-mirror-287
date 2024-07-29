"""
Data model of our input4MIPs database
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import TYPE_CHECKING, Union

import cftime
import numpy as np
import pandas as pd
import xarray as xr
from attrs import define, fields
from loguru import logger

from input4mips_validation.database.raw import Input4MIPsDatabaseEntryFileRaw
from input4mips_validation.hashing import get_file_hash_sha256
from input4mips_validation.inference.from_data import create_time_range
from input4mips_validation.logging import LOG_LEVEL_INFO_FILE

if TYPE_CHECKING:
    from input4mips_validation.cvs import Input4MIPsCVs


@define
class Input4MIPsDatabaseEntryFile(Input4MIPsDatabaseEntryFileRaw):
    """
    Data model for a file entry in the input4MIPs database
    """

    @classmethod
    def from_file(  # noqa: PLR0913
        cls,
        file: Path,
        cvs: Input4MIPsCVs,
        frequency_metadata_key: str = "frequency",
        no_time_axis_frequency: str = "fx",
        time_dimension: str = "time",
    ) -> Input4MIPsDatabaseEntryFile:
        """
        Initialise based on a file

        Parameters
        ----------
        file
            File from which to extract data to create the database entry

        cvs
            Controlled vocabularies that were used when writing the file

        frequency_metadata_key
            The key in the data's metadata
            which points to information about the data's frequency.

        no_time_axis_frequency
            The value of "frequency" in the metadata which indicates
            that the file has no time axis i.e. is fixed in time.


        time_dimension
            Time dimension of `ds`

        Returns
        -------
        :
            Initialised database entry
        """
        logger.log(
            LOG_LEVEL_INFO_FILE.name,
            f"Creating file database entry for {file}",
        )
        ds = xr.open_dataset(file)
        metadata_attributes: dict[str, Union[str, None]] = ds.attrs
        # Having to re-infer metadata from the data this is silly,
        # would be much simpler if all metadata was just in the file's attributes.
        metadata_data: dict[str, Union[str, None]] = {}

        frequency = metadata_attributes[frequency_metadata_key]
        if frequency is not None and frequency != no_time_axis_frequency:
            # Technically, this should probably use the bounds...
            time_axis = ds[time_dimension]
            # xarray's types not ideal here
            time_start: Union[np.datetime64, cftime.datetime] = time_axis.min().values  # type: ignore
            time_end: Union[np.datetime64, cftime.datetime] = time_axis.max().values  # type: ignore

            md_datetime_start: Union[str, None] = format_datetime_for_db(time_start)
            md_datetime_end: Union[str, None] = format_datetime_for_db(time_end)

            md_datetime_time_range: Union[str, None] = create_time_range(
                time_start=time_start,
                time_end=time_end,
                ds_frequency=frequency,
            )

        else:
            md_datetime_start = None
            md_datetime_end = None
            md_datetime_time_range = None

        metadata_data["datetime_start"] = md_datetime_start
        metadata_data["datetime_end"] = md_datetime_end
        metadata_data["time_range"] = md_datetime_time_range

        metadata_directories_all = cvs.DRS.extract_metadata_from_path(file.parent)
        # Only get metadata from directories/files that we don't have elsewhere.
        # Reason: the values in the filepath have special characters removed,
        # so may not be correct if used for direct inference.
        metadata_directories_keys_to_use = (
            set(metadata_directories_all.keys())
            .difference(set(metadata_attributes.keys()))
            .difference(set(metadata_data.keys()))
        )
        metadata_directories = {
            k: metadata_directories_all[k] for k in metadata_directories_keys_to_use
        }

        all_metadata: dict[str, Union[str, None]] = {}
        used_sources: list[str] = []
        # TODO: make clearer, order below sets order of sources
        for source, md in (
            ("inferred from the file's data", metadata_data),
            ("inferred from the file path", metadata_directories),
            ("retrieved from the file's attributes", metadata_attributes),
        ):
            keys_to_check = md.keys() & all_metadata
            for ktc in keys_to_check:
                if all_metadata[ktc] != md[ktc]:
                    # Raise a warning, but ultimately give preference
                    # to earlier sources
                    msg = (
                        f"Value clash for {ktc}. "
                        f"Value from previous sources ({used_sources}): "
                        f"{all_metadata[ktc]!r}. "
                        f"Value {source}: {md[ktc]!r}. "
                        f"{file=}"
                    )
                    logger.warning(msg)

            all_metadata = md | all_metadata
            used_sources.append(source)

        all_metadata["filepath"] = str(file)
        all_metadata["sha256"] = get_file_hash_sha256(file)
        all_metadata["esgf_dataset_master_id"] = cvs.DRS.get_esgf_dataset_master_id(
            file
        )

        # Make sure we only pass metadata that is actully of interest to the database
        cls_fields = [v.name for v in fields(cls)]
        init_kwargs = {k: v for k, v in all_metadata.items() if k in cls_fields}

        return cls(**init_kwargs)  # type: ignore # mypy confused for some reason


def format_datetime_for_db(time: cftime.datetime | dt.datetime | np.datetime64) -> str:
    """
    Format a "datetime_*" value for storing in the database

    Parameters
    ----------
    time
        Time value to format

    Returns
    -------
        Formatted time value
    """
    if isinstance(time, np.datetime64):
        ts: cftime.datetime | dt.datetime | pd.Timestamp = pd.to_datetime(str(time))

    else:
        ts = time

    return f"{ts.isoformat()}Z"  # Z indicates timezone is UTC
