# kms-decrypt

## Github Actions Usage

```
    - uses: wacul/actions/kms-decrypt@master
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        AWS_DEFAULT_REGION: us-east-1
```


## Docker

```
docker run -it --rm -e "AWS_PROFILE=profile" -v $HOME/.aws/:/root/.aws/ -v (pwd)/:/file decrypt -f /file/Dockerfile.encrypted
```
