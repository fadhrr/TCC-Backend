from fastapi.testclient import TestClient
import re
from .main import app
import time

client = TestClient(app)

# # # # # # # ============== Test User ============== # # # # # # # 
# test read all users
def test_read_all_users():
    response = client.get("/api/users")
    assert response.status_code == 200


def test_read_all_users_with_role():
    response = client.get("/api/users/role")
    assert response.status_code == 200
    
def test_read_user():
    response = client.get("/api/user/1")
    assert response.status_code == 200

def test_read_user_not_found():
    response = client.get("/api/user/100")
    assert response.status_code == 404
    
userTestingId = "userTesting1"
def test_write_user():
    response = client.post("/api/user", json={"id":"usertesting", "name": "usertest", "nim": "123", "score": 100, "email": "usertesting@gmail.com"})
    response = client.post("/api/user", json={"id":userTestingId, "name": "usertest1", "nim": "1231", "score": 100, "email": "usertesting1@gmail.com"})
    assert response.status_code == 200
    
def test_update_user():
    response = client.put("/api/user/usertesting", json={"name": "usertest", "nim": "123", "score": 100, "email": "usertesting2@gmail.com"})
    assert response.status_code == 200

def test_update_user_not_found():
    response = client.put("/api/user/100", json={"name": "usertest", "nim": "123", "score": 100, "email": "usertesting2@gmail.com"})
    assert response.status_code == 404

def test_delete_user():
    response = client.delete("/api/user/usertesting")
    assert response.status_code == 200

def test_leaderboard():
    response = client.get("/api/leaderboard")
    assert response.status_code == 200


# # # # # # # ============== Test Admin ============== # # # # # # #
def test_read_all_admins():
    response = client.get("/api/admins")
    assert response.status_code == 200

def test_read_admin():
    response = client.get("/api/admin/2")
    assert response.status_code == 200

def test_read_admin_not_found():
    response = client.get("/api/admin/100")
    assert response.status_code == 404

def test_write_admin():
    response = client.post("/api/admin", json={"id":userTestingId, "user_id": userTestingId, "role": 1})
    assert response.status_code == 200

def test_delete_admin():
    response = client.delete(f"/api/admin/{userTestingId}")
    assert response.status_code == 200
    
def test_read_role_assistants():
    response = client.get("/api/role/assistants")
    assert response.status_code == 200

def test_read_role_admins():
    response = client.get("/api/role/admins")
    assert response.status_code == 200

# # # # # # # ============== Test Problems ============== # # # # # # #
def test_read_all_problems():
    response = client.get("/api/problems")
    assert response.status_code == 200

def test_read_problem():
    response = client.get("/api/problem/1")
    assert response.status_code == 200
    
def test_read_problem_not_found():
    response = client.get("/api/problem/1000")
    assert response.status_code == 404

def test_write_update_delete_problem():
    response = client.post("/api/problem", json={"title":"Problem 1", "description": "Problem 1 description", "time_limit": 1, "memory_limit": 1, "input_format": "input format", "sample_input": "sample input", "output_format": "output format", "sample_output": "sample output", "constraints": "constraints", "explanation": "explanation"})
    testProblem_id = response.json()['data']['id']
    assert response.status_code == 200
    response = client.put(f"/api/problem/{testProblem_id}", json={"title":"Problem 1", "description": "Problem 1 description", "time_limit": 1, "memory_limit": 1, "input_format": "input format", "sample_input": "sample input", "output_format": "output format", "sample_output": "sample output", "constraints": "constraints", "explanation": "explanation"})
    assert response.status_code == 200
    response = client.delete(f"/api/problems/{testProblem_id}")
    assert response.status_code == 200

def test_update_problem_not_found():
    response = client.put("/api/problem/1000", json={"title":"Problem 1", "description": "Problem 1 description", "time_limit": 1, "memory_limit": 1, "input_format": "input format", "sample_input": "sample input", "output_format": "output format", "sample_output": "sample output", "constraints": "constraints", "explanation": "explanation"})
    assert response.status_code == 404

