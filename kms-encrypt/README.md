# kms-encrypt

## Github Actions Usage

```
    - uses: wacul/actions/kms-encrypt@master
      with:
        kms-key-alias: KMS Alias key name
        file: The file want to encrypt
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        AWS_DEFAULT_REGION: us-east-1
```

## Docker

```
docker run -it --rm -e "AWS_PROFILE=profile" -v $HOME/.aws/:/root/.aws/ -v (pwd)/:/file wacul/kms-encrypt -f /file/Dockerfile -k alias
```
