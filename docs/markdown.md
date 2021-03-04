# Notas de Markdown

## Énfasis y listas 

Podemos enfatizar texto con *itálicas* o _itálicas_ (asterisco o guión bajo), o con **negritas** o __negritas__ (doble asterisco o doble guión bajo). Se puede tachar ~~palabras~~. 

Listas numeradas:

1. Primer item
2. Segundo item 
   1. Sublista ordenada
   2. Sublista ordenada 2
3. Tercer item 
   * Sublista
   * Sublista 2 
4. Cuarto item 

Listas no numeradas:

* Pueden usar asteriscos
* Guiones
* Signos más

## Links

Corchetes con texto, paréntesis con URL. 

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

Signos de exclamación antes de los corchetes lo hacen imagen. 

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

## Código

Inline `code` has `back-ticks around` it.

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```
## Tables

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |



 