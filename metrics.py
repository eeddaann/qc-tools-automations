import gzip
import xml.etree.ElementTree as ET

def extract_metrics(path):
    # TODO: catch exceptions
    min_y, min_u, min_v = float('inf'), float('inf'), float('inf')
    max_y, max_u, max_v = 0, 0, 0

    inp = gzip.open(path, 'r')
    tree = ET.parse(inp)
    root = tree.getroot()

    frames = list(root)[2]
    for frame in list(frames):
        for tag in list(frame):
            field = tag.attrib
            if field['key'] == 'lavfi.signalstats.YMIN':
                min_y = min(float(field['value']),min_y)
            elif field['key'] == 'lavfi.signalstats.YMAX':
                max_y = max(float(field['value']),max_y)
            elif field['key'] == 'lavfi.signalstats.UMIN':
                min_u = min(float(field['value']),min_u)
            elif field['key'] == 'lavfi.signalstats.UMAX':
                max_u = max(float(field['value']),max_u)
            elif field['key'] == 'lavfi.signalstats.VMIN':
                min_v = min(float(field['value']),min_v)
            elif field['key'] == 'lavfi.signalstats.VMAX':
                max_v = max(float(field['value']),max_v)
    d = {
        "min_y": min_y,
        "max_y": max_y,
        "min_u": min_u,
        "max_u": max_u,
        "min_v": min_v,
        "max_v": max_v 
    }
    return d