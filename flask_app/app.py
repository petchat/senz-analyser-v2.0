# -*- coding: UTF-8 -*-

__author__ = "MeoWoodie"

import os
import bugsnag
from senz_analyser_lib.config import *
from senz_analyser_lib.logger import log
from bugsnag.flask import handle_exceptions
from flask import Flask, request, url_for, Response, send_file
from senz_analyser_lib.datasets import Dataset
from senz_analyser_lib import trainer
from senz_analyser_lib import classifier
import json

# Configure Bugsnag
bugsnag.configure(
    api_key=BUGSNAG_TOKEN,
    project_root=os.path.dirname(os.path.realpath(__file__)),
)
app = Flask(__name__)
# Attach Bugsnag to Flask's exception handler
handle_exceptions(app)

@app.before_first_request
def init_before_first_request():
    import datetime

    init_tag = "[Initiation of Service Process]\n"

    log_init_time = "Initiation START at: \t%s\n" % datetime.datetime.now()
    log_app_env = "Environment Variable: \t%s\n" % APP_ENV
    log_bugsnag_token = "Bugsnag Service TOKEN: \t%s\n" % BUGSNAG_TOKEN
    log_logentries_token = "Logentries Service TOKEN: \t%s\n" % LOGENTRIES_TOKEN
    log.info(init_tag + log_init_time)
    log.info(init_tag + log_app_env)
    log.info(init_tag + log_bugsnag_token)
    log.info(init_tag + log_logentries_token)

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
    model = data["model"]
    config = data["config"]
    # Params of Models
    _n_c = model["nComponent"]
    _n_m = model["nMix"]
    _start_prob_prior = model["hmmParams"]["startProbPrior"]
    _trans_mat_prior = model["hmmParams"]["transMatPrior"]
    _start_prob = model["hmmParams"]["startProb"]
    _trans_mat = model["hmmParams"]["transMat"]
    if model["gmmParams"].has_key("params"):
        _gmms = model["gmmParams"]["params"]
    else:
        _gmms = None
    _covar_type = model["covarianceType"]
    _n_i = model["nIter"]
    # Config of Dataset
    _rawdata_type = config["logType"]
    _event_type = config["eventType"]
    _motion_type = config["motionType"]
    _sound_type = config["soundType"]
    _location_type = config["locationType"]

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
    _event_prob_map = data["eventProbMap"]
    model = data["model"]
    config = data["config"]
    # Params of Models
    _n_c = model["nComponent"]
    _n_m = model["nMix"]
    _start_prob_prior = model["hmmParams"]["startProbPrior"]
    _trans_mat_prior = model["hmmParams"]["transMatPrior"]
    _start_prob = model["hmmParams"]["startProb"]
    _trans_mat = model["hmmParams"]["transMat"]
    if model["gmmParams"].has_key("params"):
        _gmms = model["gmmParams"]["params"]
    else:
        _gmms = None
    _covar_type = model["covarianceType"]
    _n_i = model["nIter"]
    # Config of Dataset
    _rawdata_type = config["logType"]
    _event_type = config["eventType"]
    _motion_type = config["motionType"]
    _sound_type = config["soundType"]
    _location_type = config["locationType"]


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
    _config = data["config"]

    result = classifier.classifyByGMMHMM(_seq, _models, _config)

    result = json.dumps({"result": result, "code": 0, "message": "Classifing successfully"})
    return result


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9010)
