
import threading
import time
import json
from openai import OpenAI 

client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key="API_key"  # Replace with your API key
)

def call_api_with_timeout(prompt, client, model_name, timeout=5):
    result = {"response": None, "error": None}

    def api_call():
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0
            )
            result["response"] = response.choices[0].message.content.strip().split("\n")[0]
        except Exception as e:
            result["error"] = str(e)

    api_thread = threading.Thread(target=api_call)
    api_thread.start()

    api_thread.join(timeout=timeout)

    if api_thread.is_alive():
        return None, "Timeout: API call took longer than allowed time"
    else:
        return result["response"], result["error"]


model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1-fast"
with open("cleaned_data.json", "r") as f:
    data = json.load(f)

# List to store the results
results = []

for i in range(1000):
    entry = data[i]
    idx = entry["index"]
    logP = entry["logP"]
    qed = entry["qed"]
    SAS = entry["SAS"]
    molecular_description = entry["molecular_description"]

    print("============================", i, "=======================================")

    # Generate SELFIES
    test_prompt_1 = f"""
    You are a chemical informatics assistant. Based on the following molecular data, generate the corresponding SELFIES string.
    Input:
    logP: {logP},
    qed: {qed},
    SAS: {SAS},
    molecular_description: "{molecular_description}"
    Output:
    SELFIES string only, without any additional text or explanations.
    """
    selfies_response, selfies_error = call_api_with_timeout(test_prompt_1, client, model_name, timeout=5)
    if selfies_error:
        print(f"SELFIES Error: {selfies_error}")
        selfies_response = None

    # Generate SMILES
    test_prompt_2 = f"""
    You are a chemical informatics assistant. Based on the following molecular data, generate the corresponding SMILES string.
    Input:
    logP: {logP},
    qed: {qed},
    SAS: {SAS},
    molecular_description: "{molecular_description}"
    Output:
    SMILES string only, without any additional text or explanations.
    """
    smiles_response, smiles_error = call_api_with_timeout(test_prompt_2, client, model_name, timeout=5)
    if smiles_error:
        print(f"SMILES Error: {smiles_error}")
        smiles_response = None

    # Add the result to the list
    results.append({
        "index": idx,
        "generated_selfies": selfies_response,
        "generated_smiles": smiles_response
    })
    if i%10 == 0:
        print(selfies_response)
        print(smiles_response)

# Save results to a JSON file
output_file = "generated_results.json"
with open(output_file, "w") as f:
    json.dump(results, f, indent=4)

print(f"Results saved to {output_file}")

