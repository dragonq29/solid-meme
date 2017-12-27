from datetime import timedelta, datetime

import exifread

import os
import glob


class ImageFileNameChanger(object):
    def __init__(self):
        work()


def get_camera_model_name(fn):
    f = open(fn, 'rb')
    tags = exifread.process_file(f)
    return tags['Image Model'].values


def work():
    path = 'test/*.*'
    files = glob.glob(path)

    for pathName in files:
        file_name = pathName[5:20]
        if pathName[23] == '4':
            continue
        parsed_time = datetime.strptime(file_name, '%Y%m%d_%H%M%S')
        temp_datetime = parsed_time - timedelta(hours=7)
        des_datetime_name = temp_datetime.strftime('%Y%m%d_%H%M%S')
        camera_model_name = get_camera_model_name(pathName)
        if camera_model_name == 'SM-G920K':
            name_ = 'edited/' + des_datetime_name + '.jpg'
            os.rename(pathName, name_)

        print('edited/' + pathName[5:])
