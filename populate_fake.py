import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'examplepro.settings')
import django
django.setup()
from django.db import models

##FAKE POPULATION SCRIPT
import random
from exampleapp.models import AccessRecord,Topic,Webpage

from faker import Faker

fakegenerator = Faker()

# class MyModel(models.Model):
#     objects = models.Manager()

topics = ["Search","Social",'Marketplace',"News","Games"]

def add_topics():
    t= Topic.objects.get_or_create(top_name =random.choice(topics))[0]  #get_or_create returns a tuple and [0] just takes the first element of that.
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        #get the topic for the entry
        top = add_topics()

        #create fake data for the entry
        fake_url = fakegenerator.url()
        fake_date = fakegenerator.date()
        fake_name = fakegenerator.company()


        #crreate the new webpage entry
        webpg =  Webpage.objects.get_or_create(topic = top,url = fake_url,date = fake_date,name = fake_name)[0]
        acc_rec =AccessRecord.objects.get_ro_create(name = webpg,date =fake_date)


if __name__ == "main":
    print("Populaitng script")
    populate(20)
    print("POPULATION DONE.")

