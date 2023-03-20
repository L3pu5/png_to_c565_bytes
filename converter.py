from PIL import Image
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
def make_buffer_from_image(im, rot: int =0) -> bytes:
    buffer = b""
    if rot == 0:
        for i in range(im[2]):
            for j in range(im[1]):
                pix = im[0][i,j]
                buffer += color565(pix[0], pix[1], pix[2]).to_bytes(2, 'big')
    elif rot == 3:
        for i in range(im.width):
            for j in range(im.height):
                pix = px[j,im.height-i-1]
                buffer += color565(pix[0], pix[1], pix[2]).to_bytes(2, 'big')
    return buffer

def write_buffer_to_file(buffer, path): 
    f = open(path, "wb")
    f.write(buffer)
    f.flush()
    f.close()

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        print(f"Writing {sys.argv[1]} to bytearary.")
        write_buffer_to_file(make_buffer_from_image(load_image(sys.argv[1])), sys.argv[1] + "_SCRONCHED")
    elif(len(sys.argv) ==3):
        print(f"Writing {sys.argv[1]} to bytearary at {sys.argv[2]}.")
        write_buffer_to_file(make_buffer_from_image(load_image(sys.argv[1])), sys.argv[2])