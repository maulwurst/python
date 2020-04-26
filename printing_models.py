def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after pritning.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # Simulate creating a 3D print from desgin.
        print("Printing model:" + current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_desings = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_desings, completed_models)
show_completed_models(completed_models)
