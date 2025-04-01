from sympy import *
from sympy.parsing.latex import parse_latex

def solve_math_expression():
    """Takes LaTeX input from user, detects concept, and solves it."""
    try:
        expression = input("Enter LaTeX mathematical expression: ")
        sympy_expr = parse_latex(expression)  # Convert LaTeX to SymPy expression
        
        # Check for different types of operations
        if isinstance(sympy_expr, Derivative):
            solution = sympy_expr.doit()
            concept = "Derivative"
        elif isinstance(sympy_expr, Integral):
            solution = sympy_expr.doit()
            concept = "Integral"
        elif isinstance(sympy_expr, Sum):
            solution = sympy_expr.doit()
            concept = "Summation"
        elif isinstance(sympy_expr, Limit):
            solution = sympy_expr.doit()
            concept = "Limit"
        elif isinstance(sympy_expr, Eq):
            solution = solve(sympy_expr)
            concept = "Equation Solution"
        else:
            solution = simplify(sympy_expr)  # Default simplification
            concept = "General Computation"
        
        print(f"\nConcept Detected: {concept}")
        print(f"Solution: {solution}\n")
    
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the function if executed as a script
if __name__ == "__main__":
    solve_math_expression()
