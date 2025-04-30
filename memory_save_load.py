import json
import os

class MemoryVault:
    def __init__(self):
        self.memory_data = []
        self.save_file = "memory_data.json"

    def store(self, entry):
        self.memory_data.append(entry)

    def retrieve_all(self):
        return self.memory_data

    def save_memory(self):
        try:
            with open(self.save_file, 'w') as f:
                json.dump(self.memory_data, f, indent=4)
            print("💾 Memory successfully saved.")
        except Exception as e:
            print(f"❌ Error saving memory: {e}")

    def load_memory(self):
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as f:
                    self.memory_data = json.load(f)
                print("📂 Memory successfully loaded.")
            except Exception as e:
                print(f"❌ Error loading memory: {e}")
        else:
            print("⚠️ No saved memory found.")

memory_vault = MemoryVault()
