class FrameworkException(Exception):
    """Base exception for the automation framework."""
    pass


class APIException(FrameworkException):
    """Raised for API-related framework failures."""
    pass


class UIException(FrameworkException):
    """Raised for UI/browser-related framework failures."""
    pass


class DatabaseException(FrameworkException):
    """Raised for database-related framework failures."""
    pass


class ConfigurationException(FrameworkException):
    """Raised when framework configuration is invalid."""
    pass