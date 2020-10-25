#!/bin/sh

export AWS_CONFIG_FILE='../.my-aws-config'
inputFile="../tmp/samplefile.xml"

echo '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' > "${inputFile}"
echo '<tester>' >> "${inputFile}"
echo '</tester>' >> "${inputFile}"

# May need: `chmod +x upload_s3.sh`

if ../src/upload_object_s3.sh "${inputFile}" 'sample-bucket' 'us-east-2' 'STANDARD' 'myDirectoryName/myTwoFileName.xml'; then
  echo 'OK'
  rm "${inputFile}"
else
  echo "Failed ($?)"
fi