from django.db import models
from django.contrib.auth.models import User
from PIL import ExifTags
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

from project import settings
from StringIO import StringIO
import cStringIO

from django.conf import settings


class University(models.Model):
    name = models.CharField(max_length=80, unique=True)
    acronym = models.CharField(max_length=40)
    
    def __unicode__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=80, unique=True)
    
    def __unicode__(self):
        return self.name
        
class Administrator(models.Model):
    user = models.OneToOneField(User)
    university = models.ForeignKey(University)
    
    def user_email(self):
        return self.user.email
        
    def __unicode__(self):
        return "Administrator of %s" % (self.university)

class Host(models.Model):
    user = models.OneToOneField(User)
    organization = models.ForeignKey(Organization)
    university = models.ForeignKey(University)
    administrator = models.ForeignKey(Administrator, null=True, blank=True)
    
    def user_email(self):
        return self.user.email
        
    def __unicode__(self):
        return "%s of %s" % (self.organization, self.university)
        
    def has_admin(self):
        if (self.administrator):
            return True
        else:
            return False


hours = (
    ('', 'Hour of Event'),
    ('12 PM', '12 PM'),
    ('01 PM', '01 PM'),
    ('02 PM', '02 PM'),
    ('03 PM', '03 PM'),
    ('04 PM', '04 PM'),
    ('05 PM', '05 PM'),
    ('06 PM', '06 PM'),
    ('07 PM', '07 PM'),
    ('08 PM', '08 PM'),
    ('09 PM', '09 PM'),
    ('10 PM', '10 PM'),
    ('11 PM', '11 PM'),
    ('12 AM', '12 AM'),
    ('01 AM', '01 AM'),
    ('02 AM', '02 AM'),
    ('03 AM', '03 AM'),
    ('04 AM', '04 AM'),
    ('05 AM', '05 AM'),
    ('06 AM', '06 AM'),
    ('07 AM', '07 AM'),
    ('08 AM', '08 AM'),
    ('09 AM', '09 AM'),
    ('10 AM', '10 AM'),
    ('11 AM', '11 AM'),
)

councils = (
   ('', 'Affiliated Council'),
   ('Interfraternity Council', 'Interfraternity Council'),
   ('Panhellenic', 'Panhellenic'),
   ('NPHC', 'NPHC'),
   ('Non-Affiliated', 'Non-Affiliated')
)

event_types = (
   ('', 'Type of Event'),
   ('Social', 'Social'),
   ('Date Function', 'Date Function'),
   ('Formal', 'Formal'),
   ('Other', 'Other')
)

invitation_types = (
   ('', 'Choose One'),
   ('Invitation Only', 'Invitation Only'),
   ('Open to the Public', 'Open to the Public'),
   ('Open to Faculty, Staff, Students', 'Open to Faculty, Staff, Students')
)

event_locations = (
   ('', 'Where is the event located?'),
   ('Chapter House', 'Chapter House'),
   ('Other Campus Venue', 'Other Campus Venue'),
   ('Off Campus', 'Off Campus')
)


class Event(models.Model):
    name = models.CharField(max_length=40)
    date_of_event     = models.DateField()
    time_of_event     = models.CharField(max_length=40, choices=hours)
    event_location    = models.CharField(max_length=100, choices=event_locations)
    event_location_other     = models.CharField(max_length=100, blank=True, null=True)
    name_of_planner   = models.CharField(max_length=100)
    phone_number_of_planner  = models.CharField(max_length=40)
    email_of_planner  = models.CharField(max_length=40)
    expected_number_guests   = models.IntegerField()
    affiliated_council       = models.CharField(max_length=40, choices=councils)
    type_of_event     = models.CharField(max_length=40, choices=event_types)
    type_event_other  = models.CharField(max_length=100, blank=True, null=True)
    event_description  = models.TextField()
    invitation_type   = models.CharField(max_length=100, choices=invitation_types)
    transportation    = models.TextField(blank=True, null=True)
    one_entry_point   = models.CharField(max_length=10, choices=(('', 'Will there be one entry point?'), ('Yes', 'Yes'), ('No', 'No')))
    entry_point_location     = models.CharField(max_length=100)
    co_sponsored_description = models.TextField(blank=True, null=True)
    alcohol_distribution     = models.TextField(blank=True, null=True)
    sober_monitors    = models.TextField()
    presidents_email  = models.EmailField()

    host = models.ForeignKey(Host)

    def host_email(self):
        return self.host.user.email
    
    def __unicode__(self):
        return self.name
        
class Guest(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices = (('Male', 'Male'), ('Female', 'Female')))
    event = models.ManyToManyField(Event)
    
    def __unicode__(self):
        return "%s, %s" % (self.last_name, self.first_name)

categories = (
    ('', 'Select category for flag'),
    ('Underage Drinking', 'Underage Drinking'),
    ('Stealing', 'Stealing'),
    ('Vandalism', 'Vandalism'),
    ('Violence', 'Violence'),
    ('Other', 'Other'),
)

priorities = (
    ('', 'Select severity of violation'),
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High')
)


class Flag(models.Model):
    guest = models.ForeignKey(Guest)
    host = models.ForeignKey(Host, null=True, blank=True)
    administrator = models.ForeignKey(Administrator, null=True, blank=True)
    priority = models.CharField(max_length=10, choices=priorities)
    category = models.CharField(max_length=20, choices=categories)
    other_description = models.CharField(max_length=30, blank=True, null=True, help_text='If you chose other, fill in description')
        

def flat( *nums ):
    return tuple( int(round(n)) for n in nums )
     
class Size(object):
    def __init__(self, pair):
        self.width = float(pair[0])
        self.height = float(pair[1])
     
    @property
    def aspect_ratio(self):
        return self.width / self.height
         
    @property
    def size(self):
        return flat(self.width, self.height)
     
def cropped_thumbnail(img, size):
    original = Size(img.size)
    target = Size(size)
     
    if target.aspect_ratio > original.aspect_ratio:
        scale_factor = target.width / original.width
        crop_size = Size( (original.width, target.height / scale_factor) )
        top_cut_line = 0
        img = img.crop( flat(0, top_cut_line, crop_size.width, top_cut_line + crop_size.height) )
    elif target.aspect_ratio < original.aspect_ratio:
        scale_factor = target.height / original.height
        crop_size = Size( (target.width/scale_factor, original.height) )
        side_cut_line = (original.width - crop_size.width) / 2
        img = img.crop( flat(side_cut_line, 0, side_cut_line + crop_size.width, crop_size.height) )
        
    return img.resize(target.size, Image.ANTIALIAS)
        
class GuestImage(models.Model):
    image = models.ImageField(upload_to='images/guests')
    image_thumb = models.ImageField(upload_to='images/guests')
    guest = models.ForeignKey(Guest)
    event = models.ForeignKey(Event)
    date_time_taken = models.DateTimeField()
    
    def __unicode__(self):
        return "%s, %s" % (self.guest.last_name, self.guest.first_name)
        
    def event_name(self):
        return self.event.name
        
    def save(self, *args, **kwargs):
        super(GuestImage, self).save(*args, **kwargs)
        
        img = Image.open(StringIO(self.image_thumb.read()))
        img = cropped_thumbnail(img, (80, 80))
        
        img_io = StringIO()
        img.save(img_io, format='JPEG')
  
        image_path = str(self.guest.pk) + '-' + str(self.event.pk)
        image_file = InMemoryUploadedFile(img_io, None, '%s-thumb.jpg' % (str(image_path)), 'image/jpeg', img_io.len, None)
        self.image_thumb = image_file
        super(GuestImage, self).save(*args, **kwargs)
