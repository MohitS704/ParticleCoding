FILES=*.md

for file in $FILES
do
    name="$(basename -- ${file} .md)"
    echo ${name}
    pandoc  -s --mathml -t html5 -f markdown ${file} -o ${name}.html --css=css/normalize.css --css=css/pandoc.css
    rm -rf tex2pdf*/
done
