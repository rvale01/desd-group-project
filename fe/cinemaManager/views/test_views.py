
from django.test import TestCase, Client
from django.urls import reverse
from fe.cinemaManager.models.general import Showing, Film, Screen
from cinemaManager.views.booking import list_showings_booking

class ListShowingsBookingTestCase(TestCase):
    def setUp(self):
        
        self.client = Client()
        self.film1 = Film.objects.create(title="Film1", description="Description1", age_rating="PG", duration=120)
        self.film2 = Film.objects.create(title="Film2", description="Description2", age_rating="PG", duration=100)
        self.screen1 = Screen.objects.create(name="Screen1", no_seats=100)
        self.showing1 = Showing.objects.create(time="10:00", date="2023-04-20", available_seats=50, film=self.film1, screen=self.screen1)
        self.showing2 = Showing.objects.create(time="14:00", date="2023-04-20", available_seats=40, film=self.film2, screen=self.screen1)

    def test_list_showings_booking(self):
        
        response = self.client.get(reverse('bookings/list_showings_booking'))

        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['showings']), 2)
        self.assertIn(self.showing1, response.context['showings'])
        self.assertIn(self.showing2, response.context['showings'])

        
        self.assertTemplateUsed(response, 'fe/cinemaManager/templates/Bookings/list_showings_booking.html')
