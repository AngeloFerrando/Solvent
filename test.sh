#!/bin/bash

if [ "$#" -eq 2 ]; then
    folder_path="./examples"

    # Check if the folder exists
    if [ -d "$folder_path" ]; then
        # Use a for loop to iterate through files in the folder
        for file in "$folder_path"/*; do
            echo -n "$(basename "$file") "
            start_time=$(date +%s.%N)
            python3 main.py $file $1 $2 > output.py
            end_time=$(date +%s.%N)
            elapsed_time_compilation=$(echo "$end_time - $start_time" | bc)
            start_time=$(date +%s.%N)
            python3 output.py > .tmp
            end_time=$(date +%s.%N)
            elapsed_time_verification=$(echo "$end_time - $start_time" | bc)
            if  (grep -q '(=> liquid)' .tmp && grep -q '(=> not liquid)' .tmp); then
                echo -n -e "\e[1;33m?\e[0m"
            elif (grep -q '(=> liquid)' .tmp) then
                echo -n -e "\e[32m\u2714\e[0m"
            else
                echo -n -e "\e[31m\u2717\e[0m"
            fi
            echo " (Compilation time: $elapsed_time_compilation [sec], Verification time: $elapsed_time_verification [sec])"
        done
    else
        echo "Folder not found: $folder_path"
    fi
else
    echo "You have to pass two arguments: <number of transactions> <number of participants>"
fi