import json
import random
from datetime import datetime, timedelta
from faker import Faker
import hashlib

# Initialize Faker with locale support
fake = Faker()

# Sri Lankan specific data
DISTRICTS = [
    "Colombo", "Gampaha", "Kalutara", "Kandy", "Matale", "Nuwara Eliya",
    "Galle", "Matara", "Hambantota", "Jaffna", "Kilinochchi", "Mannar",
    "Vavuniya", "Mullaitivu", "Batticaloa", "Ampara", "Trincomalee",
    "Kurunegala", "Puttalam", "Anuradhapura", "Polonnaruwa", "Badulla",
    "Monaragala", "Ratnapura", "Kegalle"
]

DEED_TYPES = [
    "Transfer Deed", "Mortgage Deed", "Lease Deed", "Gift Deed",
    "Partition Deed", "Exchange Deed", "Trust Deed"
]

LAND_TYPES = [
    "Residential", "Agricultural", "Commercial", "Industrial",
    "Plantation", "Paddy Land", "Coconut Estate", "Tea Estate"
]

SURVEY_PLANS = ["SP", "LR", "PR"]

def generate_sri_lankan_name():
    """Generate realistic Sri Lankan names"""
    first_names = [
        "Nimal", "Kamal", "Sunil", "Anil", "Pradeep", "Chaminda", "Ruwan",
        "Saman", "Kumara", "Bandara", "Silva", "Perera", "Fernando",
        "Jayawardena", "Wickramasinghe", "Rajapaksa", "Dissanayake",
        "Amarasinghe", "Gunasekara", "Mendis"
    ]
    last_names = [
        "Silva", "Perera", "Fernando", "Jayawardena", "Wickramasinghe",
        "Rajapaksa", "Dissanayake", "Amarasinghe", "Gunasekara", "Mendis",
        "De Silva", "Wijesinghe", "Gunawardena", "Senanayake", "Ranasinghe"
    ]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_nic():
    """Generate Sri Lankan NIC number"""
    year = random.randint(50, 99)
    days = random.randint(1, 366)
    suffix = random.choice(['V', 'X'])
    return f"{year}{days:03d}{random.randint(1000, 9999)}{suffix}"

def generate_deed_number():
    """Generate deed registration number"""
    year = random.randint(1990, 2024)
    return f"D/{year}/{random.randint(1000, 99999)}"

def generate_survey_plan():
    """Generate survey plan number"""
    plan_type = random.choice(SURVEY_PLANS)
    district_code = random.randint(1, 25)
    number = random.randint(1000, 99999)
    return f"{plan_type}/{district_code}/{number}"

def generate_lot_number():
    """Generate lot number"""
    return f"LOT-{random.randint(1, 500)}"

def generate_extent():
    """Generate land extent in acres, roods, and perches"""
    acres = random.randint(0, 10)
    roods = random.randint(0, 3)
    perches = random.randint(0, 39)
    return f"{acres}A {roods}R {perches}P"

def generate_address(district):
    """Generate Sri Lankan address"""
    street_num = random.randint(1, 500)
    street_names = ["Galle Road", "Kandy Road", "Main Street", "Temple Road",
                   "Station Road", "Lake Road", "Hill Street", "Park Avenue"]
    return f"{street_num}, {random.choice(street_names)}, {district}"

def generate_document_hash(deed_data):
    """Generate SHA-256 hash for the deed document"""
    data_string = json.dumps(deed_data, sort_keys=True)
    return hashlib.sha256(data_string.encode()).hexdigest()

