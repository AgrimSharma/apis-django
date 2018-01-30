#!/usr/bin/env bash

source ./setup.sh

function push {
    cf set-env doctorbox 'ALLOWED_HOSTS' "doctorbox.cfapps.io"
    cf push doctorbox -b python_buildpack
}

eval_in_virtual_environment push
