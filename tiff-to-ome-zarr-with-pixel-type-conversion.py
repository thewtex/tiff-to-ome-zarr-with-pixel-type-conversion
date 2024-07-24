#!/usr/bin/env python3

"""
Convert a TIFF file to an OME-Zarr file with pixel type conversion.
"""

import argparse

import ngff_zarr as nz
import numpy as np

def tiff_to_ome_zarr_with_pixel_type_conversion(tiff_files, zarr_file, pixel_type, min_value, max_value, dynamic_range):
    ngff_image = nz.cli_input_to_ngff_image(nz.ConversionBackend.TIFFFILE, tiff_files)

    pixel_type = np.dtype(pixel_type)
    if dynamic_range is None:
        dynamic_range = np.iinfo(pixel_type).max - np.iinfo(pixel_type).min
    scale = dynamic_range / (max_value - min_value)

    as_float = ngff_image.data.astype(np.float32)
    scaled = scale * (as_float - min_value)
    cast = scaled.astype(pixel_type)

    ngff_image.data = cast

    multiscales = nz.to_multiscales(ngff_image)
    nz.to_ngff_zarr(zarr_file, multiscales)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "--pixel_type",
        help="Pixel type for the output OME-Zarr file",
        choices=[
            "uint8",
            "uint16",
            "uint32",
            "uint64",
            "int8",
            "int16",
            "int32",
            "int64",
            "float16",
            "float32",
            "float64",
        ],
        default="float32",
    )
    parser.add_argument("--min", help="minimum value to map", default=0.0)
    parser.add_argument("--max", help="maximum value to map", default=255.0)
    parser.add_argument("--dynamic-range", help="dynamic range for scaling the min-max, infer from integer pixel types if not specified", default=None)
    parser.add_argument("tiff_files", help="Input TIFF file(s)", nargs="+")
    parser.add_argument("zarr_file", help="Output OME-Zarr file")

    args = parser.parse_args()

    tiff_to_ome_zarr_with_pixel_type_conversion(
        args.tiff_files, args.zarr_file, args.pixel_type, args.min, args.max,
        args.dynamic_range)
