from PIL import Image
import sys

try:
    if len(sys.argv) < 2:
        sys.stderr.write("No Args")
        sys.exit(1)
    
    img = Image.open(sys.argv[1])

    for j in range(img.height):
        for i in range(img.width):
            r, g, b, a = img.getpixel((i, j))
            val = (r << 16) + (g << 8) + b
            hex_val = format(val, '06x')
            if val == 0:
                print("0," + hex_val, end=" ")
            else:
                print("10," + "0x" + hex_val, end=" ")
        print() #newline

except Exception as ex:
    print("Error:", ex)