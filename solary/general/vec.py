# Import standard librariesimport mathdef norm(vector):    # Compute the norm    norm_res = math.sqrt(sum(abs(elem)**2.0 for elem in vector))    return norm_resdef unify(vector):        vector_norm = norm(vector)        unit_vector = [vector_elem / vector_norm for vector_elem in vector]        return unit_vectordef dot_prod(vector1, vector2):    dotp_res = sum(v1_i * v2_i for v1_i, v2_i in zip(vector1, vector2))    return dotp_res