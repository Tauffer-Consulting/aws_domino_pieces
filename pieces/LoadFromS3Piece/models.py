from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Input model for LoadFromS3Piece.
    """
    aws_region_name: str = Field(
        description="The AWS region name."
    )
    bucket_name: str = Field(
        description="The name of the S3 bucket."
    )
    file_or_folder_path: str = Field(
        description="The path to file or folder to be loaded."
    )


class OutputModel(BaseModel):
    """
    Output model for LoadFrom3Piece.
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )
    results_path: str = Field(
        description="The path to the downloaded content."
    )


class SecretsModel(BaseModel):
    LOADFROMS3PIECE_AWS_SECRET_ACCESS_KEY: str = Field(
        description="AWS secret access key."
    )
    LOADFROMS3PIECE_AWS_ACCESS_KEY_ID: str = Field(
        description="AWS access key id."
    )