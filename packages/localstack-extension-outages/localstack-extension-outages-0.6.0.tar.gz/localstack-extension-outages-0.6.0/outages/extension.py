import logging
from localstack.aws.chain import CompositeHandler
from localstack.extensions.api import Extension
from localstack.extensions.api.http import RouteHandler,Router
from outages.constants import CONFIG_ENDPOINT,CONFIG_PATH
from outages.handlers import OutageHandler
from outages.routes import handle_delete_config,handle_get_config,handle_patch_config,handle_post_config
LOG=logging.getLogger(__name__)
class OutagesExtension(Extension):
	name='outages'
	def on_extension_load(A):logging.getLogger(__name__).setLevel(logging.WARNING);LOG.warning('Outages Extension is deprecated. Please migrate to the Chaos API: https://docs.localstack.cloud/user-guide/chaos-engineering/chaos-api/')
	def update_gateway_routes(B,router):A=router;A.add(CONFIG_PATH,handle_get_config,methods=['GET'],host=CONFIG_ENDPOINT);A.add(CONFIG_PATH,handle_post_config,methods=['POST'],host=CONFIG_ENDPOINT);A.add(CONFIG_PATH,handle_patch_config,methods=['PATCH'],host=CONFIG_ENDPOINT);A.add(CONFIG_PATH,handle_delete_config,methods=['DELETE'],host=CONFIG_ENDPOINT)
	def update_request_handlers(A,handlers):handlers.handlers.append(OutageHandler())