import pytest
def vehicle_details(v_no,owner_name,v_type,year_manufacture):
    result=(
        f"Vehicle Number :{v_no}\n"
        f"Owner name :{owner_name}\n"
        f"Vehicle Type:{v_type}\n"
        f"Year of manufacture :{year_manufacture}\n"
    )
    return result
if __name__ == "__main__":
    #sample output
    v_no="KA001"
    owner_name="Niyati"
    v_type="Car"
    year_manufacture=2025
    print(vehicle_details(v_no, owner_name, v_type, year_manufacture))
