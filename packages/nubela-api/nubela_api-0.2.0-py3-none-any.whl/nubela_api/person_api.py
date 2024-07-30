from dataclasses import dataclass, field
from typing import Any, Optional

import requests
from pydantic_settings import BaseSettings, SettingsConfigDict

from nubela_api.models.response import Response


class NubelaSettings(BaseSettings):
    api_key: str = ""
    api_endpoint: str = "https://nubela.co/proxycurl/api/v2/linkedin"
    offline: bool = False

    model_config = SettingsConfigDict(env_prefix="nubela_")


def param_hash(d: dict | list | object) -> int:
    """Convert dict/lists/primitives to a hash"""
    if isinstance(d, dict):
        items = sorted((key, param_hash(value)) for key, value in d.items())
        return hash(frozenset(items))
    # Convert lists to tuples of hashed elements
    elif isinstance(d, list):
        t = tuple(param_hash(item) for item in d)
        return hash(t)
    # For other types, use the default hash value
    else:
        return hash(d)


class OfflineError(Exception):
    pass


@dataclass
class NubelaAPI:
    existing_queries: dict[int, Response] = field(default_factory=dict)

    settings: NubelaSettings = field(default_factory=NubelaSettings)

    def __post_init__(self):
        if not self.settings.api_key:
            raise ValueError("api_key is required")

    def _api_call(self, params: dict[str, Any]) -> dict[str, Any]:
        if self.settings.offline:
            raise ValueError("Offline mode is enabled. Set offline=False to make API calls.")
        headers = {"Authorization": "Bearer " + self.settings.api_key}
        data = requests.get(self.settings.api_endpoint, params=params, headers=headers).json()
        return data

    def save_profile_query(self, params: dict[str, Any], response: Response):
        hsh = param_hash(params)
        self.existing_queries[hsh] = response

    def _default_params(self) -> dict[str, Any]:
        params = {
            "extra": "include",
            "github_profile_id": "include",
            "facebook_profile_id": "include",
            "twitter_profile_id": "include",
            "personal_contact_number": "include",
            "personal_email": "include",
            "inferred_salary": "include",
            "experience": "include",
            "skills": "include",
            "use_cache": "if-present",
            "fallback_to_cache": "on-error",
        }
        return params

    def query_linkedin(
        self,
        linkedin_url: str,
        params: Optional[dict[str, Any]] = None,
        use_cache: bool = True,
    ) -> Response:
        if not params:
            params = self._default_params()
        params["linkedin_profile_url"] = linkedin_url
        return self.query(params, use_cache=use_cache)

    def query(self, params: dict[str, Any], use_cache: bool = True) -> Response:
        hsh = param_hash(params)
        if use_cache:
            if hsh in self.existing_queries:
                return self.existing_queries[hsh]

        data = self._api_call(params)
        try:
            r = Response(query=params, **data)
        except:
            raise
        self.existing_queries[hsh] = r
        if use_cache:
            self.save_profile_query(params, r)
        return r
