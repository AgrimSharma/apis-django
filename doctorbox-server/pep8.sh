#!/usr/bin/env bash

source ./setup.sh

function ensure_pep_8_compliance {
    APPLICATION_NAME=doctorbox_web
    flake8 ${APPLICATION_NAME} --exclude doctorbox_web/api/migrations --ignore E501
    FLAKE_STATUS=$?

    if [[ ( ${FLAKE_STATUS} == 0 ) ]] ; then
        echo "Congratulations! ${APPLICATION_NAME} is PEP8 compliant."
        exit 0
    else
        exit 1
    fi
}

eval_in_virtual_environment ensure_pep_8_compliance
