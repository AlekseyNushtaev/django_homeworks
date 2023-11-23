import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory):
    #Arrange
    course = course_factory(_quantity=1)[0]

    #Act
    response = client.get(f'/api/v1/courses/{course.id}/')

    #Assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course.id

@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=10)

    #Act
    response = client.get('/api/v1/courses/')

    #Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['id'] == courses[i].id

@pytest.mark.django_db
def test_course_id_filter(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=10)

    #Act
    response = client.get(f'/api/v1/courses/?id={courses[5].id}')

    #Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[5].id

@pytest.mark.django_db
def test_course_name_filter(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=10)

    #Act
    response = client.get(f'/api/v1/courses/?name={courses[5].name}')

    #Assert
    assert response.status_code == 200
    data = response.json()
    for course in data:
        assert course['name'] == courses[5].name

@pytest.mark.django_db
def test_course_create(client):
    #Act
    response = client.post(f'/api/v1/courses/', data={'name': 'test name'})

    #Assert
    assert response.status_code == 201

@pytest.mark.django_db
def test_course_update(client, course_factory):
    #Arrange
    course = course_factory(_quantity=1)[0]

    #Act
    response = client.patch(f'/api/v1/courses/{course.id}/', data={'name': 'patchtest'})

    #Assert
    assert response.status_code == 200

@pytest.mark.django_db
def test_course_delete(client, course_factory):
    #Arrange
    course = course_factory(_quantity=1)[0]

    #Act
    response = client.delete(f'/api/v1/courses/{course.id}/')

    #Assert
    assert response.status_code == 204




