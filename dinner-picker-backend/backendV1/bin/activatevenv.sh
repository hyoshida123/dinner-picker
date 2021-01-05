#! /bin/bash

echo "Running activate script"

venv=$DP_VENV

if [[ "$venv" != "dinner-picker-venv" ]]; then
    echo "no virtualenv name set or wrong virtual env name. set \$DP_VENV=`dinner-picker-venv` in your ~/.bash_profile"
    exit 123
    fi

if [[ -z $VIRTUALENVWRAPPER_SCRIPT ]] || [[ $VIRTUALENVWRAPPER_SCRIPT != */virtualenvwrapper.sh ]]; then
    echo "Set \$VIRTUALENVWRAPPER_SCRIPT. It should be a path to virtuanenvwrapper.sh"
    exit 123
fi

source $VIRTUALENVWRAPPER_SCRIPT
workon $venv
