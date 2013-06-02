# Pelican Pinboard Plugin

This is a plugin for Pelican that pulls in links from Pinboard and provides template tags to insert them into your Pelican template. It's basically a Pelican plugin wrapper around [python-pinboard](https://github.com/mgan59/python-pinboard), so the template tags are basically just the output of a `posts()` call, wrapped in the `pinboard_activity` keyword. This also means `python-pinboard` is a dependency.

## Setup

Once the plugin is [activated](https://github.com/jbradforddillon/pelican-plugins#how-to-use-plugins), and [python-pinboard is installed](https://github.com/mgan59/python-pinboard#python-pinboard) on your dev environemnt, the plugin requires a few constants to be set in your Pelican config file:

```python
# Required
PINBOARD_TOKEN = "jbradforddillon:0123456789ABCDEF"

# Optional
PINBOARD_URL = "https://pinboard.in/u:jbradforddillon/"
PINBOARD_COUNT = 5
PINBOARD_TAG = '#'
```

## Template Example

```html
{% if PINBOARD_TOKEN %}
<div id="bookmarks">
	<h3><a href="{{ PINBOARD_URL }}">Bookmarks</a> (via Pinboard)</h3>
	<dl>
	{% for post in pinboard_activity %}
		<dt><a href="{{ post.href }}">{{ post.description }}</a></dt>
		<dd>{{ post.extended }}</dd>
	{% endfor %}
	</dd>
</div>
{% endif %}
```