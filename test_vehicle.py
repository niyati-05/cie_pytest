from vehicle import vehicle_details
def test_vehicle_details():
    expected_output = (
        "Vehicle Number :KA001\n"
        "Owner name :Niyati\n"
        "Vehicle Type:car\n"
        "Year of manufacture :2025\n"
    )

    assert vehicle_details("KA001","Niyati","car",2025) == expected_output
