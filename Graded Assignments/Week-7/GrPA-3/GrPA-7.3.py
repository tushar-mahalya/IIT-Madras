def minor_matrix(M, i, j):
    # dimension of M
    n = len(M)
    # the matrix M_ij
    M_ij = [ ]
    for row in range(n):
        # skip row i
        if row == i:
            continue
        L = [ ]
        for col in range(n):
            # skip column j
            if col == j:
                continue
            # add all other elements as they are
            L.append(M[row][col])
        M_ij.append(L)
    return M_ij
