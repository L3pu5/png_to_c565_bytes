#
#  Converter ->  .c565 
#      By L3pu5, L3pu5_Hare
#  

from PIL import Image
from c565_chunk import c565_chunk_image
from math import floor
import sys

#Color565
def color565(r, g, b):
    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3

#Load image
def load_image(path) -> tuple[any, int, int]:
    im = Image.open(path)
    return (im.load(), im.height, im.width)

#Print the raw 565 bytes as a flat array 
#Returns a flat 
def make_buffer_from_image(img, rot: int =0) -> bytes:
    buffer = b""
    if rot == 0:
        for i in range(img[2]):
            for j in range(img[1]):
                pix = img[0][i,j]
                buffer += color565(pix[0], pix[1], pix[2]).to_bytes(2, 'big')
    elif rot == 3:
        for i in range(img.width):
            for j in range(img.height):
                pix = px[j,img.height-i-1]
                buffer += color565(pix[0], pix[1], pix[2]).to_bytes(2, 'big')
    return buffer

def build_buffer_with_chunks(img, chunk_width, chunk_height, rot: int = 0) -> bytes:
    buffer              = b""
    horizontal_chunks   = floor(img[2] / chunk_width)
    vertical_chunks     = floor(img[1] / chunk_height)
    #Do the columns:
    for chunk_y in range(vertical_chunks):
        #Do the row
        for chunk_x in range(horizontal_chunks):
            #Do the first chunk
            print(f"Buffering chunk {chunk_x}, {chunk_y}")
            for i in range(chunk_width):
                for j in range(chunk_height):
                    pix = img[0][i + (chunk_x * chunk_width), j +(chunk_y * chunk_height)]
                    buffer += color565(pix[0], pix[1], pix[2]).to_bytes(2, 'big')
    # if rot == 0:
    #     for i in range(img[2]):
    #         for j in range(img[1]):
    #             pix = img[0][i,j]
    #             buffer += color565(pix[0], pix[1], pix[2]).to_bytes(2, 'big')
    # elif rot == 3:
    #     for i in range(img.width):
    #         for j in range(img.height):
    #             pix = px[j,img.height-i-1]
    #             buffer += color565(pix[0], pix[1], pix[2]).to_bytes(2, 'big')
    return buffer

def write_chunked_buffer_to_file(write_path, png_image_tuple, chunk_width, chunk_height, buffer):
    new_image = c565_chunk_image.empty()
    new_image.set_baking_constraints_image(image_height=png_image_tuple[1], image_width=png_image_tuple[2])
    new_image.bake_with_dimensions(chunk_width, chunk_height, 2*chunk_width*chunk_height)
    new_image.accept_buffer(buffer)
    new_image.bake_to_file(write_path)

def write_buffer_to_file(buffer, path): 
    f = open(path, "wb")
    f.write(buffer)
    f.flush()
    f.close()



if __name__ == "__main__":
    png_image_tuple = load_image("../MOCKUP.png")
    buffer = build_buffer_with_chunks(png_image_tuple, 120, 80)
    write_chunked_buffer_to_file("vaccyc.c565", png_image_tuple, 120,80, buffer)
    # if(len(sys.argv) == 2):
    #     print(f"Writing {sys.argv[1]} to bytearary.")
    #     write_buffer_to_file(make_buffer_from_image(load_image(sys.argv[1])), sys.argv[1] + "_SCRONCHED")
    # elif(len(sys.argv) ==3):
    #     print(f"Writing {sys.argv[1]} to bytearary at {sys.argv[2]}.")
    #     write_buffer_to_file(make_buffer_from_image(load_image(sys.argv[1])), sys.argv[2])
    # if(len(sys.argv) == 2):
    #     print(f"Writing {sys.argv[1]} to bytearary.")
    #     write_buffer_to_file(make_buffer_from_image(load_image(sys.argv[1])), sys.argv[1] + "_SCRONCHED")
    # elif(len(sys.argv) ==3):
    #     print(f"Writing {sys.argv[1]} to bytearary at {sys.argv[2]}.")
    #     write_buffer_to_file(make_buffer_from_image(load_image(sys.argv[1])), sys.argv[2])