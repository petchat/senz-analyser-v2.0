

data_sample = [
    {'motion': 'sitting', 'sound': 'quite/', 'location': ''}
]


class Dataset(object):

    motion_type = ('sitting', 'walking', 'running', 'riding', 'driving')

    sound_level1_type  = ('quiet', 'lowish', 'noisy')
    sound_level2_type  = ('keyboard', 'mouse_click', 'turning_page', 'writing', 'tableware',
                          'school_bell', 'stair', 'step', 'talking', 'speech',
                          'quarrel', 'scream', 'bird', 'tree', 'wind',
                          'flowing', 'sea', 'car_driving_by', 'subway', 'car_whistle',
                          'car_crash', 'car_brakes', 'boom', 'gun', 'music')

    location_type = ('home', 'work_office', 'park', 'school', 'mall',
                     'restaurant', 'scenic', 'hospital', 'hotel', 'train_station')

    def __init__(self):
        pass