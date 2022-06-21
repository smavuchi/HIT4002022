import flask

from ..blueprint import blueprint

from app.helpers.router import router
from app.services.docs.get_all import get_api_documentation as _get_api_documentation

route = router.routes["get api documentation"]

@blueprint.route(route.url, methods=route.methods)
def get_api_documentation(**kwargs):
  return _get_api_documentation()