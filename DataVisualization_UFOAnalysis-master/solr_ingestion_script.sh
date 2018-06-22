#in solr-7.3.0 <your downloaded versioon> folder
bin/solr start
bin/solr create -c new_core
bin/post -c new_core output_array_json.json
