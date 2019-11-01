#!/bin/bash


CMDNAME=`basename $0`
usage() {
  echo "Usage: $CMDNAME [-a or [-f FILE]]" 1>&2
  exit 1
}

while getopts af: OPT
do
  case $OPT in
    "a") ALL_FILE=1;;
    "f") FILE="$OPTARG";;
    * )
      usage
      exit 1 ;;
  esac
done

if [[ -z "$FILE" ]] || [[ -z "$ALL_FILE" ]]; then
  echo "It must be called with `-f <ENCRYPTED FILE>` or `-a`"
  usage
fi

set -e

if [[ "${ALL_FILE}" -eq 1 ]]; then
  find ./ -type f -name '*.encrypted' | while read -r ENCRYPTED_FILE; do
    RAW_FILE=${ENCRYPTED_FILE%.encrypted}
    aws kms decrypt --ciphertext-blob "fileb://${ENCRYPTED_FILE}" --query Plaintext --output text | base64 --decode > "${RAW_FILE}"
  done
else
  RAW_FILE=${FILE%.encrypted}
  aws kms decrypt --ciphertext-blob "fileb://{FILE}" --query Plaintext --output text | base64 --decode > "${RAW_FILE}"
fi
