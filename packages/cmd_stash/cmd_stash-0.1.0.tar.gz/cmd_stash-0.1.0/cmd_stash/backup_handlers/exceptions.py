# backup_handlers/aws_exceptions.py


class AWSBackupException(Exception):
    """Base exception class for AWS backup-related errors."""

    pass


class AWSBucketCreationException(AWSBackupException):
    """Exception raised for errors during AWS bucket creation."""

    pass


class AWSBucketDeletionException(AWSBackupException):
    """Exception raised for errors during AWS bucket deletion."""

    pass


class AWSResourceNotFoundException(AWSBackupException):
    """Exception raised when an AWS resource is not found."""

    pass
