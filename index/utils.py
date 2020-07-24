import random
from datetime import datetime
from maps.main import sf, plot_comunas_2
import string
import os


def code_gen():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))


def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = '1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(3))
    year = datetime.now().year
    month = datetime.now().month
    directory = instance.folder
    return '{path}/{year}/{month}/{basename}-{randomstring}{ext}'.format(year=year,
                                                                         month=month, basename=basefilename,
                                                                         randomstring=randomstr, ext=file_extension,
                                                                         path=directory)


def generate_image_for_shape(shape):
    districts = []
    for d in shape.districts.all():
        districts.append(d.name)

    img = plot_comunas_2(sf, shape.title, districts, 'g', shape.code)
    shape.image = img
    shape.save()
    return shape
