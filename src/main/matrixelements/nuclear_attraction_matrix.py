from src.main.integrals import nuclear_attraction
from src.main.matrixelements import Matrix
import itertools


class NuclearAttractionMatrix(Matrix):

    def __init__(self, basis_set_array, nuclei_array):
        super().__init__(len(basis_set_array))
        self.basis_set_array = basis_set_array
        self.nuclei_array = nuclei_array

    def create(self):
        return self.create_matrix(self.calculate)

    def calculate(self, i, j):
        v_ij = 0
        primitives_i = self.basis_set_array[i].primitive_gaussian_array
        primitives_j = self.basis_set_array[j].primitive_gaussian_array
        for primitive_a, primitive_b in itertools.product(primitives_i, primitives_j):
            c_1 = primitive_a.contraction
            c_2 = primitive_b.contraction
            n_1 = primitive_a.normalisation
            n_2 = primitive_b.normalisation
            for nuclei in self.nuclei_array:
                v_ij += - nuclei.charge * n_1 * n_2 * c_1 * c_2 * nuclear_attraction(primitive_a, primitive_b, nuclei)
        return v_ij
