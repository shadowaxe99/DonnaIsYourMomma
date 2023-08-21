
# Importing necessary libraries
import importlib

class ExtendibilityModularity:
    def __init__(self):
        self.modules = {}

    def load_module(self, module_name):
        try:
            module = importlib.import_module(module_name)
            self.modules[module_name] = module
            print(f"Module {module_name} loaded successfully.")
        except ImportError:
            print(f"Module {module_name} cannot be loaded.")

    def unload_module(self, module_name):
        if module_name in self.modules:
            del self.modules[module_name]
            print(f"Module {module_name} unloaded successfully.")
        else:
            print(f"Module {module_name} is not loaded.")

    def reload_module(self, module_name):
        if module_name in self.modules:
            importlib.reload(self.modules[module_name])
            print(f"Module {module_name} reloaded successfully.")
        else:
            print(f"Module {module_name} is not loaded.")

if __name__ == "__main__":
    em = ExtendibilityModularity()
    em.load_module('numpy')
    em.reload_module('numpy')
    em.unload_module('numpy')
