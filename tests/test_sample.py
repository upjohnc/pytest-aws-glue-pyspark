import sys

import pytest
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession

import sample


@pytest.fixture(scope="module", autouse=True)
def glue_context():
    sys.argv.append("--JOB_NAME")
    sys.argv.append("test_count")

    args = getResolvedOptions(sys.argv, ["JOB_NAME"])
    context = GlueContext(SparkSession.builder.getOrCreate())
    job = Job(context)
    job.init(args["JOB_NAME"], args)

    yield (context)

    job.commit()


def test_counts(glue_context):
    file = "s3://awsglue-datasets/examples/us-legislators/all/persons.json"
    dyf = sample.read_json(glue_context, file)
    assert dyf.toDF().count() == 1961
