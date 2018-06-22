#Create a directory for keeping all the models.
#Choose any convenient path but make sure to use absolute path
export NER_RES=/Users/akarshgoyal/Documents/GitHub/tika-trunk/tika-parsers/target/classes
mkdir -p $NER_RES
cd $NER_RES

PATH_PREFIX="$NER_RES/org/apache/tika/parser/ner/opennlp"
URL_PREFIX="http://opennlp.sourceforge.net/models-1.5"

mkdir -p $PATH_PREFIX

# using three entity types from the above table for demonstration
wget "$URL_PREFIX/en-ner-person.bin" -O $PATH_PREFIX/ner-person.bin
wget "$URL_PREFIX/en-ner-location.bin" -O $PATH_PREFIX/ner-location.bin
wget "$URL_PREFIX/en-ner-organization.bin" -O $PATH_PREFIX/ner-organization.bin

export TIKA_APP=/Users/akarshgoyal/Documents/GitHub/tika-trunk/tika-app/target/tika-app-2.0.0-SNAPSHOT.jar

java -classpath $NER_RES:$TIKA_APP org.apache.tika.cli.TikaCLI --config=tika-config.xml -m description_only.csv

# Are there any metadata keys starting with "NER_" ?