#!/bin/bash

set -eox pipefail

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
cd "$SCRIPT_DIR" || exit

python -m venv .venv
source .venv/bin/activate

cd ../../wrapper/py
bash build.sh
pip install --force dist/trust_spec_gen-*-py3-none-any.whl

cd $SCRIPT_DIR
trust help
