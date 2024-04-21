from vehicle import Vehicle

def test_creation_vehicle():
    veh = Vehicle('hundai', speed=500, weight=1000)
    assert isinstance(veh, Vehicle)
    assert veh.model is not None
    assert veh.info is not None