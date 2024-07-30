GeoTZ v0.0.2a3
--------------

Docs: https://geotz.readthedocs.io/

This is a small library for looking up the timezone for a given country code
and postal code / postal code prefix.

Compared to alternatives like `geopy` or `pgeocode`, it's intended to be
easier to use, less feature rich, and more lightweight.

It uses offline data from www.geonames.org to find the approximate location
and then uses another library to convert that into a timezone.

Please read the LICENSE file for important information about using this
library and the data contained within.

Motivation
----------

1. Easy to use. No API key or external API service required.

2. Fast offline lookup.

3. No downloads required; the necessary data comes bundled with the package.

4. No network requests.

5. I tried to keep the extra dependencies to a minimum.

6. Data is loaded from disk on demand, so as to not use unnecessary memory.

Development
-----------

To run the build, there's the GitHub actions workflows as well as the option to run locally.

For running the build locally, use `pip install tox` and the run `tox` in the repository base
directory (or `tox -p` to run the build in parallel).

1. Ensure you have `tox` installed e.g. by running `pip install tox`

2. Extract data `tox -e extract_data`

3. Run the build: `tox`
