V_MY_PATH=$HOME
name="$(basename -- ${1} .md)"
echo ${name}
pandoc  -s --mathml -t html5 -f markdown ${1} -o ${name}.html --css=css/normalize.css --css=css/pandoc.css
rm -rf tex2pdf*/
