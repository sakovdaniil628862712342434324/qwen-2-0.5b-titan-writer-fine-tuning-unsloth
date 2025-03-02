# Titan Writer Fine-Tuning Repository
This repository contains code for fine-tuning the **Qwen 2 0.5B** model (a Chinese LLM similar to LLaMA) using the Titan Writer framework on a Russian creative writing dataset. It leverages parameter-efficient fine-tuning (PEFT) via LoRA and the Unsloth library.

## Repository Structure
```
├── README.md
├── requirements.txt
├── titan-writer.ipynb      # Script for fine-tuning the model
└── split_text_to_jsonl.py  # Utility script for splitting a large text file into JSONL chunks (default chunk size: 5500 characters)
```

## Requirements
Before running the scripts, install the required packages using:

```bash
pip install -r requirements.txt
```

The main dependencies include:
- `torch`
- `bitsandbytes`
- `accelerate`
- `xformers==0.0.29`
- `peft`
- `trl`
- `triton`
- `cut_cross_entropy`
- `unsloth_zoo`
- `unsloth`
- `sentencepiece`
- `protobuf`
- `datasets`
- `huggingface_hub`
- `hf_transfer`
- `transformers`

## Usage

### 1. Prepare Your Dataset
- Place your dataset file (in JSONL format) into a `/datasets` directory. The file should be named `titan-writer.jsonl` and contain one JSON object per line with a `"text"` field.
- If you need to convert a large text file into JSONL format, use the provided utility:

```bash
python split_text_to_jsonl.py path/to/your/input.txt path/to/output.jsonl --chunk_size 5500
```

### 2. Fine-Tune the Model
Run the training script to fine-tune the model: `titan-writer.ipynb`

This script performs the following steps:
- Loads the base model and tokenizer.
- Applies PEFT (LoRA) for efficient fine-tuning.
- Loads the dataset from `/datasets/titan-writer.jsonl`.
- Configures training parameters and starts training.
- Saves checkpoints to the `titan-writer-checkpoint` directory.
- Loads the base model in FP16.
- Loads the fine-tuned PEFT model from the specified checkpoint.
- Merges the LoRA weights into the base model.
- Saves the merged model and tokenizer to the specified output directory.

## Notes
- **Hardware Requirements:** Fine-tuning large language models generally requires a GPU with sufficient memory.
- **Model Variants:** This repository is set up for Qwen 2 0.5B. Modify the scripts if you wish to fine-tune a different model.

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
