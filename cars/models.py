from django.db import models
from datetime import datetime

# Create your models here.
class Car(models.Model):

    state_choice = (
    ("AN","Andaman and Nicobar Islands"),
    ("AP","Andhra Pradesh"),
    ("AR","Arunachal Pradesh"),
    ("AS","Assam"),
    ("BR","Bihar"),
    ("CG","Chhattisgarh"),
    ("CH","Chandigarh"),
    ("DN","Dadra and Nagar Haveli"),
    ("DD","Daman and Diu"),
    ("DL","Delhi"),
    ("GA","Goa"),
    ("GJ","Gujarat"),
    ("HR","Haryana"),
    ("HP","Himachal Pradesh"),
    ("JK","Jammu and Kashmir"),
    ("JH","Jharkhand"),
    ("KA","Karnataka"),
    ("KL","Kerala"),
    ("LA","Ladakh"),
    ("LD","Lakshadweep"),
    ("MP","Madhya Pradesh"),
    ("MH","Maharashtra"),
    ("MN","Manipur"),
    ("ML","Meghalaya"),
    ("MZ","Mizoram"),
    ("NL","Nagaland"),
    ("OD","Odisha"),
    ("PB","Punjab"),
    ("PY","Pondicherry"),
    ("RJ","Rajasthan"),
    ("SK","Sikkim"),
    ("TN","Tamil Nadu"),
    ("TS","Telangana"),
    ("TR","Tripura"),
    ("UP","Uttar Pradesh"),
    ("UK","Uttarakhand"),
    ("WB","West Bengal")
    )

    year_choice = []
    for r in range(2010, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('BluAir Conditioningetooth Handset', 'Bluetooth Handset'),
    )
 





    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    # description = RichTextField()
    description = models.TextField(max_length=500)

    car_photo = models.ImageField(upload_to='photos/%Y/%m/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    # features = MultiSelectField(choices=features_choices,max_choices=5,max_length=100)
    Cruise_Control=models.BooleanField(default=False)
    Audio_Interface=models.BooleanField(default=False)
    Airbags=models.BooleanField(default=False)
    Air_Conditioning=models.BooleanField(default=False)
    Seat_Heating=models.BooleanField(default=False)
    Alarm_System=models.BooleanField(default=False)
    ParkAssist=models.BooleanField(default=False)
    Power_Steering=models.BooleanField(default=False)
    Reversing_Camera=models.BooleanField(default=False)
    Direct_Fuel_Injection=models.BooleanField(default=False)
    Auto_Start_Stop=models.BooleanField(default=False)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    kms = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title