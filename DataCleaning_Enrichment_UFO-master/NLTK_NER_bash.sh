cd $HOME && git clone https://github.com/manalishah/NLTKRest-resources
 export NLTK_RES=$HOME/NLTKRest-resources
 vim $NLTK_RES/org/apache/tika/parser/ner/nltk/NLTKServer.properties

 export TIKA_APP={your/path/to/tika-app}/target/tika-app-1.13-SNAPSHOT.jar

#set the system property to use NLTKNERecogniser class
#sample output
java -Dner.impl.class=org.apache.tika.parser.ner.nltk.NLTKNERecogniser -classpath $NLTK_RES:$TIKA_APP org.apache.tika.cli.TikaCLI --config=$NLTK_RES/tika-config.xml -m  http://www.hawking.org.uk/