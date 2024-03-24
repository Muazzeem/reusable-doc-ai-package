from google.api_core.exceptions import GoogleAPIError


class DocAIException(GoogleAPIError):
    """
    Custom exception class for Document AI errors.

    Attributes:
        processor_name (str): Name of the document processor.
        error (str): Error message describing the exception.
    """

    def __init__(self, processor_name, error, *args: object, **kwargs) -> None:
        """
        Initialize the DocAIException instance.

        Args:
            processor_name (str): Name of the document processor.
            error (str): Error message describing the exception.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.processor_name = processor_name
        self.error = error
        super().__init__(*args, **kwargs)
