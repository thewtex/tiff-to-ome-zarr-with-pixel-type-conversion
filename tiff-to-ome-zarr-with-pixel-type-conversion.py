#!/usr/bin/env python3

"""
Convert a TIFF file to an OME-Zarr file with pixel type conversion.
"""

import argparse

import ngff_zarr as nz 

def main(tiff_file, zarr_file, pixel_type):
    # Input TIFF file
    tiff_file = "example.tif"
    # Output OME-Zarr file
    zarr_file = "example.zarr"
    # Convert TIFF to OME-Zarr
    nz.tiff_to_zarr(tiff_file, zarr_file, pixel_type="uint8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tiff_file", help="Input TIFF file")
    parser.add_argument("zarr_file", help="Output OME-Zarr file")
    # add choices for the pixel type to be based on the standard numpy dtypes
    parser.add_argument("--pixel_type", help="Pixel type for the output OME-Zarr file", choices=["uint8", "uint16", "uint32", "uint64", "int8", "int16", "int32", "int64", "float16", "float32", "float64"], default="float32")
    args = parser.parse_args()
    # convert the TIFF file to an OME-Zarr file

    main()