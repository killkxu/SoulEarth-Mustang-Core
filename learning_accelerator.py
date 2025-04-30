# learning_accelerator.py

class LearningAccelerator:
    def __init__(self):
        self.integrated = []

    def integrate_instantly(self, memory_vault, new_knowledge):
        print("⚡ Integrating knowledge via Learning Accelerator...")
        memory_vault.store(new_knowledge)
        self.integrated.append(new_knowledge)
        print(f"⚡ Knowledge integrated: {new_knowledge}")

# Instanca akceleratora
learning_accelerator = LearningAccelerator()
