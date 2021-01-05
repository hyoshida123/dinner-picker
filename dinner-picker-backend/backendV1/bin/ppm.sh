#!/bin/bash

# functions
show_help_install_dependency() {
    echo_newline
    echo_help_line
    echo "ppm install [packageName]: download [packagename] and write it to dev.txt"
    echo "ppm install [packageName] --[dev|test|base|prod]: download the [package] and write it to --[dev|test|base|prod]"
}

function show_help_install() {
    echo_newline
    echo_help_line
    echo "ppm install [nameOfThePackage] --[dev|test|base|prod]: download the package and copy into requirements/[dev|test|base|prod]"
    echo "ppm install: download all the pacakages in dev.txt"
    echo "ppm install --[dev|test|base|prod]: download all the packages in requirements/[dev|test|base|prod]"
}

function show_help_method() {
    echo_newline
    echo_help_line
    echo "ppm install: install packages. add -h or --help if you want to see a help message"
    echo "ppm start: run the ppm script"
    echo "ppm status: show all the dependencies"
    echo "ppm clean: delete all the __pycache__ in subdirectories"
    echo "ppm migrate: same as makemigrations + migrate"
}

function show_help_clean() {
    echo_newline
    echo_help_line
    echo "ppm clean pycache: clean all the pycahe data"
    echo "ppm clean migratefiles: clean all the migration files"
}

function activate_virtualenv() {
    echo_newline
    if [[ "$VIRTUALENV_ACTIVATED" != "YES" ]]; then
        echo "activate virtualenv"
        source $DP/bin/activatevenv.sh
        if [[ "$VIRTUALENV_ACTIVATED" != "YES" ]]; then
            echo "======================================================"
            echo "Error: NO \$VIRTUALENV_ACTIVATED environment variable set in postactivate & predeactivate"
            echo "Add export \$VIRTUALENV_ACTIVATED='YES' to the postactivate"
            echo "Ad unset \$VIRTUALENV_ACTIVATED to predeactivate"
            echo "in $WORKON_HOME/$DP_VENV/bin/postactivate | predeactivate"
            deactivate
        fi
    fi
}

function show_dependencies() {
    echo_newline
    echo "==========dependencies============="
    pip freeze
}

function echo_newline() {
    echo ""
}

function echo_help_line() {
    echo "=======help message========="
}

echo_newline
echo "ppm script is running"

if [[ -z $DP ]]; then
  echo "Error: Set \$DP environment variable to be backendV1"
  exit 123
fi

if [[ "$DP_VENV" != "dinner-picker-venv" ]]; then
    echo "Error: Wrong \$DP_VENV environment variable. It should be dinner-picker-venv. Add it to ~/.bash_profile"
    exit 123
fi

# Main()
activate_virtualenv

case "$1" in
        start)
            python $DP/manage.py runserver
            ;;

        -h|-\?|--help)
            show_help_method
            ;;

        migrate)
            python $DP/manage.py makemigrations
            python $DP/manage.py migrate
            ;;

        activate)
            activate_virtualenv
            ;;

        install)
            if [ -z $2 ]
              then
                pip install -r $DP/requirements/dev.txt

            # if second argument exists
            else
                case "$2" in
                    # options
                    -h|-\?|--help)
                        show_help_install
                        ;;
                    --dev)
                        pip install -r $DP/requirements/dev.txt
                        echo "download dependencies in dev.txt"
                        ;;
                    --test)
                        pip install -r $DP/requirements/test.txt
                        echo "download dependencies in test.txt"
                        ;;
                    --prod)
                        pip install -r $DP/requirements/prod.txt
                        echo "download dependencies in prod.txt"
                        ;;
                    --base)
                        pip install -r $DP/requirements/base.txt
                        echo "download dependencies in base.txt"
                        ;;
                     --*)
                        echo "Option is not supported. It should be either --[dev|test|prod|base]"
                        ;;
                    # parameter
                    *)
                        if [ -z $3 ]
                        then
                            pip install $2 && pip freeze > $DP/requirements/dev.txt

                        # if third arguments exist
                        else
                            case "$3" in
                                #options
                                -h|-\?|--help)
                                    show_help_install_dependency
                                    ;;
                                --dev)
                                    pip install $2 && pip freeze > $DP/requirements/dev.txt
                                    echo "added dependency list to dev.txt"
                                    ;;
                                --test)
                                    pip install $2 && pip freeze > $DP/requirements/test.txt
                                    echo "added dependency list to test.txt"
                                    ;;
                                --prod)
                                    echo "prod is not supported now"
                                    ;;
                                --base)
                                    pip install $2 && pip freeze > $DP/requirements/base.txt
                                    echo "added dependency list to base.txt"
                                    ;;
                                 --*)
                                    echo "Option is not supported. It should be either --[dev|test|base]"
                                    ;;
                            esac
                        fi
                        ;;
                esac
            fi
            ;;

        status)
            show_dependencies
            ;;
        clean)
            if [ -z $2 ]
              then
                show_help_clean
            # if second argument exists
            else
                case "$2" in
                pycache)
                    # delete all the __pycache__
                    echo 'delete all the __pycahce__ under your' $DP
                    find $DP -name '__pycache__' -exec rm -rf {} \;
                    ;;
                migratefiles)
                    echo "this is not supported yet"
                    ;;
                --*)
                    echo "Option is not supported. It should be either [pycahce|migratefiles]"
                    ;;
                esac
            fi
            ;;
        *)
            echo $"Usage: $0 {start|install|restart}"
            ;;
esac

echo_newline
