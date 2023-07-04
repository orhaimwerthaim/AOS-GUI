from PIL import Image, ImageDraw

def display(state, filename = None,is_merging_images = False):
    # Define cell and image dimensions
    cell_size = 80
    num_rows = 5
    num_cols = 3
    image_width = num_cols * cell_size
    image_height = num_rows * cell_size

    # Create a blank image
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Define toy colors
    colors = {
        "red": (255, 0, 0),
        "black": (0, 0, 0),
        "blue": (0, 0, 255),
        "green": (0, 255, 0)
    }

    for row in range(num_rows):
        label = f"Location{row}:"
        col=0
        if row == 4:
        	label="Got lost:"
        draw.text((col * cell_size + 10, (row) * cell_size - 30), label, fill=(0, 0, 0))
        
        
    label = f"Robot At"
    col=1
    row=0
    draw.text((col * cell_size + 10, (row) * cell_size +10), label, fill=(0, 0, 0))
    
    label = f"Visited"
    col=2
    row=0
    draw.text((col * cell_size + 10, (row) * cell_size +10), label, fill=(0, 0, 0))
    
    for l in range(3):
        loc = l+1
        name = "v" + str(loc)
        #draw.text((2 * cell_size + 10, (3) * cell_size +10), name, fill=(0, 0, 0))
        visited = state[name]["visited"]
        
        if visited:
            x1 = 2 * cell_size +4
            y1 = (loc-1) * cell_size+4
            x2 = 3 * cell_size-4
            y2 = (loc ) * cell_size-4
            tilt_y=40
            draw.rectangle([x1, y1+tilt_y, x2, y2+tilt_y], fill=colors["red"])
#    for loc in range(3):
#        name = "v" + str(loc)
#        visited = state[name]["visited"]
#        if visited:
#            x1 = 3 * cell_size
#            y1 = loc * cell_size
#            x2 = 4 * cell_size
#            y2 = (loc + 1) * cell_size
#            draw.rectangle([x1, y1, x2, y2], fill=colors["red"])
    
    # Draw circle for robot
    robot_location = state["robotLocation"]["discrete"]
    if robot_location==-1:
        robot_location=4
    x1 = robot_location * cell_size + cell_size // 4
    y1 = (num_rows - 1) * cell_size + cell_size // 4
    x2 = (robot_location + 1) * cell_size - cell_size // 4
    y2 = num_rows * cell_size - cell_size // 4
    
    y1 = (robot_location-1) * cell_size + cell_size // 4
    x1 = (num_cols - 2) * cell_size + cell_size // 4
    y2 = (robot_location) * cell_size - cell_size // 4
    x2 = (num_cols-1) * cell_size - cell_size // 4
    
    tilt_y=40
    draw.ellipse([x1, y1+tilt_y, x2, y2+tilt_y], fill=colors["blue"])
    
    
     

    image.save(filename, format='PNG')
