from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_get_user(test_user):
    response = client.get('/user/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'codingwitharslan'
    assert response.json()['email'] == 'codingwitharslan@gmail.com'
    assert response.json()['first_name'] == 'Arslan'
    assert response.json()['last_name'] == 'Ovezov'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '(111)-111-1111'
    
    
def test_change_password_success(test_user):
    response = client.put("/user/password", json={"password": "testpassword",
                                                         "new_password": "newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT