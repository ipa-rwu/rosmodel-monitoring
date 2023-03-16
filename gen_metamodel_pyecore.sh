#!/bin/bash
METAMODEL_REPO=ipa-nhg/ros-model
METAMODEL_BRANCH=YamlMigrationSystem
METAMODEL_FOLDER=pythonic-rosmodel/pythonic_rosmodel/metamodel_gen

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
sed -i 's/^from primitives/from pythonic_rosmodel.metamodel_gen.primitives/' pythonic-rosmodel/pythonic_rosmodel/metamodel_gen/ros/__init__.py
sed -i 's/^from primitives/from pythonic_rosmodel.metamodel_gen.primitives/' pythonic-rosmodel/pythonic_rosmodel/metamodel_gen/ros/ros.py
sed -i 's/^from type/from pyecore.type/' pythonic-rosmodel/pythonic_rosmodel/metamodel_gen/ros/ros.py

isort pythonic-rosmodel/pythonic_rosmodel/metamodel_gen

find pythonic-rosmodel/pythonic_rosmodel/metamodel_gen -name '*.py' -exec autopep8 --in-place '{}' \;
