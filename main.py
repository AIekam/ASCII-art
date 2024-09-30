from PIL import Image

#CHARACTERS = " .:-=+*/#%@" 
CHARACTERS = ' .-~:+=>*#%@&$8BW'

def resize_image(image, new_width): 
    width, height = image.size
    ratio = (height / width) * 0.5 # Adjust the ratio for better ASCII representation
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))
     
def brightness_to_ascii(pixel): 
    index = (pixel // 16) # Calculate the index of ASCII character coresponding to pixel brightness (10 characters )
    return CHARACTERS[index]

image = Image.open("img/ascii-pineapple.jpg") # Choose image to display in ASCII
image = resize_image(image, new_width=600) # Resize image with resize_image() # CHANGE THE new_width VAR TO RESIZE IMAGE
width, height = image.size
image = image.convert('L') # Convert image to grayscale

image_data = list(image.getdata()) # Store the value of brightness in grayscale for each pixel

rows = [image_data[i * width:(i + 1) * width] for i in range(height)] # Put the brightness data into 2D list

ascii_art = [[brightness_to_ascii(pixel) for pixel in row] for row in rows] # Get ASCII char for every pixel and put it into 2D list

ascii_art_string = "\n".join(["".join(row) for row in ascii_art]) # Turn the ascii_art into organized string

print(ascii_art_string) # Show 