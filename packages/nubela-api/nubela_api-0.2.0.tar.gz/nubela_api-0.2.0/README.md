# Nubela API Client

This project provides a Python client for interacting with the Nubela API, specifically for querying LinkedIn profiles.

## Features

- Easy-to-use interface for querying Nubela profiles
- Caching mechanism to store and reuse previous query results
- Offline mode for development and testing
- Configurable settings using environment variables

## Installation

To install the required dependencies, run:

pip install requests pydantic-settings

## Usage

### Basic usage

from nubela_api import NubelaAPI, NubelaSettings

# Create settings (API key can be set via NUBELA_API_KEY environment variable)
settings = NubelaSettings(api_key="your_api_key_here")

# Initialize the API client
api = NubelaAPI(settings=settings, offline=False)

# Query a LinkedIn profile
linkedin_url = "https://www.linkedin.com/in/example-profile"
response = api.query_linkedin(linkedin_url)

# Access the response data
print(response.full_name)
print(response.occupation)

### Custom parameters

You can pass custom parameters to the API call:

custom_params = {
    "linkedin_profile_url": "https://www.linkedin.com/in/example-profile",
    "extra": "include",
    "skills": "include",
}
response = api.query(custom_params)

### Caching

The client automatically caches responses. To disable caching for a specific query:

response = api.query_linkedin(linkedin_url, use_cache=False)

### Offline mode

For development or testing, you can enable offline mode:

api = NubelaAPI(settings=settings, offline=True)

This will raise a ValueError if an API call is attempted.

## Configuration

You can configure the API client using environment variables:

- NUBELA_API_KEY: Your Nubela API key
- NUBELA_API_ENDPOINT: The API endpoint (default: "https://nubela.co/proxycurl/api/v2/linkedin")

## Error Handling

The client will raise exceptions for various error conditions:

- ValueError: If the API key is missing or if trying to make an API call in offline mode
- OfflineError: Custom exception for offline-related errors (not currently used in the provided code)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your chosen license here]