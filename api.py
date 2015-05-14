# -*- coding: UTF-8 -*-

__author__ = "MeoWoodie"

from flask import Flask, request, url_for, Response, send_file
from senz_analyser_lib.datasets import Dataset
from senz_analyser_lib import trainer
from senz_analyser_lib import classifier
import json


app = Flask(__name__)

@app.route("/trainingGMMHMM/", methods=["POST"])
def trainingGMMHMM():
    if request.method != "POST":
        err_msg = "Your request method is illegal"
        return {"massage": err_msg, "code": 1}
    # Analyse the incoming data.
    data = json.loads(request.data)
    print "Received data is", data
    # Observation
    _obs = data["obs"]
    # Params of Models
    _n_c = data["nComponent"]
    _n_m = data["nMix"]
    _start_prob_prior = data["startProbPrior"]
    _trans_mat_prior = data["transMatPrior"]
    _start_prob = data["startProb"]
    _trans_mat = data["transMat"]
    _gmms = data["gmms"]
    _covar_type = data["covarianceType"]
    _n_i = data["nIter"]
    # Config of Dataset
    _rawdata_type = data["logType"]
    _event_type = data["eventType"]
    _motion_type = data["motionType"]
    _sound_type = data["soundType"]
    _location_type = data["locationType"]

    d = Dataset(
        obs=_obs,
        rawdata_type=_rawdata_type,
        event_type=_event_type,
        motion_type=_motion_type,
        sound_type=_sound_type,
        location_type=_location_type
    )
    
    result = trainer.trainingGMMHMM(
        dataset=d,
        n_c=_n_c,
        n_m=_n_m,
        start_prob_prior=_start_prob_prior,
        trans_mat_prior=_trans_mat_prior,
        start_prob=_start_prob,
        trans_mat=_trans_mat,
        gmms=_gmms,
        covar_type=_covar_type,
        n_i=_n_i
    )
        
    result = json.dumps({"result": result, "code": 0, "message": "Training successfully"})
    return result

@app.route("/trainingGMMHMMrandomly/", methods=["POST"])
def trainingGMMHMMrandomly():
    if request.method != "POST":
        err_msg = "Your request method is illegal"
        return {"massage": err_msg, "code": 1}
    # Analyse the incoming data.
    data = json.loads(request.data)
    print "Received data is", data
    # The training event
    _obs_event = data["obsEvent"]
    _obs_length = data["obsLength"]
    _obs_count = data["obsCount"]
    # Params of Models
    _n_c = data["nComponent"]
    _n_m = data["nMix"]
    _start_prob_prior = data["startProbPrior"]
    _trans_mat_prior = data["transMatPrior"]
    _start_prob = data["startProb"]
    _trans_mat = data["transMat"]
    _gmms = data["gmms"]
    _covar_type = data["covarianceType"]
    _n_i = data["nIter"]
    # Config of Dataset
    _rawdata_type = data["logType"]
    _event_type = data["eventType"]
    _motion_type = data["motionType"]
    _sound_type = data["soundType"]
    _location_type = data["locationType"]
    _event_prob_map = data["eventProbMap"]

    d = Dataset(
        rawdata_type=_rawdata_type,
        event_type=_event_type,
        motion_type=_motion_type,
        sound_type=_sound_type,
        location_type=_location_type,
        event_prob_map=_event_prob_map
    ).randomObservations(_obs_event, _obs_length, _obs_count)

    result = trainer.trainingGMMHMM(
        dataset=d,
        n_c=_n_c,
        n_m=_n_m,
        start_prob_prior=_start_prob_prior,
        trans_mat_prior=_trans_mat_prior,
        start_prob=_start_prob,
        trans_mat=_trans_mat,
        gmms=_gmms,
        covar_type=_covar_type,
        n_i=_n_i
    )

    result = json.dumps({"result": result, "code": 0, "message": "Training successfully"})
    return result

@app.route("/classifyGMMHMM/", methods=["POST"])
def classifyGMMHMM():
    if request.method != "POST":
        err_msg = "Your request method is illegal"
        return {"massage": err_msg, "code": 1}
    # Analyse the incoming data.
    data = json.loads(request.data)
    print "Received data is", data
    # The training event
    _seq = data["seq"]
    _models = data["models"]

    result = classifier.classifyByGMMHMM(_seq, _models)

    result = json.dumps({"result": result, "code": 0, "message": "Classifing successfully"})
    return result


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9010)
