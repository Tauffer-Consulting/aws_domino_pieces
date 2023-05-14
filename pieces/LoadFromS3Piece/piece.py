from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import os
import boto3


class LoadFromS3Piece(BasePiece):
    """
    This Piece loads file or folder contents from a AWS S3 bucket.
    """
    
    def piece_function(self, input_model: InputModel):
        self.session = boto3.Session(
            aws_access_key_id=os.environ.get("LOADFROMS3PIECE_AWS_SECRET_ACCESS_KEY")
            aws_secret_access_key=os.environ.get("LOADFROMS3PIECE_AWS_ACCESS_KEY_ID")
        )
        self.client_s3 = self.session.client("s3")
        self.bucket = self.s3r.Bucket(input_model.bucket_name)

        # Check if target is file or folder, download accordingly...
        input_model.file_or_folder_path

        # Finally, results should return as an Output model
        return OutputModel(
            message=message,
            results_path=
        )

    def download_file_from_s3_folder(self, object_key: str, file_path: str):
        """ref: https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/s3.html#S3.Bucket.download_file"""
        self.bucket.download_file(
            Key=object_key, 
            Filename=file_path
        )
    
    def download_s3_folder(self, s3_folder, local_dir=None):
        """
        Download the contents of a S3 folder, with sub-directories
        ref: https://stackoverflow.com/a/62945526/11483674
        
        Args:
            bucket_name: the name of the s3 bucket
            s3_folder: the folder path in the s3 bucket
            local_dir: a relative or absolute directory path in the local file system
        """
        try:
            for obj in self.bucket.objects.filter(Prefix=s3_folder):
                target = obj.key if local_dir is None \
                    else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
                if not os.path.exists(os.path.dirname(target)):
                    os.makedirs(os.path.dirname(target))
                if obj.key[-1] == '/':
                    continue
                self.bucket.download_file(obj.key, target)
            return None
        except ClientError as e:
            self.logger.exception(e)
            return str(e)