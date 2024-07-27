from geodesic.bases import _APIObject
from geodesic.descriptors import (
    _StringDescr,
    _BoolDescr,
    _ListDescr,
    _DictDescr,
    _IntDescr,
    _BaseDescr,
    _FloatDescr,
    _TypeConstrainedDescr,
)
from geodesic.boson.middleware import MiddlewareConfig
from geodesic.boson.tile_options import TileOptions
from geodesic.boson.servicer_settings import ServicerSettings

# Credential Keys
DEFAULT_CREDENTIAL_KEY = "default"
STORAGE_CREDENTIAL_KEY = "storage"
API_CREDENTIAL_KEY = "api"


class CacheConfig(_APIObject):
    enabled = _BoolDescr(doc="enable/disable caching for a particular provider")
    ttl_seconds = _FloatDescr(doc="time to live for cached items in seconds")


class BosonConfig(_APIObject):
    """BosonConfig Provider Configuration

    This tells Boson how it should access the underlying data.
    """

    provider_name = _StringDescr(doc="the name of the provider this Boson uses")
    url = _StringDescr(doc="the url of the service this refers to (if any)")
    thread_safe = _BoolDescr(doc="is this particular provider implementation thread safe")
    pass_headers = _ListDescr(doc="list of headers that this provider should pass to backend")
    max_page_size = _IntDescr(doc="the max number of records this provider can page through")
    properties = _DictDescr(doc="additional provider-specific properties")
    credentials = _DictDescr(doc="credentials that are needed by this provider")
    middleware = _TypeConstrainedDescr((MiddlewareConfig, dict), doc="user configured middleware")
    cache = _TypeConstrainedDescr((CacheConfig, dict), doc="user configured cache config")
    tile_options = _TypeConstrainedDescr((TileOptions, dict), doc="user configured tile options")
    servicer_settings = _TypeConstrainedDescr(
        (ServicerSettings, dict), doc="user configured servicer settings"
    )


class BosonDescr(_BaseDescr):
    """A Boson Provider Config

    __get__ returns a BosonConfig object

    __set__ sets from a dictionary or BosonConfig, coercing to a BosonConfig if needed and stores internally to the
            APIObject dict
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._type = (BosonConfig, dict)

    def _get(self, obj: object, objtype=None) -> dict:
        # Try to get the private attribute by name (e.g. '_boson_config')
        b = getattr(obj, self.private_name, None)
        if b is not None:
            # Return it if it exists
            return b

        try:
            b = self._get_object(obj)
            if isinstance(b, dict):
                b = BosonConfig(**b)
            self._set(obj, b)
            setattr(obj, self.private_name, b)
        except KeyError:
            if self.default is None:
                self._attribute_error(objtype)
            self._set(obj, self.default)
            return self.default
        return b

    def _set(self, obj: object, value: object) -> None:
        # Reset the private attribute (e.g. "_boson_config") to None
        setattr(obj, self.private_name, None)

        if isinstance(value, BosonConfig):
            self._set_object(obj, value)
        elif isinstance(value, dict):
            self._set_object(obj, BosonConfig(**value))
        else:
            raise ValueError(f"invalid value type {type(value)}")

    def _validate(self, obj: object, value: object) -> None:
        if not isinstance(value, (BosonConfig, dict)):
            raise ValueError(f"'{self.public_name}' must be a BosonConfig or a dict")

        try:
            BosonConfig(**value)
        except Exception as e:
            raise ValueError("boson config is invalid") from e
