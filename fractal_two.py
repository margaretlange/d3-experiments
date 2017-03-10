import json

def make_fractal(fractal, depth, max_depth, color_type, row, col):
    print "testing fractal recursive function"
    num_rows = 3
    num_cols = 3
    white = ["1, 2", "2, 1", "2, 3", "3, 2"]
    patterned = ["1, 1", "1, 3", "2, 2", "3, 1", "3, 3"]
    if depth == max_depth:
        print "coloring black"
        fractal["color"] = "black"
        fractal["row"] = row
        fractal["col"] = col
    else:
        if color_type == "white":
            print "coloring white"
            fractal["color"] = "white"
            fractal["row"] = row
            fractal["col"] = col
        else:
            fractal["color"] = "patterned"
            fractal["row"] = row
            fractal["col"] = col
            fractal["children"] = []
            for i in range(num_rows):
                for j in range(num_cols):
                    my_row = i + 1
                    my_col = j + 1
                    str_id = str(my_row) + ", " + str(my_col)
                    print str_id
                    if str_id in white:
                        maggie_child = {}
                        make_fractal(maggie_child, depth, max_depth, "white", my_row, my_col)
                        fractal["children"].append(maggie_child)                    
                    else:
                        maggie_child = {}
                        make_fractal(maggie_child, depth+1, max_depth, "patterned", my_row, my_col)
                        fractal["children"].append(maggie_child)
                        

my_fractal = {}
make_fractal(my_fractal, 0, 2, "patterned", 1, 1)
with open("fractal.json", "w") as my_file:
    json.dump(my_fractal, my_file, indent=4, separators=(',', ': '))
print my_fractal