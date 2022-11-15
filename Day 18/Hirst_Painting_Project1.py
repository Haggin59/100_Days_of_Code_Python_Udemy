import colorgram

colors = colorgram.extract('damien-hirst-lactulose.jpg', 30)

colors_rgb = []

for i in range(30):
    
    r = colors[i].rgb[0]
    g = colors[i].rgb[1]
    b = colors[i].rgb[2]

    temp_color = (r,g,b)

    colors_rgb.append(temp_color)

print(colors_rgb)