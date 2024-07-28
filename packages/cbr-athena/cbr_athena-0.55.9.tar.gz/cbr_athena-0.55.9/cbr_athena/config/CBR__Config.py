from osbot_utils.base_classes.Type_Safe             import Type_Safe
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from osbot_utils.utils.Env                          import get_env
from osbot_utils.utils.Http                         import is_url_online, GET_json

CBR_CONFIG__DEFAULT_PORT   = '3000'
CBR_CONFIG__DEFAULT_SERVER = 'localhost'
CBR_CONFIG__DEFAULT_SCHEMA = 'http'
CBR_CONFIG__PATH__ACTIVE   = '/site_info/cbr-config-active'

class CBR__Config(Type_Safe):
    port    : str
    server  : str = CBR_CONFIG__DEFAULT_SERVER
    schema  : str = CBR_CONFIG__DEFAULT_SCHEMA


    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.port   = self.port or get_env('PORT', CBR_CONFIG__DEFAULT_PORT)

    def cbr_config(self):
        return dict(cbr_config_data      = self.cbr_config_data         (),
                    cbr_config_available = self.is_cbr_config_available (),
                    cbr_config_url       = self.url__cbr_config         ())

    def cbr_config_data(self):
        if self.is_cbr_config_available():
            return GET_json(self.url__cbr_config())
        return {}

    def url__cbr_config(self):
        return f'{self.schema}://{self.server}:{self.port}{CBR_CONFIG__PATH__ACTIVE}'

    def url__open_api_json(self):
        return f'{self.schema}://{self.server}:{self.port}/openapi.json'

    @cache_on_self
    def is_cbr_config_available(self):                          # todo figure out why this takes quite a long time (from 200ms to 400ms)
        return is_url_online(self.url__open_api_json())
