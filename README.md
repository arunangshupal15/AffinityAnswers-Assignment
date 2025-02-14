# # AffinityAnswers Assignment

## Contents

### 1. NAV Data Extractor (`extract.sh`)
A shell script for extracting Net Asset Value (NAV) data from AMFI (Association of Mutual Funds in India).

**Features:**
- Fetches real-time NAV data from AMFI website
- Extracts Scheme Name and Net Asset Value
- Outputs data in TSV (Tab-Separated Values) format
- Includes detailed commentary on data format considerations (JSON vs TSV)

**Usage:**
```bash
./extract.sh
```
The script will create a `nav_data.tsv` file in the current directory.

### 2. Rfam Database Queries (`rfam dataset sql.txt`)
A collection of SQL queries for analyzing the Rfam database, which contains RNA families data.

**Included Queries:**
- Species counting for Panthera tigris
- NCBI ID retrieval for specific subspecies
- Maximum sequence length analysis for Oryza species
- Complex family analysis for DNA sequences with specific length criteria

### 3. Indian Address Validator (`pincode.py`)
A Python script for validating Indian addresses using pincode verification and location matching.

**Features:**
- Pincode extraction and validation
- State detection from address string
- Integration with postal API for verification
- Comprehensive location field validation
- Support for all Indian states and Union Territories

**Requirements:**
```
requests
re
```

**Usage:**
```python
# Example usage
address = "D-89, NH-2, NTPC Township, Madhya Pradesh 486885"
#All the addresses in assignment given
#D-89, NH-2, NTPC Township, Bihar 486885 (Wrong)
#B-8, Digantika Abasan, Saltlake, Kolkata 700091 (Wrong)
#B-8, Digantika Abasan 700091 (Wrong)
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Install Python requirements (for pincode validator):
```bash
pip install requests
```

3. Make the shell script executable:
```bash
chmod +x extract.sh
```

