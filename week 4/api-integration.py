import json

def process_system_prompt(input_text, character_setup="Role: Factory Database Assistant."):
    api_request_payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": character_setup},
            {"role": "user", "content": input_text}
        ],
        "temperature": 0.0
    }
    
    simulated_server_response = {
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Database Action: Logs recorded successfully. Discrepancies solved."
            }
        }]
    }
    
    extracted_text_block = simulated_server_response["choices"]["message"]["content"]
    return extracted_text_block

query_message = "Cross reference thermal logs for Grid Area 9."
final_verdict = process_system_prompt(query_message)
print(final_verdict)
