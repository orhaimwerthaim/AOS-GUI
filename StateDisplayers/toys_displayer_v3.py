from PIL import Image, ImageDraw,ImageFont

font_size=20
fontName = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'#"Tests/fonts/FreeMono.ttf"
default_font = ImageFont.truetype(fontName, font_size)

def display(state, filename = None,is_merging_images = False):
    # Define cell and image dimensions
    cell_size = 80
    num_rows = 8
    num_cols = 8
    image_width = num_cols * cell_size
    image_height = num_rows * cell_size

    # Create a blank image
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Define toy colors
    toy_colors = {
        "red": (255, 0, 0),
        "black": (0, 0, 0),
        "blue": (0, 0, 255),
        "green": (0, 255, 0)
    }


    # Draw labels for toy rows
    for row in range(num_rows - 1):
        toy_key = f"toy{row + 1}"
        if toy_key in state:
            toy = state[toy_key]
            toy_type = ''# toy["type"]
            toy_reward = toy["reward"]
            toy_reward_str = ""
            while toy_reward > 0:
                toy_reward_str += "$"
                toy_reward -=10

            label = f"Toy{row + 1}: {toy_type.capitalize()}"
            draw.text((0, row * cell_size+10), label, font=default_font, fill=(0, 0, 0))
            draw.text((cell_size*(num_cols-1)+10, row * cell_size + 20), toy_reward_str, font=default_font, fill=(0, 0, 0))

    # Draw label for robot row
    row=4
    draw.text((0, row * cell_size + 10), "Robot:", fill=(0, 0, 0), font=default_font)

    # Draw labels for location columns
    for col in range(num_cols):
        c= col-1
        label = f"Location {c}"
        label = f"Loc.{c}" if c < 4 else "Child" if c == 4 else  "Arm" if c == 5else "Value"
        if c < 0:
            label = f"Obj."
        row=5
        draw.text(((col) * cell_size + 10, row * cell_size + 20), label, fill=(0, 0, 0),font=default_font)

    # Draw rectangles for toys
    for row in range(num_rows - 1):
        toy_key = f"toy{row + 1}"
        if toy_key in state:
            toy = state[toy_key]
            toy_location = toy["location"]+1
            toy_type = toy["type"]
            toy_color = toy_colors[toy_type]
            x1 = toy_location * cell_size
            y1 = row * cell_size
            x2 = (toy_location + 1) * cell_size
            y2 = (row + 1) * cell_size
            draw.rectangle([x1, y1, x2, y2], fill=toy_color)

    # Draw circle for robot
    r=0
    c=0
    robot_location = state["robotLocation"]
    row = 5
    x1 = (robot_location+1) * cell_size + cell_size // 4
    y1 = (row - 1) * cell_size + cell_size // 4
    x2 = (robot_location + 2) * cell_size - cell_size // 4
    y2 = row * cell_size - cell_size // 4
    draw.ellipse([x1, y1, x2, y2], fill=(0, 0, 0))

    x = (num_cols-1)*cell_size
    y1 = 0
    y2 = num_rows * cell_size

    for col in range(num_cols):
        x = (col) * cell_size
        y1 = 0
        max_row=6
        y2 = max_row * cell_size
        if col == 1:
            draw.line([x, y1, x, y2], fill=(0, 0, 0), width=5)
        elif col > 1:
            draw.line([x,y1, x, y2], fill=(0,0,0), width=2)

    for row in range(num_rows):
        x1=0
        x2 = (col+1) * cell_size
        y = (row) * cell_size
        if row == 5:
            draw.line([x1, y, x2, y], fill=(0, 0, 0), width=5)
        elif row < 5:
            draw.line([x1,y, x2, y], fill=(0,0,0), width=2)
    image.save(filename, format='PNG')
