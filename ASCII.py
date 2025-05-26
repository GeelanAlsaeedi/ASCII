# okay so how does one come to a solution to make an image into pixels
# basically, back in the day people used to see numbers and characters only on their screen
# they didn't have any colors and pixels to showcase their images
# so how could they capture images into their devices?
# they used ASCII, represent a real-life image into a bunch of characters to show an image, right?
# but it isn't that simple, the images or even real-life objects are complex
# so one of the main things that make the image an image is
# 1 - the pixel brightness, right? even when you draw you know this
#     adding shadows or minimizing shadows can literally make you an art piece
# 2 - you need to maintain the object sizes
#     a head is a certain shape—if you don't maintain the ratio it might become an egg or even a globe
# another issue is
# 3 - the images are huge and too detailed
#     so we basically squint our eyes and resize the goddamn image to make it simpler and easier to see each pixel
# then boom you have a barefaced image
# make it grey so you can see brightness just right
# and then replace each pixel with a symbol that is similar to it in brightness
# @ is heavy and full brightness while . is darker, you see
# map this to this and that to that and then you get an ASCII image
# easy enough huh?
import PIL.Image

#define the ascii characters in more brightness --> lower brightness order 
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#1- resize the Image and maintain aspect ratio 
def resize(image, new_width=80):
    width, height = image.size #get the image current size 
    ratio = height / width #get the image current aspect ratio 
    new_height = int(new_width * ratio * 0.5 )#get the new height for the image by multiplying the new weight and the images ratio 
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

#2- make the image to grayscale
def life_out (image):
    grayscaled_img = image.convert("L")
    return(grayscaled_img)

#3- convert each greyscale pixel to an ascii character with the same intensity 
def pixel_map_ascii (image):
    pixels = image.getdata() #a function to get the image's greyscale value 
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])#loop through the pixels and assign an ascii character to each pixel 
    return(characters)

def main(new_width = 80):
    # take in an image 
    path = "ASCII\drawing256.png"
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image.")
    
    #convert image to ascii
    raw_ASCII_data = pixel_map_ascii(life_out(resize(image)))

    #format the image in aspect ratio and seperate the characters by newlines
    #seperate the lines by the desired width and the amount of line breaks will be the desired height
    pixel_count = len(raw_ASCII_data)
    ascii_image = "\n".join(raw_ASCII_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    #print result 
    print(ascii_image)

    #save result 
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 
main()