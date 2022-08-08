# Pyspark Local - AWS Glue 3

pyspark aws glue locally in docker container.  Pulled from this [aws blog post](https://aws.amazon.com/blogs/big-data/develop-and-test-aws-glue-version-3-0-jobs-locally-using-a-docker-container/)

## Usage

- Update the path to your projects in `.envrc` - where you put this repo
- run the just recipe
  - Set up with docker compose (and created just recipe) for running unit tests with a spark context.

## Note

- with jupyter lab, there is an error message from the docker container: `Permission denied: '/home/glue_user/.jupyter/lab/workspaces'`
  - it doesn't seem to effect the running of the script in jupyter lab
