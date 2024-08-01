class VegaClientError(IOError):
    def __init__(self, *args, **kwargs):
        super(VegaClientError, self).__init__(*args, **kwargs)


class ConfigError(VegaClientError):
    pass


class Timeout(VegaClientError):
    pass


class RequestMalformed(VegaClientError):
    pass


class RequestUnauthorized(VegaClientError):
    pass


class RequestForbidden(VegaClientError):
    pass


class ObjectNotFound(VegaClientError):
    pass


class ObjectAlreadyExists(VegaClientError):
    pass


class ObjectUnprocessable(VegaClientError):
    pass


class ServerError(VegaClientError):
    pass


class ServiceUnavailable(VegaClientError):
    pass


class HTTPStatus0Error(VegaClientError):
    pass


class InvalidParameter(VegaClientError):
    pass
