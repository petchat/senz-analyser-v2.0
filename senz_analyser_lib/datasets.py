import numpy as np
import utils as ut
import matplotlib.pyplot as plt

class Dataset(object):
    """
    Dataset

    private attributes:
        - obs:
        - dataset:

    """
    rawdata_type = ("motion", "location", "sound")

    # event_type  = ("shopping", "dining_out_in_chinese_restaurant", "work", "running_fitness")
    event_type  = ("shopping", "dining_out_in_chinese_restaurant", "work", "running_fitness")

    motion_type = ("sitting", "walking", "running", "riding", "driving")

    # sound_level1_type  = ("quiet", "lowish", "noisy")

    sound_type  = (
        # artificial
        "keyboard", "mouse_click", "turning_page", "writing", "tableware", "school_bell", "stair",
        # human_related
        "talking", "speech", "step", "quarrel", "scream", "laugh",
        # natural
        "bird", "tree", "wind", "flowing", "sea",
        # city
        "car_driving_by", "subway", "car_whistle",
        # special
        "car_crash", "car_brakes", "boom", "gun", "music",
        # other
        "silence"
    )

    # location_level1_type = ("dining", "shopping", "life_service", "entertainment", "auto_related", "healthcare", "hotel", "scenic_spot", "exhibition", "education", "finance", "infrastructure", "estate")

    location_type = (
        # dining
        "chinese_restaurant", "japan_korea_restaurant", "western_restaurant", "bbq", "chafing_dish", "seafood", "vegetarian_diet", "muslim", "buffet", "dessert", "cooler", "snack_bar",
        # shopping
        "comprehensive_market", "convenience_store", "supermarket", "digital_store", "pet_market", "furniture_store", "farmers_market", "commodity_market", "flea_market", "sports_store", "clothing_store", "video_store", "glass_store", "mother_store", "jewelry_store", "cosmetics_store", "gift_store", "photography_store", "pawnshop", "antique_store", "bike_store", "cigarette_store", "stationer",
        # life service
        "travel_agency", "ticket_agent", "post_office", "telecom_offices", "newstand", "water_supply_office", "electricity_office", "photographic_studio", "laundry", "talent_market", "lottery_station", "housekeeping", "intermediary", "pet_service", "salvage_station", "welfare_house", "barbershop",
        # entertainment
        "bath_sauna", "ktv", "bar", "coffee", "night_club", "cinema", "odeum", "resort", "outdoor", "game_room", "internet_bar",
        # auto_related
        "gas_station", "parking_plot", "auto_sale", "auto_repair", "motorcycle", "car_maintenance", "car_wash",
        # healthcare
        "hospital", "clinic", "emergency_center", "drugstore",
        # hotel
        "motel", "hotel", "economy_hotel", "guest_house", "hostel",
        # scenic_spot
        "scenic_spot",
        # exhibition
        "museum", "exhibition_hall", "science_museum", "library", "gallery", "convention_center",
        # education
        "university", "high_school", "primary_school", "kinder_garten", "training_institutions", "technical_school", "adult_education",
        # finance
        "bank", "atm", "insurance_company", "security_company",
        # infrastructure
        "traffic", "public_utilities", "toll_station", "other_infrastructure",
        # estate
        "residence", "business_building",
        # other
        "other",
        # algo recognized
        "home", "work_office"
    )

    rawdata_map = {
        "motion": motion_type,
        "sound": sound_type,
        "location": location_type
    }

    event_prob_map = {
        "dining_out_in_chinese_restaurant": {
            "motion": [{"sitting": 0.7}, {"walking": 0.3}],
            "sound": [{"talking": 0.4}, {"laugh": 0.3}, {"silence": 0.15}, {"tableware": 0.1}, {"Others": 0.05}],
            "location": [{"chinese_restaurant": 0.7}, {"Others": 0.25}, {"residence": 0.05}]
        },
        "running_fitness": {
            "motion": [{"running": 0.4}, {"walking": 0.4}, {"sitting": 0.2}],
            "sound": [{"step": 0.2}, {"wind": 0.2}, {"silence": 0.2}, {"car_driving_by": 0.2}, {"Others": 0.2}],
            "location": [{"scenic_spot": 0.3}, {"Others": 0.3}, {"residence": 0.2}, {"traffic": 0.2}]
        },
        "work": {
            "motion": [{"sitting": 0.85}, {"walking": 0.15}],
            "sound": [{"step": 0.2}, {"silence": 0.2}, {"keyboard": 0.2}, {"mouse_click": 0.1}, {"turning_page": 0.1}, {"talking": 0.2}],
            "location": [{"work_office": 0.7}, {"home": 0.2}, {"Others": 0.1}]
        },
        "shopping": {
            "motion": [{"walking": 0.7}, {"sitting": 0.3}],
            "sound": [{"step": 0.2}, {"talking": 0.4}, {"car_driving_by": 0.1}, {"music": 0.2}, {"Others": 0.1}],
            "location": [{"comprehensive_market": 0.7}, {"chinese_restaurant": 0.2}, {"Others": 0.1}]
        }
    }

    def __init__(self, obs=None, rawdata_type=None, event_type=None, motion_type=None, sound_type=None, location_type=None, event_prob_map=None):
        self.obs = obs
        if rawdata_type is not None:
            self.rawdata_type   = rawdata_type
        if event_type is not None:
            self.event_type     = event_type
        if motion_type is not None:
            self.motion_type    = motion_type
        if sound_type is not None:
            self.sound_type     = sound_type
        if location_type is not None:
            self.location_type  = location_type
        if event_prob_map is not None:
            self.event_prob_map = event_prob_map

    def _convertNumericalObservation(self, obs):
        """
        Convert Numerical Observation

        Convert Observation from Object to numerical python array (ie. list)
        """
        # compose the dataset in numpy array
        numerical_obs = []
        for seq in obs:
            spots_set = []
            for senz in seq:
                spot = [
                    self.motion_type.index(senz["motion"]),
                    self.location_type.index(senz["location"]),
                    self.sound_type.index(senz["sound"])
                ]
                spots_set.append(spot)
            numerical_obs.append(spots_set)
        return numerical_obs

    def _convetNumericalSequence(self, seq):
        """
        Convert Numerical Sequence

        Convert Sequence from Object to numercial python array (ie. list)
        """
        numerical_seq = []
        for senz in seq:
            spot = [
                self.motion_type.index(senz["motion"]),
                self.location_type.index(senz["location"]),
                self.sound_type.index(senz["sound"])
            ]
            numerical_seq.append(spot)
        return numerical_seq

    # Generate fitable dataset
    def _convertObs2Dataset(self, obs):
        """
        Fit Dataset

        Generate dataset which could be fitted by hmmlearn module.
        obs look like:
        [np.array([...]), ...]
        """
        # compose the dataset in numpy array
        dataset = []
        for seq in obs:
            spots_set = []
            for senz in seq:
                spot = [
                    self.motion_type.index(senz["motion"]),
                    self.location_type.index(senz["location"]),
                    self.sound_type.index(senz["sound"])
                ]
                spots_set.append(spot)
            dataset.append(np.array(spots_set))
        return dataset

    # Generate Rawdata in a discrete pdf randomly.
    def _generateRawdataRandomly(self, rawdata_type, results_prob_list):
        """
        Generate Rawdata Randomly

        Generate rawdata randomly in a specifid discrete probability distribution.
        You should choose which rawdata type you want to generate, then
        you need specify the probability distribution by results_prob_list,
        it"s format looks like:
            [{key: prob1}, {key: prob2}, ...]
        """
        # validate input rawdata type
        if rawdata_type not in self.rawdata_type:
            return None
        for result_prob in results_prob_list:
            # validate input possible result list
            if result_prob.keys()[0] not in self.rawdata_map[rawdata_type] and result_prob.keys()[0] != "Others":
                return None
            # if result_prob.keys()[0] is "other":
            #     result_prob.keys()[0] = ut.chooseRandomly(self.rawdata_map[rawdata_type])
        results_prob_list = ut.selectOtherRandomly(results_prob_list, self.rawdata_map[rawdata_type])
        # According to results" probability list,
        # generate the random rawdata.
        return ut.discreteSpecifiedRand(results_prob_list)

    def getDataset(self):
        """
        Get Dataset

        You can invoke this method to get the dataset,
        which can be fitted by variety of hmm model.
        """
        if self.obs is None:
            return None
        else:
            return self._convertObs2Dataset(self.obs)

    # Generate fitabel dataset randomly
    def randomSequence(self, event, length):
        """
        Random Sequence

        Generate a sequence which contains several senzes.
        the sequence can be scored by invoking hmmlearns" score() method after convert to np.array
        You should specify which event you want to generate,
        and length of sequence.
        """
        # validate input event.
        if event not in self.event_prob_map.keys():
            return None
        # generate senz one by one.
        seq   = []
        times = 0
        while times < length:
            senz = {}
            # generate every type of rawdata.
            for rawdata_type in self.rawdata_type:
                senz[rawdata_type] = self._generateRawdataRandomly(rawdata_type, self.event_prob_map[event][rawdata_type])
            seq.append(senz)
            times += 1
        # self.seq = seq
        return seq

    def randomObservations(self, event, seq_length, seq_count):
        """
        Random Observations

        Generate an Observations which contains several sequences.
        the observations can be converted to dataset by invoking _convertObs2Dataset.
        You should specify which event you want to generate,
        and every sequence length, and count of sequences.
        """
        # validate input event.
        if event not in self.event_prob_map.keys():
            return None
        obs = []
        times = 0
        while times < seq_count:
            obs.append(self.randomSequence(event, seq_length))
            times += 1
        self.obs = obs
        return self

    def plotObservations3D(self):
        # TODO: Currently we only process 3-dimensinal plot.
        # Create a new figure
        fig   = plt.figure()
        ax    = fig.add_subplot(111, projection="3d")
        n_obs = np.array(self._convertNumericalObservation(self.obs))
        dim   = n_obs.shape[0] * n_obs.shape[1]
        # Extract every axis data.
        xs = n_obs[:, :, 0].reshape(dim,)
        ys = n_obs[:, :, 1].reshape(dim,)
        zs = n_obs[:, :, 2].reshape(dim,)
        # plot
        ax.scatter(xs, ys, zs, c="r", marker="o")
        ax.set_xlabel("Motion Label")
        ax.set_ylabel("Location Label")
        ax.set_zlabel("Sound Label")
        # show the figure
        plt.show()

if __name__ == "__main__":
    dataset = Dataset()
    dataset.randomObservations("dining_out_in_chinese_restaurant", 10, 100)
    print dataset.obs
    dataset.plotObservations3D()

