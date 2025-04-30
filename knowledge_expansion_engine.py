# knowledge_expansion_engine.py

class KnowledgeExpansionEngine:
    def __init__(self):
        self.core_knowledge = []

    def expand(self, data):
        print("📡 Expanding knowledge base...")
        for entry in data:
            self.core_knowledge.append(entry)
            print(f"➕ Added knowledge: {entry}")

    def integrate_into_core(self, memory_vault):
        for item in self.core_knowledge:
            memory_vault.store(item)
        print("🧠 Core knowledge integrated into Memory Vault.")

# Instanca engine-a
knowledge_engine = KnowledgeExpansionEngine()
