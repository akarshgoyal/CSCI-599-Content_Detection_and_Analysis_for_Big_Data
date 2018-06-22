git clone https://github.com/manalishah/mitie-resources
cd mitie-resources
# absolute path to mitie-resources folder
export NER_RES=$PWD
chmod a+x install.sh
./install.sh

export TIKA_APP=/Users/akarshgoyal/Documents/GitHub/tika-trunk/tika-app/target/tika-app-2.0.0-SNAPSHOT.jar

java -Djava.library.path=$NER_RES/MITIE/mitielib -Dner.mitie.model=$NER_RES/MITIE/MITIE-models/english/ner_model.dat -Dner.impl.class=org.apache.tika.parser.ner.mitie.MITIENERecogniser -classpath $NER_RES/MITIE/mitielib/javamitie.jar:$TIKA_APP org.apache.tika.cli.TikaCLI --config=$NER_RES/tika-config.xml -m description_only.csv

