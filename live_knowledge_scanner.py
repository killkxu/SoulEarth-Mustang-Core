# live_knowledge_scanner.py
class LiveKnowledgeScanner:
    def __init__(self):
        self.sources = [
            "https://www.sciencedaily.com",
            "https://www.nature.com",
            "https://arxiv.org",
            "https://www.pubmed.ncbi.nlm.nih.gov"
        ]

    def scan_sources(self):
        findings = []
        for source in self.sources:
            findings.append((source, "Simulirani novi podaci sa izvora"))
        return findings

    def log_results(self, findings, memory_logger):
        for source, content in findings:
            memory_logger.log_event(f"Novi podaci pronađeni: {source} → {content}")

live_scanner = LiveKnowledgeScanner()
