#! /bin/sh

# Re-vendors Bootstrap into the repo. The build does not run `npm install`
# (see .github/workflows/deploy.yml) -- it compiles the Sass in _sass/bootstrap
# and serves the bundle in assets/javascript/bootstrap, both of which are
# checked in. Run this script to refresh those vendored copies.
#
# Installs the version declared in package.json rather than @latest, so the
# vendored copy and the manifest cannot drift apart.

set -e

rm -rf node_modules package-lock.json
npm install

rm -rf _sass/bootstrap
mkdir -p _sass/bootstrap
cp -r node_modules/bootstrap/scss/* _sass/bootstrap
touch _sass/bootstrap/__DO_NOT_MODIFY

rm -rf assets/javascript/bootstrap
mkdir -p assets/javascript/bootstrap
cp node_modules/bootstrap/dist/js/bootstrap.bundle.min.js assets/javascript/bootstrap/
touch assets/javascript/bootstrap/__DO_NOT_MODIFY

rm -rf node_modules package-lock.json
