import datetime
import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from risk_managed.main.models import Administrator, Event, Host, Organization, University


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "-f", "--force", action="store_true", dest="force", default=False, help="Force DB Wipe"
        )

    def handle(self, *args, **kwargs):
        if not kwargs.get("force"):
            print("Are you sure you would like to recreate your entire database?")
            print("Enter `DELETE` to delete database and load with fixture data: ")
            choice = input()
            if choice != "DELETE":
                print("Your actions have resulted in zero change to the database.")
                return

        ORGANIZATIONS = [
            {"name": "Kappa Sigma"},
            {"name": "Sigma Nu"},
            {"name": "Sigma Alpha Epsilon"},
            {"name": "Pi Kappa Phi"},
            {"name": "Theta Chi"},
            {"name": "Delta Chi"},
        ]
        organizations = []

        UNIVERSITIES = [
            {"name": "Southern Polytechnic State University", "acronym": "SPSU"},
            {"name": "University of Georgia", "acronym": "UGA"},
            {"name": "University of West Georgia", "acronym": "UWG"},
            {"name": "Kennesaw State University", "acronym": "KSU"},
            {"name": "Georgia Institute of Technology", "acronym": "GT"},
            {"name": "Georgia State University", "acronym": "GSU"},
        ]
        universities = []

        """
        Generate Universities.
        """
        # Delete pre-existing objects
        University.objects.all().delete()

        print()
        print("Universities")
        print("--------------------------------------------------------------------------------")
        for university in UNIVERSITIES:
            obj = University.objects.create(**university)
            print(obj)
            universities.append(obj)

        """
        Generate Organizations.
        """
        # Delete pre-existing objects
        Organization.objects.all().delete()

        print()
        print("Organizations")
        print("--------------------------------------------------------------------------------")
        for organization in ORGANIZATIONS:
            obj = Organization.objects.create(**organization)
            print(obj)
            organizations.append(obj)

        """
        Generate Users.
        """
        # Delete pre-existing objects
        get_user_model().objects.all().exclude(is_superuser=True).delete()

        hosts = []
        administrators = []

        # Create new users
        for university in universities:
            username = university.acronym.lower()
            email = username + "@" + username + ".com"
            user = get_user_model().objects.create_user(
                email=email, username=username, password=username
            )
            administrator = Administrator.objects.create(user=user, university=university)
            administrators.append(administrator)
            print()
            print(administrator)
            print(
                "--------------------------------------------------------------------------------"
            )

            for organization in organizations:
                username = "{organization_acronym}{university_acronym}".format(
                    organization_acronym="".join(filter(str.isupper, organization.name)).lower(),
                    university_acronym=university.acronym.lower(),
                )
                email = username + "@" + username + ".com"
                user = get_user_model().objects.create_user(
                    email=email, username=username, password=username
                )
                host = Host.objects.create(
                    user=user,
                    organization=organization,
                    university=university,
                    administrator=administrator,
                )
                hosts.append(host)
                print(host)

        """
        Generate Events.
        """
        EVENTS = [
            {"name": "Christmas Party", "date_of_event": datetime.date(2017, 12, 23)},
            {"name": "Halloween Party", "date_of_event": datetime.date(2017, 10, 31)},
            {"name": "Fourth of July Party", "date_of_event": datetime.date(2017, 7, 4)},
            {"name": "Rush Party", "date_of_event": datetime.date(2017, 8, 12)},
        ]

        print()
        print("Events")
        print("--------------------------------------------------------------------------------")
        for host in hosts:
            event = random.choice(EVENTS)
            event = Event.objects.create(
                name=event["name"],
                date_of_event=event["date_of_event"],
                time_of_event="07 PM",
                event_location="Chapter House",
                name_of_planner="Josh Eppinette",
                phone_number_of_planner="1234567890",
                email_of_planner="test@test.com",
                expected_number_guests=500,
                affiliated_council="Interfraternity Council",
                type_of_event="Social",
                event_description=" ",
                invitation_type="Invitation Only",
                transportation="Uber",
                one_entry_point="Yes",
                entry_point_location="Front Door",
                sober_monitors="Not me",
                presidents_email="president@president.com",
                host=host,
            )
            print(event)
