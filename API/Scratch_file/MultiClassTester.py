import importlib
import os
from pathlib import Path


def import_classes_from_directory(directory):
    classes = {}
    for filename in os.listdir(directory):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            module_path = f"API.scripts.{module_name}"
            module = importlib.import_module(module_path)

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type):
                    classes[attr_name] = attr
    return classes


def call_custom_methods(instance):
    method_names = [func for func in dir(instance) if callable(getattr(instance, func)) and not func.startswith('_')]
    results = {}
    for method in method_names:
        method_to_call = getattr(instance, method)
        try:
            results[method] = method_to_call()
        except Exception as e:
            results[method] = str(e)
    return results


def main():
    directory = Path(__file__).parent.parent / "scripts"

    classes = import_classes_from_directory(directory)

    for class_name, cls in classes.items():
        print(f"Testing {class_name}")
        instance = cls()  # Assuming no arguments needed or defaults are sufficient
        results = call_custom_methods(instance)
        for method, result in results.items():
            print(f"Method {method} returned: {result}")


if __name__ == "__main__":
    main()
