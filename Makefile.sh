#!/bin/bash

# Default value
DEFAULT_N_TRANSACTIONS=100

# If no argument is provided, use the default value
if [ -z "$N_Transactions" ]; then
    N_Transactions=$DEFAULT_N_TRANSACTIONS
fi

compile() {
    clean
    python3 main.py "$1" "$2" "$3"
    python3 outputTrace.py
    python3 outputState.py
}

set_logic() {
    for Prop in out/*; do
        for file in $(find "$Prop/tracebased" -type f -name '*.smt2' | sort); do
            sed -i "1s/^/$1\\n/" "$file"
        done
    done

    for Prop in out/*; do
        for file in $(find "$Prop/statebased" -type f -name '*.smt2' | sort); do
            sed -i "1s/^/$1\\n/" "$file"
        done
    done
}

run() {
    for Prop in out/*; do
        echo "PROPERTY: $Prop"
        foundUNSAT=false
        for file in $(find "$Prop/statebased" -type f -name '*.smt2' | sort); do
            foundSAT=false
            output=$($1 "$file")
            if [ "$output" = "unsat" ]; then
                foundUNSAT=true
                break
            elif [ "$output" = "sat" ]; then
                foundSAT=true
            fi
        done

        if [ "$foundUNSAT" = "true" ]; then
            echo "STRONG UNSAT (=> LIQUID)"
        elif [ "$foundSAT" = "true" ]; then
            echo "WEAK SAT (=> NOT LIQUID?)"
            for i in $(find "$Prop/tracebased/" -mindepth 1 -maxdepth 1 -type d | sort); do
                foundUNSAT=false
                for file in $(find "$i" -type f -name '*.smt2' | sort); do
                    foundSAT=false
                    output=$($1 "$file")
                    if [ "$output" = "unsat" ]; then
                        foundUNSAT=true
                        echo "step $(basename "$i"): WEAK UNSAT (=> LIQUID?) in $(basename "$j") steps"
                        break
                    elif [ "$output" = "sat" ]; then
                        foundSAT=true
                    fi
                done
                if [ "$foundUNSAT" = "false" ] && [ "$foundSAT" = "true" ]; then
                    echo "STRONG SAT (=> NOT LIQUID)"
                    break
                fi
            done
        fi
    done
}

clean() {
    rm -rf out/*
}

# Main entry point
if [ "$1" == "compile" ]; then
    compile "$2" "$3" "$4"
elif [ "$1" == "set-logic" ]; then
    set_logic "$2"
elif [ "$1" == "run" ]; then
    run "$2"
elif [ "$1" == "clean" ]; then
    clean
elif [ "$1" == "all" ]; then
    compile "$2" "$3" "$4"
    run
else
    echo "Usage: $0 [compile|run|clean|set-logic|all] [Contract] [N_Transactions] [N_Participants]"
    exit 1
fi
