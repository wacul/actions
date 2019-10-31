#!/bin/bash


CMDNAME=`basename $0`
usage() {
  echo "Usage: $CMDNAME [-f FILE] [-k KEY_ALIAS]" 1>&2
  exit 1
}

while getopts f:k: OPT
do
  case $OPT in
    "f")
      FILE="$OPTARG"
      ;;
    "k")
      KEY_ALIAS="$OPTARG"
      ;;
    * )
      usage
      exit 1 ;;
  esac
done

if [[ -z "$FILE" ]]; then
  echo "暗号化する対象ファイルを指定してください"
  usage
fi
if [[ -z "$KEY_ALIAS" ]]; then
  echo "KMSのエイリアスを指定してください"
  usage
fi


ENCRYPTED_FILE="${FILE}.encrypted"

set -e

aws kms encrypt --key-id "alias/${KEY_ALIAS}" --plaintext "fileb://${FILE}" --output text --query CiphertextBlob | base64 --decode > "${ENCRYPTED_FILE}"