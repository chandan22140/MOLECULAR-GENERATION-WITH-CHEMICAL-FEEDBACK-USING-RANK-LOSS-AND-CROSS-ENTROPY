# MOLECULAR GENERATION WITH CHEMICAL FEEDBACK USING RANK LOSS AND CROSS ENTROPY

## Project Overview
This project focuses on generating **SELFIES** (Self-Referencing Embedded Strings) and **SMILES** (Simplified Molecular Input Line Entry System) representations of molecules using molecular descriptors as input. The generation is guided by **chemical feedback mechanisms** and optimized with **rank loss** and **cross-entropy loss** for higher accuracy and relevance.

The script processes molecular data in batches, leverages an AI API for generation, and logs the results in a structured JSON format for further analysis.

---

## Key Features
- **SELFIES and SMILES Generation**: Molecular string generation based on descriptors like `logP`, `qed`, and `SAS`.
- **Chemical Feedback Integration**: Implements molecular data-driven prompts to guide generation.
- **Rank Loss and Cross-Entropy Optimization**: Ensures output relevance and diversity in molecular representations.
- **Error Handling and Timeout Management**: Handles API failures and ensures smooth execution with defined timeouts.

---

## Prerequisites

### 1. Install Required Dependencies
Ensure Python 3.8 or later is installed. Then, install the following library:
```bash
pip install openai
```

### 2. API Key Setup
Replace the placeholder in the script with your **OpenAI API key**:
```python
api_key="YOUR_API_KEY"
```

### 3. Input Data
The input file (`cleaned_data.json`) should be structured as follows:
```json
[
  {
    "index": 1,
    "logP": 2.3,
    "qed": 0.8,
    "SAS": 3.2,
    "molecular_description": "description of molecule"
  },
  ...
]
```

---

## How to Run

### 1. Add API Credentials
Ensure the `api_key` variable in the script contains your valid API key.

### 2. Prepare Input File
Place a JSON file named `cleaned_data.json` in the same directory as the script. Ensure it adheres to the required format.

### 3. Execute the Script
Run the script as follows:
```bash
python main.py
```

### 4. Review Output
The script generates a file named `generated_results.json` with the following structure:
```json
[
  {
    "index": 1,
    "generated_selfies": "SELFIES_STRING",
    "generated_smiles": "SMILES_STRING"
  },
  ...
]
```

---

## Workflow

1. **Initialize API Client**:
   - Connect to the AI API using the provided API key.

2. **Generate Representations**:
   - For each molecule:
     - Prompt the API to generate **SELFIES** and **SMILES** strings using the molecular descriptors and descriptions.
     - Incorporate chemical feedback to refine generation.

3. **Optimize with Loss Functions**:
   - Apply rank loss and cross-entropy to ensure accuracy and diversity in the generated strings.

4. **Save and Log Results**:
   - Save outputs to `generated_results.json` for analysis and debugging.

5. **Handle Errors and Timeouts**:
   - Manage API timeouts and log errors for molecules that fail to process.

---

## Key Parameters

- **Timeout**: The timeout for each API call can be adjusted in the `call_api_with_timeout` function:
  ```python
  call_api_with_timeout(test_prompt, client, model_name, timeout=10)
  ```

- **Model Selection**: Update the `model_name` variable to switch models:
  ```python
  model_name = "your_preferred_model_name"
  ```

---

## Future Enhancements

- **Parallel Processing**: Introduce multiprocessing to handle larger datasets more efficiently.
- **Advanced Feedback Loops**: Implement a scoring mechanism for iterative molecular improvement.
- **Model Adaptation**: Support for fine-tuning models using domain-specific datasets.

---

## Dependencies
- `openai`: Used for API calls to generate SELFIES and SMILES strings.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
