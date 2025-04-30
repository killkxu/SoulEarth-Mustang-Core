def run_pipeline(memory_vault, memory_logger):
    try:
        for knowledge in memory_vault.retrieve_all():
            # Simulacija obrade svakog podatka
            print(f"📝 LOGGED: Pipeline processed: {knowledge}")
            memory_logger.log_event(f"Pipeline processed: {knowledge}")
        print("🌐 Global data stream successfully processed.\n")
        memory_logger.log_event("Global Data Pipeline Completed.")
    except Exception as e:
        print(f"❌ Pipeline Error: {e}")
        memory_logger.log_event(f"Pipeline Error: {e}")
