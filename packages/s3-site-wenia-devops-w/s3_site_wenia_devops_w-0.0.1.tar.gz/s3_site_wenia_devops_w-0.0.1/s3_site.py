"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

class S3Site:
    def __init__(self, bucket_name, index_file_name):
        self.bucket = bucket_name
        self.index_file = index_file_name

# Create an AWS resource (S3 Bucket)
    def run(self):
        bucket = s3.Bucket(self.bucket, 
                        website=s3.BucketWebsiteArgs(
                        index_document=self.index_file,
            ),)

        # Create an S3 Bucket object

        ownership_controls = s3.BucketOwnershipControls(
            'ownership-controls',
            bucket=bucket.id,
            rule=s3.BucketOwnershipControlsRuleArgs(
                object_ownership='ObjectWriter',
            ),
        )

        public_access_block = s3.BucketPublicAccessBlock(
            'public-access-block', bucket=bucket.id, block_public_acls=False
        )

        s3.BucketObject(
            'index.html',
            bucket=bucket.id,
            source=pulumi.FileAsset(self.index_file),
            content_type='text/html',
            acl='public-read',
            opts=pulumi.ResourceOptions(depends_on=[public_access_block, ownership_controls]),
        )

        # Export the name of the bucket
        pulumi.export('bucket_name', bucket.id)
        pulumi.export('bucket_endpoint', pulumi.Output.concat('http://', bucket.website_endpoint))
