## Prerequisites
- Install Miniconda: https://docs.conda.io/en/latest/miniconda.html

## Setup

### Step 1 — (Optional) Update Conda
conda update -n base -c defaults conda

### Step 2 — Create the environment
conda env create -f env_py311_full.yml

### Step 3 — Activate the environment
conda activate ds_310_hcds1

### Step 4 — Run the Streamlit app
streamlit run streamlit.py