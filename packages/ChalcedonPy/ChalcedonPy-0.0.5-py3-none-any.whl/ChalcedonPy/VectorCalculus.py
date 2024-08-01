def vectorangle(vector1, vector2):
    """ Calculates the angle between two vectors. Takes in two vectors and produces the angle in degrees."""
    a_len = np.sqrt(np.sum(np.square(vector1)))
    b_len = np.sqrt(np.sum(np.square(vector2)))

    angle = np.arccos(np.dot(vector1, vector2) / (a_len * b_len))

    return angle * 180 / np.pi
