# MAMO

**MAMO** is a multi-agent collaborative molecular optimization framework that enables efficient molecular structure optimization through distributed agent cooperation.

------

## 🚀 Quick Start

### 1. Install Dify Platform

```bash
# 1. Clone repository
git clone https://github.com/langgenius/dify.git

# 2. Enter Docker directory
cd dify/docker

# 3. Start services
docker compose up -d
```

### 2. Import MAMO Workflow

```bash
# 1. Login to Dify Console → Studio → Import DSL

# 2. Select the corresponding .yml file to upload, which will generate a visual workflow.
```

### 3. Get Dify API Key

```bash
# 1. Open your application in Dify platform

# 2. Navigate to "Settings" → "API Keys"

# 3. Copy the key in format app-xxxxxxxxxxxxxx
```

### 4. Prepare Input Data

~~~bash
Create CSV file (e.g., `input.csv`) with format:
```csv
smiles
CCN(CC)CCOc1ccc(Nc2ncc3cc(-c4c(Cl)cccc4Cl)c(=O)n(C)c3n2)cc1
CCC1CC2OC(C)(C1OC)n1c3ccccc3c3c4c(c5c6ccccc6n2c5c31)C(=O)NC4O
C1CCCCC1
...(other molecule SMILES)
~~~

### 5. Run Optimization

```bash
python batch_mamo.py --file_path xxx.csv --key "app-xxx"
```

