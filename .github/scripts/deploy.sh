#!/bin/sh

# create a new build directory to build a tgz file containing the project
mkdir build
cp * build
cp -r mycollection build
cp -r collection build
tar -czf mycollection.tgz build
# transfer the tgz file to a custom server
export SSHPASS=$DEPLOY_PASS
sshpass -e scp -o stricthostkeychecking=no mycollection.tgz $DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_PATH
# run a deploy script in the server to finally deploy the project
sshpass -e ssh -o stricthostkeychecking=no $DEPLOY_USER@$DEPLOY_HOST $DEPLOY_SCRIPT_PATH/deploy.sh