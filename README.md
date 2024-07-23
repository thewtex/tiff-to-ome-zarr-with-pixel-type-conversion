# tiff-to-ome-zarr-with-pixel-type-conversion

> Script to convert a TIFF to OME-Zarr while simultaneously converting the pixel type

Motivated by [this thread on the Image.SC forum]().

## Installation

### Option 1: pip

```shell
pip install ngff-zarr "tifffile<2023.3.22"
```

[`tifffile` version constraint reported here.](https://github.com/cgohlke/tifffile/issues/67).

### Option 2: pixi

Install [pixi](https://pixi.sh), then

```sh
pixi install
```

## Usage

The python script/module can either be used via its command line interface
or the function `tiff_to_ome_zarr_with_pixel_type_conversion` can be used directly.

## Testing

```sh
pixi run test
```
