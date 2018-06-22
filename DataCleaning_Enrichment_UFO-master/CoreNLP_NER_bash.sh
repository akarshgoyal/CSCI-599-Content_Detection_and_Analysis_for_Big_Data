


git clone https://github.com/thammegowda/tika-ner-corenlp.git
cd tika-ner-corenlp
mvn clean compile package assembly:single -PtikaAddon

#this should produce target/tika-ner-corenlp-addon-*-jar-with-dependencies.jar
export CORE_NLP_JAR=`find $PWD/target/tika-ner-corenlp-addon-*jar-with-dependencies.jar`

echo $PWD 
export TIKA_APP=/Users/akarshgoyal/Documents/GitHub/tika-trunk/tika-app/target/tika-app-2.0.0-SNAPSHOT.jar

java -Dner.impl.class=org.apache.tika.parser.ner.corenlp.CoreNLPNERecogniser \
      -classpath $TIKA_APP:$CORE_NLP_JAR org.apache.tika.cli.TikaCLI \
      --config=tika-config.xml -m description_only.csv

 java  -Dner.corenlp.model=edu/stanford/nlp/models/ner/english.all.3class.distsim.crf.ser.gz \
       -Dner.impl.class=org.apache.tika.parser.ner.corenlp.CoreNLPNERecogniser \
       -classpath $TIKA_APP:$CORE_NLP_JAR org.apache.tika.cli.TikaCLI \
       --config=tika-config.xml -m description_only.csv
