#-*-coding:utf-8-*-
echo imput_sent
read line
cd /Users/tachibanaryuichi/Downloads/geniatagger-3.0.1/
word=`echo $line | ./geniatagger `
echo $word
cd /Users/tachibanaryuichi/Dropbox/gitHub/100_Drill/eight
python file80.py $word > feature_for_classias.txt