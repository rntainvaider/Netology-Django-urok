import pytest
from django.urls import reverse
from rest_framework import status
from model_bakery import baker
from students.models import Course


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make(Course, **kwargs)

    return factory


def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = reverse("course-detail", args=[course.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == course.id


def test_list_courses(api_client, course_factory):
    courses = course_factory(_quantity=5)
    url = reverse("course-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5


def test_filter_courses_by_id(api_client, course_factory):
    courses = course_factory(_quantity=5)
    url = reverse("course-list")
    response = api_client.get(url, {"id": courses[0].id})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["id"] == courses[0].id


def test_filter_courses_by_name(api_client, course_factory):
    courses = course_factory(_quantity=5)
    url = reverse("course-list")
    response = api_client.get(url, {"name": courses[0].name})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == courses[0].name


def test_create_course(api_client):
    url = reverse("course-list")
    data = {"name": "New Course"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Course.objects.filter(name="New Course").exists()


def test_update_course(api_client, course_factory):
    course = course_factory()
    url = reverse("course-detail", args=[course.id])
    data = {"name": "Updated Course"}
    response = api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    course.refresh_from_db()
    assert course.name == "Updated Course"


def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse("course-detail", args=[course.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Course.objects.filter(id=course.id).exists()
