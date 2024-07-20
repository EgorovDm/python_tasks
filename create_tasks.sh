#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NOSTYLE="\e[0m"
BOLD="\e[1m"
BLINK="\e[5m"

PROMT=$(cat <<-END
Are you sure? This action will overwrite existing files!
Do you want to continue? [N/y]
END
)
printf "${YELLOW}${BOLD}"
read -p "${PROMT}" -n 1 -r
printf "${NOSTYLE}"
if [[ ! ${REPLY} =~ ^[Yy]$ ]]; then 
    printf "\n${RED}${BOLD}>>(-) ${BLINK} canceled ${NOSTYLE} \n\n"
    exit 1
fi

for F_NUM in $(seq 1 ${1}); do
    NAME=task${F_NUM}.py
    touch ./${NAME}
    printf "#!/usr/bin/env python\n\n" > ./${NAME}
    chmod +x ./${NAME}
done && printf "\n${GREEN}${BOLD}>>(+) Files created!\n\n"
