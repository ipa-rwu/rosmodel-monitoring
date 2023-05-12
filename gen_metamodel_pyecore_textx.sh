#!/bin/bash
METAMODEL_REPO=ipa320/ros-model
METAMODEL_BRANCH=main
PYTHON_PKG_NAME=pythonic_rosmodel_with_textx
PKG_FOLDER=pythonic-rosmodel-with-textx
METAMODEL_FOLDER=${PKG_FOLDER}/${PYTHON_PKG_NAME}/metamodel_gen

METAMODEL_REPO=${1:-$METAMODEL_REPO}
METAMODEL_BRANCH=${2:-$METAMODEL_BRANCH}
METAMODEL_FOLDER=${3:-$METAMODEL_FOLDER}

function log_error {
    local out; out=$(mktemp)
    # shellcheck disable=SC2216
    # shellcheck disable=SC2260
    "$@" &> "$out" | true # '|| err=$?' disables errexit
    local err=${PIPESTATUS[0]}
    if [ "$err" -ne 0 ]; then
        cat "$out"
        echo "'$*' failed"
    fi
    rm -rf "$out"
    return "$err"
}

function run_python {
    log_error venv/*/python "$@"

}

run_python -m textx_pyecoregen.cli --ecore-model https://raw.githubusercontent.com/"$METAMODEL_REPO"/"$METAMODEL_BRANCH"/plugins/de.fraunhofer.ipa.ros/model/ros.ecore -o "$METAMODEL_FOLDER"  --auto-register-package --with-dependencies

# fix python module name
sed -i "s/^from primitives/from ${PYTHON_PKG_NAME}.metamodel_gen.primitives/" ${PKG_FOLDER}/${PYTHON_PKG_NAME}/metamodel_gen/ros/__init__.py
sed -i "s/^from primitives/from ${PYTHON_PKG_NAME}.metamodel_gen.primitives/" ${PKG_FOLDER}/${PYTHON_PKG_NAME}/metamodel_gen/ros/ros.py
sed -i "s/^from type/from pyecore.type/" ${PKG_FOLDER}/${PYTHON_PKG_NAME}/metamodel_gen/ros/ros.py

isort ${PKG_FOLDER}/${PYTHON_PKG_NAME}/metamodel_gen

find ${PKG_FOLDER}/${PYTHON_PKG_NAME}/metamodel_gen -name '*.py' -exec autopep8 --in-place '{}' \;
