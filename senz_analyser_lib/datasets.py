import numpy as np

class Dataset(object):
    '''
    Dataset

    private attributes:
        - datasets:
        - np_datasets:

    '''

    senz_sample = {
        'motion':   'sitting',
        'sound':    'laugh',
        'location': 'chinese_restaurant'
    }

    eating_seq_sample = np.array([
        {'motion': 'sitting', 'sound': 'talking', 'location': 'estate'},
        {'motion': 'sitting', 'sound': 'laugh', 'location': 'chinese_restaurant'},
        {'motion': 'sitting', 'sound': 'laugh', 'location': 'chinese_restaurant'},
        {'motion': 'sitting', 'sound': 'talking', 'location': 'chinese_restaurant'},
        {'motion': 'sitting', 'sound': 'talking', 'location': 'chinese_restaurant'},
        {'motion': 'sitting', 'sound': 'laugh', 'location': 'chinese_restaurant'},
        {'motion': 'sitting', 'sound': 'talking', 'location': 'chinese_restaurant'},
        {'motion': 'sitting', 'sound': 'silence', 'location': 'chinese_restaurant'},
        {'motion': 'sitting', 'sound': 'talking', 'location': 'chinese_restaurant'}
    ])

    event_type  = ('shopping', 'dining_out', 'work', 'fitness')

    motion_type = ('sitting', 'walking', 'running', 'riding', 'driving')

    sound_level1_type  = ('quiet', 'lowish', 'noisy')

    sound_level2_type  = (
        # artificial
        'keyboard', 'mouse_click', 'turning_page', 'writing', 'tableware', 'school_bell', 'stair',
        # human_related
        'talking', 'speech', 'step', 'quarrel', 'scream', 'laugh',
        # natural
        'bird', 'tree', 'wind', 'flowing', 'sea',
        # city
        'car_driving_by', 'subway', 'car_whistle',
        # special
        'car_crash', 'car_brakes', 'boom', 'gun', 'music',
        # other
        'silence'
    )

    location_level1_type = ('dining', 'shopping', 'life_service', 'entertainment', 'auto_related', 'healthcare', 'hotel', 'scenic_spot', 'exhibition', 'education', 'finance', 'infrastructure', 'estate')

    location_level2_type = (
        # dining
        'chinese_restaurant', 'japan_korea_restaurant', 'western_restaurant', 'bbq', 'chafing_dish', 'seafood', 'vegetarian_diet', 'muslim', 'buffet', 'dessert', 'cooler', 'snack_bar',
        # shopping
        'comprehensive_market', 'convenience_store', 'supermarket', 'digital_store', 'pet_market', 'furniture_store', 'farmers_market', 'commodity_market', 'flea_market', 'sports_store', 'clothing_store', 'video_store', 'glass_store', 'mother_store', 'jewelry_store', 'cosmetics_store', 'gift_store', 'photography_store', 'pawnshop', 'antique_store', 'bike_store', 'cigarette_store', 'stationer',
        # life service
        'travel_agency', 'ticket_agent', 'post_office', 'telecom_offices', 'newstand', 'water_supply_office', 'electricity_office', 'photographic_studio', 'laundry', 'talent_market', 'lottery_station', 'housekeeping', 'intermediary', 'pet_service', 'salvage_station', 'welfare_house', 'barbershop',
        # entertainment
        'bath_sauna', 'ktv', 'bar', 'coffee', 'night_club', 'cinema', 'odeum', 'resort', 'outdoor', 'game_room', 'internet_bar',
        # auto_related
        'gas_station', 'parking_plot', 'auto_sale', 'auto_repair', 'motorcycle', 'car_maintenance', 'car_wash',
        # healthcare
        'hospital', 'clinic', 'emergency_center', 'drugstore',
        # hotel
        'motel', 'hotel', 'economy_hotel', 'guest_house', 'hostel',
        # scenic_spot
        'scenic_spot',
        # exhibition
        'museum', 'exhibition_hall', 'science_museum', 'library', 'gallery', 'convention_center',
        # education
        'university', 'high_school', 'primary_school', 'kinder_garten', 'training_institutions', 'technical_school', 'adult_education',
        # finance
        'bank', 'atm', 'insurance_company', 'security_company',
        # infrastructure
        'traffic', 'public_utilities', 'toll_station', 'other_infrastructure',
        # estate
        'residence', 'business_building',
        # other
        'other'
    )

    def __init__(self, obs):
        # compose the datasets in numpy array
        self.datasets = []
        for seq in obs:
            spots_set = []
            for senz in seq:
                spot = [
                    self.motion_type.index(senz['motion']),
                    self.location_level2_type.index(senz['location']),
                    self.sound_level2_type.index(senz['sound'])
                ]
                print spot
                spots_set.append(spot)
            self.datasets.append(spots_set)
        self.np_datasets = np.array(self.datasets)

    def randomTrainingSample(self, event):
        if event not in self.event_type:
            return None




