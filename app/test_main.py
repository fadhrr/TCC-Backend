from fastapi.testclient import TestClient
import re
from .main import app

client = TestClient(app)

# Fungsi untuk mendapatkan semua endpoint "GET" dari semua router yang telah Anda daftarkan
def get_all_get_endpoints():
    endpoints = []
    print("Getting all endpoints\n")
    # print("app.routes: ", app.routes, "\n")
    for route in app.routes:
        print("route: ", route, "\n")
        if 'GET' in route.methods and route.path.startswith('/'):
            endpoints.append(route.path)
    return endpoints

# Fungsi untuk menguji semua endpoint "GET"
def test_all_get_endpoints():
    endpoints = get_all_get_endpoints()
    print(f"Testing {len(endpoints)} endpoints\n")
    for endpoint in endpoints:
        print(f"Testing {endpoint}\n")
        endpoint = re.sub(r'\{(.*?)\}', '1', endpoint)
        response = client.get(endpoint)
        assert response.status_code == 200, f"Failed to get {endpoint}. Status code: {response.status_code}"