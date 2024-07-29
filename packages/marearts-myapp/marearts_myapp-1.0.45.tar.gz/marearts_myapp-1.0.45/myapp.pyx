# cython: language_level=3
# distutils: language = c

def sensitive_function(x):
    return x * 2

cpdef int cy_sensitive_function(int x):
    return sensitive_function(x)

def main():
    result = cy_sensitive_function(10)
    print(f"Result: {result}")

# Ensure the module is importable
def __getattr__(name):
    if name == 'main':
        return main
    raise AttributeError(f"module 'marearts_myapp_compiled' has no attribute '{name}'")