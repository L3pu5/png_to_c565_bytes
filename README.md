# png_to_c565_bytes

Requires Pillow.


Does what it says on the tin: Scronches images from png to c565 bytearray.
Does not compress in terms of resolution, samples with Pillow's pixelsAccessor.
Writes 1:1 to target, input target at desired resolution.