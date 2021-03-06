from typing import List

from drf_spectacular import openapi


class AutoSchema(openapi.AutoSchema):
    def _get_response_bodies(self):
        defaults = {
            "200": {"description": "OK"},
            "400": {"description": "Bad Request"},
            "405": {"description": "Method Not Allowed"},
            "500": {"description": "Internal Error"},
        }
        if self.view.action != "list":
            defaults["404"] = {"description": "Not Found"}
        defaults.update(super()._get_response_bodies())
        return defaults

    def get_tags(self) -> List[str]:
        try:
            return [self._get_verbose_name_plural().capitalize()]
        except AttributeError:
            return super().get_tags()

    def get_summary(self):
        if self.view.action == "list":
            return f"Get list of {self._get_verbose_name_plural()}"
        if self.view.action == "retrieve":
            return f"Get a {self._get_verbose_name()}"
        return super().get_summary()

    def _get_verbose_name(self):
        return self._get_model_meta().verbose_name

    def _get_verbose_name_plural(self):
        return self._get_model_meta().verbose_name_plural

    def _get_model_meta(self):
        # noinspection PyProtectedMember
        return self.view.serializer_class.Meta.model._meta
