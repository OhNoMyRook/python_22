def dot_product(N, vector1, vector2):
	scalar_product_of_vector = 0
	for i in range(N):
		scalar_product_of_vector += vector1[i]*vector2[i]
	return scalar_product_of_vector
    