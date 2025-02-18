from django.db import models

class Room(models.Model):
    room_no = models.CharField(max_length=10, unique=True)  # Room number (unique)
    no_of_beds = models.IntegerField()  # Number of beds in the room

    def __str__(self):
        return f"Room {self.room_no} (Beds: {self.no_of_beds})"
