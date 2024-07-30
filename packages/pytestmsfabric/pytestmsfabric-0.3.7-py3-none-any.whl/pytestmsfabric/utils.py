from pyspark.sql import SparkSession

def get_workspace_id() -> str:
    """Return the workspace ID."""
    msg = "You are not running in a Fabric workspace. Please add --workspace-id to the command line."
    spark = SparkSession.getActiveSession()
    if spark is None:
        raise AttributeError(msg)

    res = spark.conf.get("trident.workspace.id")
    if res is None:
        raise AttributeError(msg)

    return res
