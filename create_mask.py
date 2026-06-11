from PIL import Image, ImageDraw

width = 320
height = 600

img = Image.new('L', (width, height), 0)
draw = ImageDraw.Draw(img)

draw.ellipse((100, 30, 220, 130), fill=255)
draw.ellipse((40, 80, 100, 160), fill=255)
draw.ellipse((220, 80, 280, 160), fill=255)
draw.rectangle((60, 160, 260, 480), fill=255)
draw.ellipse((80, 460, 130, 540), fill=255)
draw.ellipse((190, 460, 240, 540), fill=255)

img.save('model_mask.png')
print("model_mask.png created successfully!")