from sympy import Matrix, lcm
def solve_matrix(matrix_array):
   matrix = Matrix(matrix_array)
   nullspace = matrix.nullspace()
   if len(nullspace) == 1:
      solution=matrix.nullspace()[0]
      multiple = lcm([val.q for val in solution])
      solution = multiple*solution
      coeff=[_[0] for _ in solution.tolist()]
      if 0 in coeff:
         raise ValueError('Missing product or reactant')
      return coeff
   elif len(nullspace) == 2:
      lowest_sum = ()
      for x in range(1, 21):
         for y in range(1, 21):
            solution = x*matrix.nullspace()[0] + y*matrix.nullspace()[1]
            multiple = lcm([val.q for val in solution])
            solution = multiple*solution
            coeff=[_[0] for _ in solution.tolist()]
            if not all([_ != 0 for _ in coeff]):
               continue
            if lowest_sum == () or sum(coeff) < lowest_sum[1]:
               lowest_sum = (coeff, sum(coeff))
      return lowest_sum[0]
   else:
      raise ValueError("Reaction has more than 2 degrees of freedom or is overdetermined")