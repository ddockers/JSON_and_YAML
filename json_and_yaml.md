# JSON and YAML

JSON stands for JavaScript Object Notation.

It is used mainly to transport data, and it works with key:value pairs.

## Parsing

Parsing is turning a string into a data structure, and vice versa.

If the source text of the string matches what the parser programme is expecting, we should be able to output that data in the format that we want.

In the example, we'll be turning Python strings into JSON objects, and vice versa.

Firstly, we have created a JSON file called *example.json*. We can parse the data on that file in Python.

Here is the data in *example.json*:
```commandline
{
  "name": "test",
  "ip": "192.168.23.45",
  "project": "DevOps",
  "website": "spartaglobal.com"
}
```

First, the JSON library needs to be imported.
```
import json
```
Then, we need to create a variable called json and use *loads()* in the JSON library. *loads()* reads the JSON object in a file.
```
json = json.loads(open('example.json').read())
```
This is telling the script to use the JSON library, open the JSON file and read it. This content will then be put into the *json* variable.

From the json data that has now been read, we want to get the value of a key.

```commandline
value = json['name']
print(value)
```
The name of the key needs to be specified, so if we want the project, *project* needs to be typed in the square brackets.