#!/usr/bin/env python3
import sys
from google.cloud import storage
from google.oauth2 import service_account

KEY_PATH = "service_account_key.json"

credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
client = storage.Client(credentials=credentials, project=credentials.project_id)

bucket_name = sys.argv[1]
bucket = client.bucket(bucket_name)

blobs = bucket.list_blobs()
for blob in blobs:
    print(blob.name)

blob_name = "test.txt"
# write to a bucket
blob = bucket.blob(blob_name)
blob.upload_from_string("this is a test äöüß")

# read from a bucket
blob = bucket.blob(blob_name)
print(blob.download_as_bytes().decode("utf-8"))