def generate_random_date(start_year=1990, end_year=2024):
    """Generate random date"""
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generate_land_deed():
    """Generate a complete land deed record"""
    district = random.choice(DISTRICTS)
    deed_type = random.choice(DEED_TYPES)
    registration_date = generate_random_date(1990, 2024)
    
    deed = {
        "deed_id": generate_deed_number(),
        "deed_type": deed_type,
        "registration_date": registration_date,
        "registration_office": f"{district} Land Registry",
        "district": district,
        
        "property_details": {
            "survey_plan": generate_survey_plan(),
            "lot_number": generate_lot_number(),
            "extent": generate_extent(),
            "land_type": random.choice(LAND_TYPES),
            "address": generate_address(district),
            "boundaries": {
                "north": f"Property of {generate_sri_lankan_name()}",
                "south": f"Property of {generate_sri_lankan_name()}",
                "east": random.choice(["Main Road", "Canal", "Railway Line", f"Property of {generate_sri_lankan_name()}"]),
                "west": random.choice(["River", "Path", "Government Land", f"Property of {generate_sri_lankan_name()}"])
            }
        },
        
        "current_owner": {
            "name": generate_sri_lankan_name(),
            "nic": generate_nic(),
            "address": generate_address(district)
        },
        
        "previous_owner": {
            "name": generate_sri_lankan_name(),
            "nic": generate_nic(),
            "address": generate_address(district)
        } if deed_type in ["Transfer Deed", "Gift Deed"] else None,
        
        "transaction_value": random.randint(500000, 50000000) if deed_type in ["Transfer Deed", "Mortgage Deed"] else None,
        
        "notary_details": {
            "name": f"Notary {generate_sri_lankan_name()}",
            "license_number": f"NP/{random.randint(1000, 9999)}",
            "office_address": generate_address(district)
        },
        
        "witnesses": [
            {
                "name": generate_sri_lankan_name(),
                "nic": generate_nic(),
                "address": generate_address(district)
            }
            for _ in range(2)
        ],
        
        "encumbrances": random.choice([None, "Mortgage", "Lease", "Right of Way"]),
        "stamp_duty_paid": random.randint(10000, 500000),
        "registration_fee": random.randint(5000, 50000),
        
        "digital_metadata": {
            "scanned_date": generate_random_date(2020, 2024),
            "scan_quality": random.choice(["High", "Medium"]),
            "page_count": random.randint(2, 15),
            "file_format": "PDF"
        }
    }
    
    # Add document hash
    deed["document_hash"] = generate_document_hash(deed)
    deed["blockchain_timestamp"] = datetime.now().isoformat()
    deed["verification_status"] = random.choice(["Verified", "Pending", "Verified"])
    
    return deed

def main():
    """Generate 250 land deed records"""
    print("Generating 250 dummy land deed records for Sri Lankan blockchain system...")
    
    deeds = []
    for i in range(250):
        deed = generate_land_deed()
        deeds.append(deed)
        if (i + 1) % 50 == 0:
            print(f"Generated {i + 1} records...")
    
    # Save to JSON file
    output_file = "land_deeds_data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(deeds, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Successfully generated 250 land deed records!")
    print(f"✓ Data saved to: {output_file}")
    
    # Generate summary statistics
    print("\n--- Summary Statistics ---")
    print(f"Total Records: {len(deeds)}")
    print(f"Districts Covered: {len(set(d['district'] for d in deeds))}")
    print(f"Deed Types: {len(set(d['deed_type'] for d in deeds))}")
    print(f"Date Range: {min(d['registration_date'] for d in deeds)} to {max(d['registration_date'] for d in deeds)}")
    
    # Save a sample CSV for quick viewing
    import csv
    csv_file = "land_deeds_summary.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Deed ID', 'Type', 'District', 'Owner', 'Extent', 'Registration Date', 'Document Hash'])
        for deed in deeds:
            writer.writerow([
                deed['deed_id'],
                deed['deed_type'],
                deed['district'],
                deed['current_owner']['name'],
                deed['property_details']['extent'],
                deed['registration_date'],
                deed['document_hash'][:16] + '...'
            ])
    
    print(f"✓ Summary CSV saved to: {csv_file}")

if __name__ == "__main__":
    main()
