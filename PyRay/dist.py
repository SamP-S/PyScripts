def signedDistToCircle(point, centre, radius):
    return (centre - point).length - radius

def signedDistToBox(point, centre, size):
    offset = (point - centre).abs - size
    # dist from point outside box to edge (0 if inside box)
    unsignedDist = offset.pos.length
    # -dist from point inside box to edge (0 if outside box)
    distInsideBox = offset.neg.max
    return unsignedDist + distInsideBox