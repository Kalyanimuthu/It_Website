from django.db import models
from ckeditor.fields import RichTextField

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    background = models.ImageField(upload_to="hero/")

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=120)
    icon = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="projects/")
    short_description = models.TextField()

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=120)
    photo = models.ImageField(upload_to="team/")
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name

class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    email_icon = models.CharField(max_length=50, default="bx bx-envelope")
    phone_icon = models.CharField(max_length=50, default="bx bx-phone-call")
    address_icon = models.CharField(max_length=50, default="bx bx-map")

    def __str__(self):
        return "Company Contact Info"

class ContactPage(models.Model):
    heading = models.CharField(max_length=150, default="Contact Us")
    sub_heading = models.CharField(max_length=300, default="We're here to help you.")
    map_embed_url = models.TextField(help_text="Paste Google Map Embed URL")

    form_title = models.CharField(max_length=150, default="Send a Message")
    name_placeholder = models.CharField(max_length=100, default="Your Name")
    email_placeholder = models.CharField(max_length=100, default="Your Email")
    message_placeholder = models.CharField(max_length=150, default="Your Message")
    submit_text = models.CharField(max_length=50, default="Send Message")

    def __str__(self):
        return "Contact Page Settings"

