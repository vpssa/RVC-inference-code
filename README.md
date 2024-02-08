# Retrieval-based Voice Cloning (RVC) Inference Script

This repository provides a Python inference script for the Retrieval-based Voice Cloning (RVC) project. This is particularly useful for those who prefer not to use Gradio.

## Getting Started

### Prerequisites

The stable version used for this project is RVC Beta. You can download and extract it from the provided link.

### Installation

1. After downloading the RVC project and installing the requirements, paste the `infer3.py` file into the root folder.

### Configuration

The paths of the models are specified in the `.env` file. You may encounter errors if you do not expose the paths of the model from the environment. For example, for default locations, you can run the following commands:

```bash
export rmvpe_root=assets/rmvpe
export index_root=logs
export weight_uvr5_root=assets/uvr5_weights
export weight_root=assets/weights


Alternatively, you can hardcode the script with the path by removing .getenv and pasting the path as a string.

Usage
Adjust the variables as needed and you are good to go.

Resources
For more information about the RVC project, please visit the following links:

RVC Project on GitHub
https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/blob/main/docs/en/README.en.md

RVC Project on Hugging Face
https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main

i used rvc beta version, below is the link to download it
https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/RVC-beta.7z?download=true
extract it by 7z unzip application and you are good to go
