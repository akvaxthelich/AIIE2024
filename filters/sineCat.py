from PIL import Image
import math

img = Image.open("cart.jpg")
img.thumbnail((250,250))

img2 = Image.new("RGB", img.size)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        color = img.getpixel((x,y))

        sined_red = 1 - int(math.sin(color[0]) * color[0])
        sined_green = 2 * int(math.sin(color[1]) * color[1])
        sined_blue = int(math.sin(color[2]) * color[2])
        sinedcolor = ((sined_red, sined_green, sined_blue))

        img2.putpixel((x,y), sinedcolor)

def spiral(image, density):
    width, height = image.size

    max_radius = min(width, height) // 2

    something = True

    spiralImg = Image.new("RGB",(width, height))

    pixels = spiralImg.load()

    for x in range(width):
        for y in range(height):

            #angle of twist is based on density and distance from center
            if(something):
                angle = density * (max_radius - min(abs(x - width * 2), abs(y - height // 2)))

            #     something = False
            # else:
            #     angle = density * (max_radius * 2 - min(abs(x - width // 2), abs(y - height // 2)))
            #     something = True
            #reposition at new cartesian coord and cast to int
            newX = int((x - width // 2) * angle / max_radius + width // 2)
            newY = int((y - height // 2) * angle / max_radius + height // 2)



            #copy from original
            if 0 <= newX < width and 0 <= newY < height:
                pixels[x,y] = image.getpixel((newX, newY))
    
    return spiralImg

def pixel_average(p):
  return int((p[0] + p[1] + p[2]) / 3) # (R+G+B)/3

def rainbow(image):
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x,y))
            pixels_average = pixel_average(pixel)
            if pixels_average >= 150:
                image.putpixel((x,y), (x+100,y+100,203))
    return image

spiral(img, 3.14).show()
