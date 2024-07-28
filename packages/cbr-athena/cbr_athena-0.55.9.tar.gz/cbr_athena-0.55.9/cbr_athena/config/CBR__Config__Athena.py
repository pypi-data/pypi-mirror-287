import requests

from cbr_athena.config.CBR__Config                  import CBR__Config
from cbr_athena.utils.Version                       import version__cbr_athena
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from osbot_utils.base_classes.Type_Safe             import Type_Safe


class CBR__Config__Athena(Type_Safe):
    override__aws_enabled : bool

    def aws_enabled(self):
        if self.cbr_config().get('cbr_website', {}).get('aws_enabled'):
            return True
        if self.override__aws_enabled:
            return True
        return False

    def aws_disabled(self):
        enabled = self.aws_enabled()
        return enabled == False

    @cache_on_self
    def cbr_config(self):
        return CBR__Config().cbr_config().get('cbr_config_data', {}).get('cbr_config', {})

    def cbr_config_athena(self):
        cbr_config = self.cbr_config()
        return dict(aws_enabled = self.aws_enabled() ,
                    cbr_config  = cbr_config         ,
                    version     = version__cbr_athena)

cbr_config_athena = CBR__Config__Athena()