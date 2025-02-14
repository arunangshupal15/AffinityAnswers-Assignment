import re
import requests

INDIAN_STATES_UTS = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli",
    "Daman and Diu",
    "Delhi",
    "Jammu and Kashmir",
    "Ladakh",
    "Lakshadweep",
    "Puducherry",
]

# Convert the list to lowercase for easier comparison
INDIAN_STATES_UTS_LOWER = [state.lower() for state in INDIAN_STATES_UTS]


def extract_pincode(address):
    pincode_match = re.search(r"\b\d{6}\b", address)
    return pincode_match.group() if pincode_match else None


def get_state_from_address(address):
    address_lower = address.lower()
    for state in INDIAN_STATES_UTS_LOWER:
        if state in address_lower:
            return state
    return None


def validate_address(address):
    pincode = extract_pincode(address)
    print(f"Pincode: {pincode}")
    if not pincode:
        return False

    state_in_address = get_state_from_address(address)

    api_url = f"http://www.postalpincode.in/api/pincode/{pincode}"
    response = requests.get(api_url)

    if response.status_code != 200:
        return False

    data = response.json()
    if data.get("Status") != "Success":
        return False

    post_offices = data.get("PostOffice", [])
    if not post_offices:
        return False

    address_lower = address.lower()
    post_office_names = [po["Name"].lower() for po in post_offices]
    state_names = [po["State"].lower() for po in post_offices]
    district_names = [po.get("District", "").lower() for po in post_offices]
    division_names = [po.get("Division", "").lower() for po in post_offices]
    region_names = [po.get("Region", "").lower() for po in post_offices]
    taluk_names = [po.get("Taluk", "").lower() for po in post_offices]
    circle_names = [po.get("Circle", "").lower() for po in post_offices]

    # Combine all location-related fields for validation
    location_fields = (
        post_office_names
        + district_names
        + division_names
        + region_names
        + taluk_names
        + circle_names
    )

    # Validate based on presence of state in address
    if state_in_address:
        if state_in_address in state_names:
            for name in location_fields:
                if name and name in address_lower:
                    return True
        return False
    else:
        # If state is not in address, validate using location fields only
        for name in location_fields:
            if name and name in address_lower:
                return True

    return False


# Test the function with sample addresses
address_correct = "D-89, NH-2, NTPC Township, Madhya Pradesh 486885"
address_incorrect = "Colony, Bengaluru, Karnataka 560050"

print(validate_address(address_correct))  # Output: True
print(validate_address(address_incorrect))  # Output: False
