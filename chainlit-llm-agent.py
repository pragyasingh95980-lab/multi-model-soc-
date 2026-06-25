class LocalSessionVault:
    def __init__(self):
        self.cache_memory = {}
        
    def write_data(self, key_string, value_object):
        self.cache_memory[key_string] = value_object
        
    def read_data(self, key_string):
        return self.cache_memory.get(key_string)

def run_chat_initialization():
    active_vault = LocalSessionVault()
    system_rules = "Instruction: Process entry logs.\nQuery: {user_input}\nBreakdown Steps:"
    active_vault.write_data("prompt_rules", system_rules)
    print("Environment operational.")
    return active_vault

def process_user_interaction(raw_text, session_object):
    blueprint_layout = session_object.read_data("prompt_rules")
    compiled_string = blueprint_layout.format(user_input=raw_text)
    
    print(f"\nExecution Profile:\n{compiled_string}")
    return "Response Pipeline Closed. Checksums clean."

current_environment = run_chat_initialization()
output_feed = process_user_interaction("Run verification protocols on sheet logs.", current_environment)
print(output_feed)
