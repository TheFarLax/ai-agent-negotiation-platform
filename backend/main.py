from services.genlayer_service import (
    submit_appeal_result
)
from services.genlayer_service import (
    submit_validator_result
)
from services.genlayer_service import store_on_genlayer
from escrow.escrow_manager import (
    create_escrow,
    release_escrow
)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from negotiation.run_negotiation import run_negotiation
from validators.delivery_validator import evaluate_delivery
from validators.consensus import run_consensus

import json
import uuid
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/negotiate")
def negotiate(request: dict):

    result = run_negotiation(
        request["task"]
    )

    return result


@app.post("/store-agreement")
def store_agreement(agreement: dict):

    result = store_on_genlayer(
        agreement
    )

    return result

@app.post("/evaluate-delivery")
def evaluate(data: dict):

    result = run_consensus(
        task=data["task"],
        agreement=data["agreement"],
        delivery=data["delivery"]
    )

    return result

@app.post("/create-escrow")
def escrow(data: dict):

    result = create_escrow(
        agreement_id=data["agreement_id"],
        amount=data["amount"]
    )

    return result

@app.post("/release-payment")
def release(data: dict):

    result = release_escrow(
        agreement_id=data["agreement_id"]
    )

    return result

@app.post("/submit-validator-result")
def submit_result(data: dict):

    result = submit_validator_result(
        agreement_id=data["agreement_id"],
        validator_result=data["validator_result"]
    )

    return result
@app.post("/submit-appeal-result")
def submit_appeal(data: dict):

    result = submit_appeal_result(
        agreement_id=data["agreement_id"],
        validator_result=data["validator_result"]
    )

    return result

@app.post("/submit-appeal-result")
def submit_appeal(data: dict):

    result = submit_appeal_result(
        agreement_id=data["agreement_id"],
        validator_result=data["validator_result"]
    )

    return result
