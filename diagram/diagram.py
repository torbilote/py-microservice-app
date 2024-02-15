from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3, ElasticFileSystemEFSFileSystem
from diagrams.aws.integration import SQS
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DDB, RDSPostgresqlInstance
from diagrams.onprem.analytics import Metabase


with Diagram(name="Architecture", filename="architecture", show=False):
    with Cluster("Terraform") as _:
        with Cluster("External Source") as _:
            data_source = ElasticFileSystemEFSFileSystem("Exporter")

        with Cluster("AWS Cloud") as _:
            s3 = S3("S3")
            sqs = SQS("SQS")
            dynamo_db = DDB("DynamoDB")
            lambda_function = Lambda("Lambda Function")

            sqs >> dynamo_db

        with Cluster("On Premise") as _:
            postgresql = RDSPostgresqlInstance("PostgreSQL")
            metabase = Metabase("Metabase")


    data_source >> s3 >> sqs >> lambda_function >> postgresql >> metabase
