# memory_expansion.py

class MemoryExpansion:
    def __init__(self):
        self.knowledge_modules = []

    def expand_with(self, module):
        print(f"📚 Integrating memory module: {module}")
        self.knowledge_modules.append(module)

    def get_all_modules(self):
        return self.knowledge_modules

memory_vault = MemoryExpansion()
