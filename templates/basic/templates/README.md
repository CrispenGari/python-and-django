# Templates

According to the documentation, A template is a text file. It can generate any text-based format (HTML, XML, CSV, etc.). A template contains variables, which get replaced with values when the template is evaluated, and tags, which control the logic of the template.

### Template inheritance

Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.

> Let's create a file called header.html and mount it in the index.html file which is our entry point in this case.

## Templates tags

- for

  ```
  {%for month in months %}
      <h3>{{forloop.counter }}. {{month | upper}} {{forloop.first}}</h3>

   {% endfor %}
  ```

  - forloop.counter  
     -The current iteration of the loop (1-indexed)
  - forloop.counter0 -The current iteration of the loop (0-indexed)
  - forloop.revcounter -The number of iterations from the end of the loop (1-indexed)
  - forloop.revcounter0 -The number of iterations from the end of the loop (0-indexed)
  - forloop.first - True if this is the first time through the loop
  - forloop.last -True if this is the last time through the loop
  - forloop.parentloop -For nested loops, this is the loop surrounding the current one

- for … empty
  ```
  {%for month in months %}
      <h3>{{forloop.counter }}. {{month | upper}} {{forloop.first}}</h3>
      {% empty %}
      <h1>There are no months!!</h1>
      {% endfor %}
  ```
- if
  ```
  {% if age == 20 %}
      <h1>You are 20 years Old</h1>
      {% elif age < 20 %}
      <h1>You are {{ age }}</h1>
      {% else %}
      <h1>You are {{ age }}</h1>
    {% endif %}
  ```
  - date()
- etc. More [Documentation](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#std:templatetag-for)
