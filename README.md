# Sri Lankan Land Deed Dummy Data Generator

This Python script generates 250 realistic dummy land deed records for blockchain-based land registry research in Sri Lanka.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python generate_deed_data.py
```

## Output Files

1. **land_deeds_data.json** - Complete deed records with all details
2. **land_deeds_summary.csv** - Quick summary view in spreadsheet format

## Data Structure

Each land deed record includes:

- **Deed Information**: ID, type, registration date, office
- **Property Details**: Survey plan, lot number, extent (acres/roods/perches), land type, address, boundaries
- **Owner Information**: Current and previous owners with NIC numbers
- **Transaction Details**: Value, notary details, witnesses
- **Legal Information**: Encumbrances, stamp duty, registration fees
- **Digital Metadata**: Scan date, quality, page count
- **Blockchain Data**: Document hash (SHA-256), timestamp, verification status

## Sri Lankan Land Deed Components

The generated data includes authentic Sri Lankan elements:

- 25 districts across Sri Lanka
- Traditional land measurement (Acres, Roods, Perches)
- Sri Lankan naming conventions
- NIC number formats
- Deed types: Transfer, Mortgage, Lease, Gift, Partition, Exchange, Trust
- Land types: Residential, Agricultural, Commercial, Paddy, Tea Estate, etc.
- Survey plan formats (SP, LR, PR)
- Notary and witness information
- Boundary descriptions (North, South, East, West)


