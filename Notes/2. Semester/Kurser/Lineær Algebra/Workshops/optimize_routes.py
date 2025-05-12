import numpy as np
from scipy.optimize import linprog


def optimize_routes(C, P, D):
    """
    Solves the linear programming problem for network routing.

    This function finds the optimal solution for routing given demands through
    a network as specified in the Workshop.

    Args:
        C: Matrix where capacity of arc (i,j) is C[i,j]
        P: Matrix where price of arc (i,j) is P[i,j]
        D: Matrix where the demand from i to j is D[i,j]

    Returns:
        solution: The values of the variables in the solution as a vector. The
                variables are ordered according to the demand matrix (in row-
                wise fashion), and then according to arc ordering in C.
        value: The value of the problem.
    """
    # Check if matrices have the same dimensions
    if (
        C.shape[0] != C.shape[1]
        or P.shape[0] != P.shape[1]
        or D.shape[0] != D.shape[1]
        or C.shape[0] != P.shape[0]
        or C.shape[0] != D.shape[0]
        or P.shape[0] != D.shape[0]
    ):
        raise ValueError("Matrices C, P, and D must be square and of same dimensions!")

    # Count non-zero demands (number of routes)
    n_routes = np.count_nonzero(D)
    n_nodes = C.shape[0]
    n_arcs = C.size

    # Form the objective function by concatenating the rows of P as many times
    # as there are routes in the demand matrix
    f = np.tile(P.T.reshape(-1), n_routes)

    # Add the edge capacity constraints to the matrix A and vector b
    # The constraint is that the sum of flow on an arc across all demands
    # must not exceed the capacity of that arc
    A_capacity = np.zeros((n_arcs, n_routes * n_arcs))
    for i in range(n_arcs):
        for j in range(n_routes):
            A_capacity[i, i + j * n_arcs] = 1
    b_capacity = C.T.reshape(-1)

    # Construct a matrix containing the conditions on preservation of data through
    # each vertex, for each demand
    A_preserve = np.kron(np.eye(n_nodes), np.ones((1, n_nodes))) - np.tile(
        np.eye(n_nodes), (1, n_nodes)
    )
    A_preserve = np.kron(np.eye(n_routes), A_preserve)

    # Initialize the right-hand side for flow preservation constraints
    b_preserve = np.array([])

    # Construct the matrix ensuring that demands are met
    A_demand = np.array([]).reshape(0, n_routes * n_arcs)
    b_demand = np.array([])

    # Helper function to create canonical basis vector
    def cbv(n, i):
        """Return the i-th canonical basis vector of R^n"""
        v = np.zeros(n)
        v[i - 1] = 1  # Convert to 0-indexed
        return v

    # Loop over all entries in D to find the nonzero demands
    count = 0
    for i in range(1, n_nodes + 1):
        for j in range(1, n_nodes + 1):
            if D[i - 1, j - 1] == 0:
                continue

            # Fill in demand in b_preserve
            source_cbv = cbv(n_nodes, i)
            dest_cbv = cbv(n_nodes, j)
            b_preserve = np.append(
                b_preserve, D[i - 1, j - 1] * (source_cbv - dest_cbv)
            )

            all_ones = np.ones(n_nodes)

            # Source constraint
            tmp_mat_source = np.kron(cbv(n_nodes, i), all_ones)

            # Destination constraint
            tmp_mat_dest = np.kron(all_ones, cbv(n_nodes, j))

            # Create a block for the current route
            route_block = np.zeros((2, n_routes * n_arcs))
            route_block[0, count * n_arcs : (count + 1) * n_arcs] = tmp_mat_source
            route_block[1, count * n_arcs : (count + 1) * n_arcs] = tmp_mat_dest

            # Add block to A_demand
            if A_demand.size == 0:
                A_demand = route_block
            else:
                A_demand = np.vstack((A_demand, route_block))

            b_demand = np.append(b_demand, [D[i - 1, j - 1], D[i - 1, j - 1]])
            count += 1

    # Combine constraints
    A_eq = np.vstack((A_preserve, A_demand))
    b_eq = np.concatenate((b_preserve, b_demand))

    # Define lower bound to ensure that all variables are positive
    lb = np.zeros(len(f))

    # Solve linear programming problem
    # Ensure all arrays have the right shape
    f = f.flatten()
    b_capacity = b_capacity.flatten()
    b_eq = b_eq.flatten()

    result = linprog(
        f,
        A_ub=A_capacity,
        b_ub=b_capacity,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=(0, None),
        method="highs",
    )

    solution = result.x
    value = result.fun

    if len(solution) == 0:
        # No solution was found
        return None, None

    # Check if value is an integer
    is_integer = lambda n: n == int(n)

    if is_integer(value):
        print(f"Problem value is {int(value)}.\n")
    else:
        print(f"Problem value is {value}.\n")

    # Present solution in matrix form
    count = 0
    for i in range(1, n_nodes + 1):
        for j in range(1, n_nodes + 1):
            if D[i - 1, j - 1] == 0:
                continue
            print(f"Routing {D[i-1, j-1]:.2f} from vertex {i} to vertex {j} via arcs:")
            entries = solution[count * n_arcs : (count + 1) * n_arcs]
            print(np.reshape(entries, (n_nodes, n_nodes)).T)
            count += 1

    return solution, value


# Example usage
if __name__ == "__main__":
    # Define example matrices
    C = np.array(
        [
            [0, 0, 25, 0, 0, 0, 0, 0],
            [5, 0, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 20, 0, 10, 0, 0],
            [0, 8, 20, 0, 10, 15, 0, 12],
            [0, 0, 15, 0, 0, 12, 0, 0],
            [0, 0, 0, 0, 12, 0, 8, 0],
            [5, 0, 0, 0, 15, 0, 0, 0],
            [0, 0, 0, 12, 0, 8, 15, 0],
        ]
    )

    P = np.array(
        [
            [0, 0, 6, 0, 0, 0, 0, 0],
            [3, 0, 0, 4, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 8, 0, 0],
            [0, 3, 6, 0, 10, 6, 0, 10],
            [0, 0, 5, 0, 0, 8, 0, 0],
            [0, 0, 0, 0, 8, 0, 4, 0],
            [3, 0, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 10, 0, 4, 5, 0],
        ]
    )

    D = np.array(
        [
            [0, 0, 0, 0, 0, 20, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 0, 0],
        ]
    )

    print("Optimizing routes...")
    solution, value = optimize_routes(C, P, D)
    if solution is not None:
        print("Solution found.")
    else:
        print("No solution found.")
