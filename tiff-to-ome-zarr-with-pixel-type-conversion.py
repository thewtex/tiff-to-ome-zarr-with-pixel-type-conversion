#!/usr/bin/env python3

"""
Convert a TIFF file to an OME-Zarr file with pixel type conversion.
"""

import argparse

from rich import print

import ngff_zarr as nz 


def tiff_to_ome_zarr_with_pixel_type_conversion(tiff_file, zarr_file, pixel_type):
    ngff_image = nz.cli_input_to_ngff_image(nz.ConversionBackend.TIFF, tiff_file)
    print(ngff_image)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tiff_file", help="Input TIFF file")
    parser.add_argument("zarr_file", help="Output OME-Zarr file")
    parser.add_argument("--pixel_type", help="Pixel type for the output OME-Zarr file", choices=["uint8", "uint16", "uint32", "uint64", "int8", "int16", "int32", "int64", "float16", "float32", "float64"], default="float32")
    args = parser.parse_args()

    tiff_to_ome_zarr_with_pixel_type_conversion(args.tiff_file, args.zarr_file, args.pixel_type)