def test_search_problem():
    response = client.get("/api/problems/search?q=Bilangan")
    assert response.status_code == 200

def test_read_problem_by_category():
    response = client.get("/api/problems/categories/1")
    assert response.status_code == 200
    
def test_write_problem_category():
    response = client.post("/api/problems/1/categories/1")
    assert response.status_code == 200
    
def test_delete_problem_category():
    response = client.delete("/api/problems/1/categories/1")
    assert response.status_code == 200
    
    
    

# # # # # # # ============== Test Submissions ============== # # # # # # #
def test_read_all_submissions():
    response = client.get("/api/submissions")
    assert response.status_code == 200
    
def test_read_submission():
    response = client.get("/api/submission/1")
    assert response.status_code == 200

def test_read_submission_not_found():
    response = client.get("/api/submission/1000")
    assert response.status_code == 404


def test_write_update_delete_submission():
    response = client.post("/api/submission", json={"user_id":"1", "problem_id": 1, "language_id": 3,"time": 0,"memory": 0, "code": "print('Hello World')"})
    testSubmission_id = response.json()['data']['id']
    assert response.status_code == 200
    response = client.delete(f"/api/submission/{testSubmission_id}")
    assert response.status_code == 200

# # # # # # # ============== Test Contests ============== # # # # # # #
def test_read_all_contests():
    response = client.get("/api/contests")
    assert response.status_code == 200
    
def test_read_contest():
    response = client.get("/api/contest/1")
    assert response.status_code == 200

def test_read_contest_not_found():
    response = client.get("/api/contest/1000")
    assert response.status_code == 404

def test_write_update_delete_contest():
    response = client.post("/api/contest", json={"admin_id":"2", "title" : "test", "description" : "test", "start_time" : time.time(), "end_time": time.time(), "slug" : "test"})
    print(response.json())
    testContest_id = response.json()['data']['id']
    assert response.status_code == 200
    response = client.put(f"/api/contest/{testContest_id}", json={"title":"Contest 1", "description": "Contest 1 description", "start_time": time.time(), "end_time": time.time(), "slug" : "test1"})
    assert response.status_code == 200
    response = client.delete(f"/api/contests/{testContest_id}")
    assert response.status_code == 200

def test_update_contest_not_found():
    response = client.put("/api/contest/1000", json={"title":"Contest 1", "description": "Contest 1 description", "start_time": time.time(), "end_time": time.time(), "slug" : "test"})
    assert response.status_code == 404

def test_read_scoreboard_contest():
    response = client.get("/api/contest/1/scoreboard")
    assert response.status_code == 200

# # # # # # # ============== Test Contest Problems ============== # # # # # # #
def test_read_contest_problems():
    response = client.get("/api/contest/problems")
    assert response.status_code == 200

def test_write_update_delete_contest_problem():
    response = client.post("/api/contest/problem", json={"contest_id": 1, "title":"Contest Problem 1", "description": "Contest Problem 1 description", "time_limit": 1, "memory_limit": 1, "input_format": "input format", "sample_input": "sample input", "output_format": "output format", "sample_output": "sample output", "constraints": "constraints", "explanation": "explanation"})
    testContestProblem_id = response.json()['data']['id']
    print(f"respon {response.json()}");
    assert response.status_code == 200
    response = client.put(f"/api/contest/problems/{testContestProblem_id}", json={"contest_id": 1, "title":"Contest Problem 1", "description": "Contest Problem 1 description", "time_limit": 1, "memory_limit": 1, "input_format": "input format", "sample_input": "sample input", "output_format": "output format", "sample_output": "sample output", "constraints": "constraints", "explanation": "explanation"})
    assert response.status_code == 200
    response = client.delete(f"/api/contest/problems/{testContestProblem_id}")
    assert response.status_code == 200

def test_clear_all():
    response = client.delete(f"/api/user/{userTestingId}")
    assert response.status_code == 200
