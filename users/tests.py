from django.test import TestCase
from django.db.models import Max, Count

from users.models import User, Group


class GroupTest(TestCase):
    fixtures = ['users', 'groups']

    def test_annotate_bug(self):
        group = (Group.objects.all()
            .values("name")
            .annotate( description=Max("description"), age=Max("user__age")))
        print(group)

    def test_union_exception(self):
        group = (Group.objects.all()
                 .values("name")
                 .annotate( description=Max("description"), age=Max("user__age")
        ).union(Group.objects.all()
                .values("name")
                .annotate(description=Max("description"), age=Max("user__age"))))
        print(group)
