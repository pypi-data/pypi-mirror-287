from huggingface_hub import hf_hub_download

def download_llama3_1_8b_gguf():
    hf_hub_download("lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF", "Meta-Llama-3.1-8B-Instruct-Q8_0.gguf")
