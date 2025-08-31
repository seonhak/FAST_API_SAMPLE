class ServiceError(Exception):
    """서비스 로직에서 발생하는 공용 에러"""
    def __init__(self, message: str, status_code: int = 500, data=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.data = data