class Unauthorized(Exception):
    """Raised when the API request is unauthorized (HTTP 401)."""
    pass

class DailyUsageLimitExceeded(Exception):
    """Raised when the API daily usage limit is exceeded or query is empty."""
    pass

class MonthlyUsageLimitExceeded(Exception):
    """Raised when the API monthly usage limit is exceeded or query is empty."""
    pass

class InvalidMembership(Exception):
    """Raised when the user has no membership."""
    pass

class InvalidQuery(Exception):
    """Raised when the query is invalid (e.g., empty string)."""
    pass
